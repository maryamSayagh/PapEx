| theme    | default |
| -------- | ------- |
| paginate | true    |

# PapEx — A Living Systematic Review Engine with Analytical Extraction

*(These slides summarize my project notes and design documents, drafted with AI assistance for structure and phrasing. The design and methodology are my own.)*

**Call for contribution**

**Can a systematic review update itself, and pull out the analytics it needs, in one pass over the literature?**

---

## Summary

**What PapEx is, in four points**

- Systematic reviews go stale because updating them is manual work, and existing open tools help with screening but stop before extraction.
- PapEx screens and extracts in one probabilistic pass, so the output is a structured dataset rather than a filtered reading list.
- Many studies each report a frequentist result, not a dataset. Collected together, those results become one table that can be modeled Bayesianly.
- The current release fetches and normalizes papers from several providers. The analytical core is designed and open to contribution.

---

## Content Overview

1- Why systematic reviews go stale

2- What existing open tools do and do not do

3- Screening and extraction as one pass

4- Why the output is a dataset, not a reading list

5- The pipeline, from a seed paper to a structured table

6- Relevance as a probability over protocol elements

7- One paper, several fields

8- Outcome extraction: the hard branch

9- PRISMA, transparency, reproducibility

10- What the current release does

11- Where contribution is needed

---

## Why Systematic Reviews Go Stale

**A review reflects the literature only up to its search date**

- Every systematic review is a snapshot. New studies appear the moment it is published and start to erode it.
- Updating a review by hand means redoing the search, the screening, and the extraction. Most reviews are never updated for exactly this reason.
- A living review re-runs itself as new papers arrive. The bottleneck is not the search. It is the manual work of screening each paper and pulling the numbers out of it.

---

## What Existing Open Tools Do and Do Not Do

**Screening is assisted; extraction is not**

- ASReview and similar tools rank papers by predicted relevance, so a reviewer reads the likely-relevant ones first. This helps, but it ends at a reading list.
- Reading each kept paper and extracting its effect sizes, outcomes, and design elements is still done by hand, and that is the step that consumes the time.
- No open tool I am aware of does living review and analytical extraction together. PapEx targets that gap.

---

## Screening and Extraction as One Pass

**Deciding a paper is relevant is deciding what it contains**

- Relevance in PapEx is not "is this on topic" but "does this paper hold the elements my protocol needs": the PICO / PECO variables of population, intervention, comparator, outcome.
- Estimating the probability that those elements are present is the keep-or-discard decision, and it already locates the content to extract.
- Screening and extraction collapse into one probabilistic pass. This is the core of the project and the hardest part to build, which is why it is the part still open.

---

## Why the Output Is a Dataset, Not a Reading List

**Many frequentist results become one Bayesian table**

- A single study reporting frequentist statistics gives a result, not data to re-analyze. There is no dataset inside one paper.
- The reported results of many studies, gathered together, form a dataset assembled across the literature rather than found in any one paper.
- That table serves as a Bayesian foundation: the individual hypotheses drop away, and what gets modeled is the pattern across all of them. Building that table is the point of PapEx.

---

## The Pipeline, from a Seed Paper to a Structured Table

**The intended end-to-end flow**

- Start from a few known-good papers. Fetch and normalize records from providers, and store metadata.
- Extract titles and abstracts, derive candidate keywords with KeyBERT, and score each paper against the protocol.
- For kept papers, expand synonyms and classify the P / I / C / O elements with SciBERT + LoRA, handling the outcome branch separately.
- The result is a flat table of studies and their extracted elements, ready for synthesis.

---

## Relevance as a Probability over Protocol Elements

**A learned scoring rule with a human fallback**

- Each paper gets a relevance score from weighted keyword evidence across keyword types, normalized so scores are comparable.
- Papers above a threshold are accepted. The weights are learned from a curated set where acceptance is already known, then refined as new papers pass through.
- Low-confidence decisions go to human review instead of being guessed, and the reviewed cases feed back into the keyword set.

---

## One Paper, Several Fields

**Why a single global score is unfair**

- A paper spanning two fields loses under one score: the dominant field contributes more high-scoring keywords, and the minority field gets ruled out.
- Scoring each paper per field and taking the strongest judges a cross-disciplinary paper by its best-fitting field rather than an averaged one.
- The same holds for protocols. A paper is scored across field-and-protocol combinations and can belong to more than one. The structure of the rule was selecting outcomes on its own, and making it explicit corrects that.

---

## Outcome Extraction: The Hard Branch

**Outcomes carry the result and resist classification**

- Population and intervention can often be caught by classification and entity detection. Outcomes cannot: they are phrased differently in every paper and hold the actual finding.
- The outcome branch does more: detect whether an outcome is reported, extract its span, clean and rephrase it into a comparable form, cluster similar outcomes, and score confidence.
- This branch turns prose into a measurement. It is the least finished part of the design and where the project most needs help.

---

## PRISMA, Transparency, Reproducibility

**A living review still has to be auditable**

- Automating screening and extraction is only acceptable if every decision can be traced, which PRISMA requires of any systematic review.
- The design records the full pipeline as a stored, re-runnable specification, so a review can be reproduced and re-executed as the literature grows.
- The keyword rules, thresholds, and per-paper scores are the justification a reviewer would otherwise write by hand.

---

## What the Current Release Does

**The state of the code today**

- The released library covers the foundation layer: it fetches and normalizes academic papers from multiple providers (Elsevier, arXiv, PRISM, IEEE, and others) into a consistent format.
- It does not yet do the unified screening-and-extraction that defines the project.
- Repository: [github.com/maryamSayagh/PapEx](https://github.com/maryamSayagh/PapEx)

---

## Where Contribution Is Needed

**Open call**

- The screening-as-extraction core: relevance scoring and element detection in a single pass.
- The outcome branch: span extraction, normalization, and clustering of reported results into comparable measurements.
- The reconciliation layer: assembling many studies' statistics into one table for Bayesian synthesis, with a PRISMA-transparent record.
- Issues, ideas, and pull requests on any of these are welcome at [github.com/maryamSayagh/PapEx](https://github.com/maryamSayagh/PapEx).

---
