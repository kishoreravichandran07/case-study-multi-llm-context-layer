# Case Study: Cross-LLM Work Context Layer

> **What this is:** A written case study of an internal system I designed and built at work.
> The original code and data belong to my employer and are not shared here.
> This document describes the problem, my design, and what I learned. No company data,
> credentials, or coworkers' content appears in this repository.
>
> **Date written:** November 2026

## The problem

Coworkers across functions each used their preferred LLM for daily work. Useful work
context - decisions, customer notes, analysis, drafts - was accumulating inside separate,
individual LLM workflows. There was no way for a colleague in another function to benefit
from that context without asking everyone to standardize on a single tool, which nobody
wanted.

## My role and contribution

I identified the opportunity, designed the system, and built it. Specifically, I:

- Identified what counted as *work-related* context inside each person's individual LLM
  usage, versus personal or noise.
- Selected the relevant keywords and extraction rules used to pull that context out.
- Built a synthesis layer so context from one person's workflow could be used by
  designated coworkers in other functions, while everyone kept their preferred LLM.
- Validated extracted contextual data against our internal database before it was
  treated as usable.
- Restricted access to designated coworkers through firewall controls, so context was
  shared only with the people it was meant for.

## What I got wrong first

My initial assumption was that implementation would be straightforward across different
LLMs. It was not. Each LLM surfaced and structured context differently, so the hard part
was not "choosing a model" - it was selecting the *right context* per source and checking
the output. That context-selection difference is where most of the real work went.

## How I knew it worked

- Extracted contextual data checked against the internal database for validity.
- The practical result: designated coworkers across functions could use context from one
  another's work while keeping their preferred LLM. That cross-functional access was the
  outcome I was aiming for.

## Takeaway

A useful AI workflow depends on selecting the right context and verifying the output,
not just choosing a model. Access control and validation are part of the product, not
an afterthought.

---

*For a working demonstration of related ideas, see the companion repository
`demo-llm-context-layer`, which is new portfolio work built with synthetic data and
clearly labeled as such - it is not the original company system.*
