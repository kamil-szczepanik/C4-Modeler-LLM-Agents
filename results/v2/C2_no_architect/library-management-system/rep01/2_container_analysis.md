## Overview
[The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals.]
[The architecture enforces strict EU data residency and low-latency search constraints to serve library patrons and staff.]

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- Self-Service Portal (Public Trust Zone / DMZ)
- API Gateway (OAuth2/OIDC, JWT)
- Search Container (Elasticsearch / OpenSearch)
- Audit & Compliance Container
- User Analytics & Feedback Container
- Notification Gateway, External ILS / Book Supplier Integration, Reporting & Analytics System, Centralized Logging & SIEM Service

## Relationships
- Patrons and Staff interact with the Self-Service Portal via HTTPS / TLS 1.3
- API Gateway routes requests to core containers using mTLS via SPIFFE/SPIRE
- Search Container receives data via asynchronous Change-Data-Capture (CDC) pipelines
- User Analytics & Feedback Container ingests telemetry via asynchronous message queues (Kafka / Fluentbit sidecars)
- Monitoring via Prometheus and Grafana

## Technology Stack
- Kubernetes: Container orchestration with node affinity rules for EU-only data residency
- Elasticsearch / OpenSearch: Horizontally scalable search engine for R-05 (< 800 ms p99 search)
- OAuth2/OIDC & JWT: Authentication and RBAC at the API Gateway
- TLS 1.3 / mTLS: Inter-container communication encryption
- AES-256: Encryption at rest for persistent storage with EU-localized HSM

## Rationale
- Decouples the Search Container via asynchronous CDC to guarantee the 99th-percentile search response time under 800 ms.
- Enforces strict EU data residency and GDPR compliance using Kubernetes node affinity, EU cloud availability zones, and an isolated Audit & Compliance container.