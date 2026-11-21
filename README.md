# Web Abuse Detection Lab | DR Disso

**Laboratoire de dÃ©tection des abus web**

[![Tests](https://github.com/566653/dr-disso-web-abuse-detect/actions/workflows/tests.yml/badge.svg)](https://github.com/566653/dr-disso-web-abuse-detect/actions/workflows/tests.yml)

## English

Detect suspicious web requests, injection attempts and credential attacks from sanitized logs.

A **working, offline, rule-based investigation prototype** with auditable JSON findings, SHA-256 source integrity, sample records and unit tests. No cloud account or external API required.

### Quick start

```bash
python engine.py data/sample.json --output report.json
python -m unittest discover -s tests -v
```


### Ethical use

Use only your own data or data collected with appropriate legal authorization. Preserve originals; investigate copies. A flag is **not** proof of wrongdoing, attribution or guilt. This project does not access live devices, private accounts or third-party systems.

## FranÃ§ais

DÃ©tecter les requÃªtes suspectes, tentatives d'injection et attaques d'identifiants.

Prototype fonctionnel **hors ligne**, fondÃ© sur des rÃ¨gles explicables : rapports JSON, empreintes SHA-256, exemples synthÃ©tiques et tests automatisÃ©s.

Lancement : `python engine.py data/sample.json --output rapport.json`.

Utilisez uniquement des donnÃ©es autorisÃ©es. Les alertes sont des pistes d'investigation, jamais une preuve d'identitÃ© ou de culpabilitÃ©.

## Contribute / Contribuer

Security researchers and defensive developers are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue or a pull request for improvements, tests, parsers or documentation. Please do not upload real victim data.

## Discover / DÃ©couvrir

GitHub Topics: cybersecurity, digital-forensics, incident-response, cybercrime-investigation, python

**Author / Auteur:** DR Disso
