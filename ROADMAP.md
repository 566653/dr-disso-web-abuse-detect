# Security and capability roadmap / Feuille de route

This repository is an early **offline, defensive research prototype**, not a certified investigative system. No 90% accuracy, readiness or completeness is claimed.

## Comparable open-source projects (design inspiration only)
- DFIR-IRIS (case management and evidence handling): https://www.dfir-iris.org/
- MISP (structured threat indicators and provenance): https://github.com/MISP/MISP
- OpenCTI (structured intelligence and relationships): https://github.com/OpenCTI-Platform/opencti
- Prowler (auditable checks and reporting): https://github.com/prowler-cloud/prowler

## Prioritized next steps
1. Project-specific threat model, user requirements and privacy impact review
2. Versioned input/output schemas, strict validation, bounded data sizes and meaningful errors
3. Evidence provenance, timestamps, reproducible exports and deterministic test fixtures
4. False-positive and false-negative evaluations with consented, representative datasets
5. Automated regression tests, secure CI, dependency inventory and reproducible releases
6. User documentation in French and English; accessibility and deployment guidance
7. Independent code review and documented acceptance tests before real-world use

These are proposed improvements, not currently implemented features. Do not upload sensitive case data or treat indicators as proof of identity or wrongdoing.
