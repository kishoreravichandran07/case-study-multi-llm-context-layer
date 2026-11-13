"""Offline synthetic portfolio example, not the original company system.

Run python3 example.py. Uses only the Python standard library.
No LLM calls, real integrations, authentication, or firewall enforcement.
"""
import json
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYWORDS = {'deployment', 'pricing', 'customer', 'project'}


def run(data):
    """Return recipient digests and rejected records; default to no access.

    Two invented export formats normalize into structured assertions. A local
    SQLite table checks exact project/status matches, not semantic truth.
    """
    db = sqlite3.connect(':memory:')
    try:
        db.execute('CREATE TABLE projects (id TEXT PRIMARY KEY, status TEXT)')
        db.executemany('INSERT INTO projects VALUES (?, ?)',
                       [(p['id'], p['status']) for p in data['projects']])
        records = []
        for export in data['exports']:
            if export['format'] == 'chat':
                records.extend((export['owner'], m['context'])
                               for m in export['messages'] if m['role'] == 'assistant')
            elif export['format'] == 'notes':
                records.extend((export['owner'], n) for n in export['notes'])
            else:
                raise ValueError('Unsupported synthetic export format')
        digests, quarantine = {}, []
        seen = set()
        for owner, item in records:
            record_id = (owner, item['id'])
            if record_id in seen:
                continue
            seen.add(record_id)
            if item['scope'] != 'work':
                continue
            words = set(item['text'].lower().split())
            if not words & KEYWORDS:
                continue
            row = db.execute('SELECT status FROM projects WHERE id = ?',
                             (item['project_id'],)).fetchone()
            if row is None or row[0] != item['status']:
                quarantine.append({'owner': owner, 'id': item['id'],
                                   'reason': 'unknown project or conflicting status'})
                continue
            # No fallback recipient, and missing owner grant means no sharing.
            for recipient in sorted(set(data['grants'].get(owner, []))):
                digests.setdefault(recipient, []).append({
                    'owner': owner, 'id': item['id'], 'text': item['text']})
        return {'digests': digests, 'quarantine': quarantine}
    finally:
        db.close()


if __name__ == '__main__':
    print(json.dumps(run(json.loads((HERE / 'synthetic.json').read_text())), indent=2))
