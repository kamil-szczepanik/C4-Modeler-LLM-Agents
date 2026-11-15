## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures high performance and strict EU-only data residency compliance.

## Key Elements
* Library Member (Patron)
* Librarian / Staff
* Library Administrator
* Library Management System (Software System / Kubernetes containers)
* EU Identity Provider (SaaS / OAuth2/OIDC)
* EU Payment Gateway (REST / HTTPS)
* EU-hosted Log & Telemetry Aggregator

## Relationships
* Users to Library Management System via HTTPS (TLS 1.3)
* Library Management System to EU Identity Provider via OIDC / HTTPS
* Library Management System to EU Payment Gateway via REST / HTTPS with asynchronous queueing
* Library Management System to EU-hosted Log & Telemetry Aggregator via Syslog / TLS
* Internal service-to-service communication via mTLS

## Technology Stack
* Kubernetes: Containerized deployment to enforce EU-region isolation and scalability
* OpenID Connect (OIDC): Secure authentication with mandatory MFA for staff and administrators
* AES-256: Database and cache encryption at rest managed via an EU-hosted KMS
* Prometheus: Metrics collection for monitoring the R-05 search latency (<800ms) requirement

## Rationale
This architecture uses cloud-native containerization and EU-hosted services to strictly satisfy data residency constraints. Microservices and asynchronous queueing ensure low latency search performance and resilience against third-party outages.