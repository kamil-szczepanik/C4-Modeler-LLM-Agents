## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries within an EU data residency boundary. It ensures high-performance patron search capabilities and robust administrative workflows.

## Key Elements
* Library Patrons (Students, Public Citizens)
* Librarians / Library Staff
* Library Administrators
* Third-Party Vendors / Interlibrary Loan (ILL) Partners
* Library Management System (System-in-Scope)
* EU Identity Provider (Keycloak / EU Auth0)
* Digital Content Delivery Network / S3-compatible EU Object Storage
* SEPA / Stripe EU API Payment Gateway
* External Notification Service (EU Mailgun / Twilio)
* Centralized SIEM / Monitoring Platform (Datadog EU / Grafana Cloud Frankfurt)

## Relationships
* Library Patrons to Library Management System via HTTPS/TLS 1.3 for self-service portals
* Librarians and Administrators to Library Management System via HTTPS/TLS 1.3 for cataloging and management
* Library Management System to EU Identity Provider via OpenID Connect / OAuth 2.0
* Library Management System to Digital Content Storage via HTTPS
* Library Management System to Payment Gateway via REST API over HTTPS
* Library Management System to ILL Partners via ISO ILL protocol or REST/JSON over HTTPS with mTLS
* Library Management System to Notification Service and SIEM via HTTPS/TLS 1.3

## Technology Stack
* OpenID Connect / OAuth 2.0 via Keycloak or EU Auth0: Ensures identity data remains strictly within EU boundaries
* S3-compatible EU-region Object Storage: Fulfills digital item cataloging and streaming requirements (R-01)
* SEPA / Stripe EU API: Handles regulated fines and fee processing
* HTTPS / TLS 1.3 with mTLS: Enforces secure transport across all external and internal integrations
* Datadog EU / Grafana Cloud Frankfurt: Provides centralized audit logging and telemetry within the EU

## Rationale
This architecture guarantees strict EU data residency compliance while isolating workloads to meet the p99 search response time under 800ms. External integrations utilize resilient protocols, circuit breakers, and asynchronous queuing to protect core library operations from third-party latency.