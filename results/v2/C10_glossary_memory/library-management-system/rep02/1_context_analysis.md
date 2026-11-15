## Overview
The Library Management System provides public and academic libraries with catalogue management, circulation control, and self-service portals. It enforces strict EU-only data residency and meets high-performance search requirements.

## Key Elements
* Library Patrons (Students, Public Citizens)
* Circulation Staff and Library Administrators
* Library Management System (Internal Software System)
* Identity Provider / SSO (External System supporting SAML/Shibboleth and local accounts)
* Digital Content Providers (External Vendor Systems for e-books/audiobooks)
* Notification Gateway (External SMS/Email Provider)
* Observability & Logging Platform (Prometheus/Grafana)

## Relationships
* Patrons, Staff, and Administrators to Library Management System via HTTPS (Web/Mobile) using TLS 1.3
* Library Management System to Identity Provider via OIDC/SAML over HTTPS
* Library Management System to Digital Content Providers via HTTPS/REST with mutual TLS (mTLS)
* Library Management System to Notification Gateway via asynchronous HTTPS/REST webhooks

## Technology Stack
* OAuth 2.0 / OIDC with JWT: Secure, token-based authentication and authorization
* TLS 1.3 and mTLS: Mandatory encryption for all internal and external network communications
* Asynchronous Message Queues: Decouples notification dispatch and third-party integrations to protect performance
* EU-pinned Cloud Regions: Ensures strict compliance with EU-only data residency and GDPR constraints

## Rationale
This architecture offloads federated authentication and third-party digital lending while strictly isolating PII within EU boundaries. Asynchronous processing and caching layers guarantee the 99th-percentile search response time remains below 800 ms.