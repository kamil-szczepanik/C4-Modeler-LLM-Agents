## Overview
The Library Management System is a cloud-hosted EU solution designed to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and sub-800ms search response times.

## Key Elements
* **Users:** Patrons (Students, Researchers, Public), Librarians, Library Administrators.
* **Core System:** Library Management System (LMS) deployed exclusively in EU cloud regions.
* **External Systems:** Academic Identity Providers (Shibboleth/SAML/OIDC), Payment Gateway (PCI-DSS compliant), Digital Content Providers, EU Notification Gateway.
* **Infrastructure Components:** Elasticsearch/OpenSearch tier, EU-hosted KMS, centralized telemetry engine.

## Relationships
* **Patrons/Librarians -> LMS:** HTTPS (TLS 1.3) via Web and Mobile clients.
* **LMS -> Academic IdPs:** OIDC and SAML federation over HTTPS.
* **LMS -> Payment Gateway & Digital Content Providers:** REST/JSON over HTTPS with mTLS and OAuth2 token exchange.
* **LMS -> EU Notification Gateway:** Asynchronous webhooks and REST APIs over HTTPS (TLS 1.3).

## Technology Stack
* **Cloud & Infrastructure:** Infrastructure-as-Code deployed in EU regions (Frankfurt/Dublin) for data residency.
* **Search & Performance:** Elasticsearch/OpenSearch tier to decouple queries and meet <800ms response targets.
* **Security & Encryption:** TLS 1.3 for data in transit; AES-256 for database storage and backups via EU-hosted KMS.
* **Authentication & Resilience:** OIDC/SAML federations, mutual TLS (mTLS) for service-to-service communication, circuit breakers, and dead-letter queues.

## Rationale
This architecture guarantees strict EU data residency compliance and robust security controls without introducing friction to the user experience. Decoupling search indexing and utilizing asynchronous notification processing ensures high performance (<800ms) and operational resilience.