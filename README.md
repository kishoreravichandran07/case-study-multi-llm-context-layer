# Case Study: Cross-LLM Work Context Layer

> **What this is:** A written case study, in my own words, of an internal system I
> designed and built at work. The original code, configuration, and data are not
> included here. This document describes the problem, my contribution, and what I
> learned. No company data, credentials, or coworkers' content appears in this
> repository.
>
> **Date written:** November 2026

## The problem

Coworkers across functions each used their preferred LLM for daily work. Useful
work-related context was sitting within separate individual workflows, so I built a way
for coworkers across functions to use one another's work context without asking
everyone to switch LLMs.

## My role and contribution

I identified the opportunity, designed the system, and built it. My contribution was:

- Identifying the work-related context within each person's LLM use.
- Selecting the relevant keywords used to pull that context out.
- Checking the extracted contextual data against our internal database for validity.
- Restricting access to designated coworkers through firewall controls.

## What I got wrong first

My initial assumption was that implementation across LLMs would be straightforward. It
was not, and I had to work through the context-selection differences between them.

## How I knew it worked

- I checked the contextual data against our internal database for validity.
- The practical result: designated coworkers across functions could use context from one
  another's work while keeping their preferred LLM. That cross-functional access was the
  outcome I was aiming for.

## Takeaway

A useful AI workflow depends on selecting the right context and checking the output,
not just choosing a model.

---

*For a working illustration of related ideas, see the companion repository
`demo-llm-context-layer`: a demo with synthetic data, created for this portfolio.
It is not the original system.*
