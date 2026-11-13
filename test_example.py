import copy
import json
import unittest
from pathlib import Path
from example import run


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path(__file__).with_name('synthetic.json').read_text())

    def test_two_adapters_and_separate_grants(self):
        out = run(self.data)
        self.assertEqual([r['id'] for r in out['digests']['sam']], ['C1'])
        self.assertEqual([r['id'] for r in out['digests']['alex']], ['N1'])
        self.assertNotIn('priya', out['digests'])

    def test_conflicting_and_unknown_assertions_quarantined(self):
        self.assertEqual({r['id'] for r in run(self.data)['quarantine']}, {'C2', 'N2'})

    def test_personal_item_with_work_keyword_excluded(self):
        self.assertNotIn('C3', json.dumps(run(self.data)))

    def test_default_deny(self):
        self.data['grants'] = {}
        self.assertEqual(run(self.data)['digests'], {})

    def test_duplicate_does_not_duplicate_digest(self):
        messages = self.data['exports'][0]['messages']
        messages.append(copy.deepcopy(messages[0]))
        self.assertEqual(len(run(self.data)['digests']['sam']), 1)

    def test_no_cross_owner_leak(self):
        self.data['grants']['alex'] = []
        self.assertNotIn('sam', run(self.data)['digests'])
        self.assertEqual([r['owner'] for r in run(self.data)['digests']['alex']], ['priya'])

    def test_no_input_mutation(self):
        original = copy.deepcopy(self.data)
        run(self.data)
        self.assertEqual(self.data, original)

    def test_unsupported_adapter_rejected(self):
        self.data['exports'][0]['format'] = 'unsupported'
        with self.assertRaises(ValueError):
            run(self.data)


if __name__ == '__main__':
    unittest.main()
