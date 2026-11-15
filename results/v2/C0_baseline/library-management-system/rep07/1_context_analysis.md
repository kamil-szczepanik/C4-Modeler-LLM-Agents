## Overview
The Library Management System is a EU-compliant platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict data residency and high-performance search capabilities.

## Key Elements
* **Personas:** Library Patrons, Librarians / Circulation Staff, Library Administrators, Third-Party Vendors / Digital Content Providers.
* **Core System:** Library Management System.
* **External Systems:** EU Payment Gateway, Notification Service.
* **Containers:** Asynchronous Staging Container, Internal Message Broker, Core Search and Circulation microservices.

## Relationships
* **Library Patrons, Librarians, Administrators -> Library Management System:** HTTPS (TLS 1.3), OAuth 2.0 / OIDC authentication.
* **Library Management System -> EU Payment Gateway:** HTTPS/REST protocols.
* **Library Management System -> Notification Service:** HTTPS/SMTP protocols via message broker.
* **Third-Party Vendors -> Library Management System:** SFTP / HTTPS REST webhooks.
* **Internal Containers:** mTLS with SPIFFE/SPIRE workload identities.

## Technology Stack
* **Edge & Routing:** Geo-DNS and Anycast CDN constrained to EU Points of Presence to meet performance SLAs.
* **Message Broker:** EU-hosted Kafka or RabbitMQ for asynchronous notification decoupling.
* **Security & Secrets:** HashiCorp Vault / AWS KMS EU for secrets management; AES-256 and TLS 1.3 for data protection.
* **Observability:** W3C Trace Context for distributed tracing across services.

## Rationale
This architecture enforces strict EU data residency and GDPR compliance while maintaining isolated asynchronous ingestion to meet the sub-800ms search latency requirement. Secure zero-trust controls ensure robust data protection across all internal and external touchpoints.