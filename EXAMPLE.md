# Runnable example: context validation and sharing

New illustrative portfolio work, November 2026. This example uses invented data and invented implementation choices. It is not the original company system, a reconstruction of its source, or a statement about its technology stack. The historical case study remains in README.md.

## Run locally

Python 3.10 or newer. No packages, account, network connection, or credentials needed.

```sh
python3 example.py
python3 -m unittest test_example.py -v
```

Run these commands from this repository's root. The first command reads synthetic.json and prints JSON without changing files.

## What it demonstrates

- Two synthetic export adapters normalize chat and notes into structured records.
- Work-scope and keyword filters exclude unrelated items.
- An in-memory SQLite table checks project IDs and exact status values.
- Unknown or conflicting assertions enter quarantine, not recipient digests.
- Explicit per-owner recipient lists default to no sharing.
- Duplicate record IDs within an owner's input are processed once.

Expected result: sam receives C1 from alex; alex receives N1 from priya. C2 and N2 are quarantined. Personal item C3 is excluded. Eight tests cover these checks and input immutability.

## Limits

This is an offline mechanics example. Structured assertions and scope labels are supplied in the fixture, not extracted or verified by an LLM. Matching a stored status does not prove a statement is true, current, complete, or safe to share. Keywords are not a privacy classifier. Duplicate IDs assume consistent source records; conflicting versions need a real versioning policy. Local recipient-list filtering is not authentication, authorization infrastructure, or firewall isolation. Quarantine output is for a local operator, not for recipients. Input schema validation, persistent storage, encryption, retention policies, concurrency, and real provider adapters are outside this example. Do not use real company or personal data with it.
