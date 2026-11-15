## Overview
The Library Management System is a cloud-native platform providing self-service portals, circulation management, and cataloguing for public and academic libraries. It ensures strict EU data residency while meeting high-performance search requirements.

## Key Elements
* **Patrons & Library Staff:** End-users accessing self-service portals, circulation, and cataloguing tools.
* **Library Management System:** Core software system handling inventory, loans, and search functionality.
* **EU-bound API Gateway:** Perimeter element enforcing rate-limiting, TLS termination, and payload sanitization.
* **Payment Gateway:** External system processing fines and fees.
* **Digital Content Providers:** External system supplying e-books and digital media licenses.
* **Inter-Library Loan Networks:** External system enabling resource sharing and partner catalogue exchange.

## Relationships
* Patrons & Library Staff -> Library Management System: Interacts via HTTPS, TLS 1.3, and OIDC/MFA.
* Library Management System -> Payment Gateway: Processes transactions via REST/JSON over TLS 1.3 with mTLS and circuit breakers.
* Library Management System -> Digital Content Providers: Syncs inventory via REST/JSON over TLS 1.3 using async caching.
* Library Management System <-> Inter-Library Loan Networks: Exchanges metadata via REST/JSON over TLS 1.3, mTLS, and asynchronous webhooks.

## Technology Stack
* **Cloud-Native Microservices:** Hosted exclusively in EU-compliant data centres to satisfy data residency constraints.
* **Active-Active Multi-Region Deployment:** Frankfurt and Dublin with Anycast DNS routing for high availability and regional failover.
* **API Gateway:** Perimeter routing, rate-limiting, and payload sanitization.
* **OpenTelemetry:** Distributed tracing and centralized logging for latency and SLA monitoring.
* **AES-256:** At-rest data encryption with a regionally isolated KMS.

## Rationale
This architecture uses multi-region EU-pinned infrastructure and asynchronous inventory caching to guarantee compliance with EU-only data residency. Additionally, it protects the 800ms search latency SLA under load.