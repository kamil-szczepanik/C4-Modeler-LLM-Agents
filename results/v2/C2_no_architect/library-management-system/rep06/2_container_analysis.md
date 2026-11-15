## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It strictly enforces EU-only data residency and sub-second search performance.

## Key Elements
- **Users:** Library Patrons, Librarians/Circulation Staff, Library Administrators
- **External Systems:** EU-hosted Identity Provider (IdP), CDN/WAF Edge Services, Digital Content Vendors / Third-Party E-Resource Providers
- **Containers:** API Gateway, Patron Portal, Circulation & Cataloguing Container, Elasticsearch Container, Kafka/Redpanda Event Streaming Container, Audit & Event Tracking Container, Reporting/Analytics Container, PostgreSQL Database (Primary/Read Replica)
- **Infrastructure:** Kubernetes (managed cluster pinned to EU cloud regions), Istio Service Mesh, HashiCorp Vault, OpenTelemetry sidecars, OPA Gatekeeper

## Relationships
- Patrons and Staff access the **API Gateway** via **CDN/WAF Edge Services** using **HTTPS/TLS 1.3** and **OAuth2/OIDC (JWT)**.
- **API Gateway** routes traffic to **Patron Portal** and **Circulation & Cataloguing Container** using **mTLS**.
- **Circulation & Cataloguing** writes transactional data to **PostgreSQL Database** and publishes events via **Kafka/Redpanda**.
- **Patron Portal** queries **Elasticsearch Container** using CQRS to meet search NFRs.
- **Audit & Event Tracking Container** consumes from **Kafka/Redpanda** and populates the **Reporting/Analytics Container**.

## Technology Stack
- **Orchestration & Infrastructure:** Kubernetes with OPA Gatekeeper for EU region enforcement.
- **Security & IAM:** OAuth2/OIDC, Istio Service Mesh (mTLS), HashiCorp Vault for secrets, AES-256 encryption at rest.
- **Data & Search:** PostgreSQL (primary + read replica), Elasticsearch (for sub-second searches under R-05).
- **Streaming & Observability:** Apache Kafka/Redpanda, OpenTelemetry sidecars, Prometheus (for HPA).

## Rationale
The CQRS pattern with Elasticsearch and asynchronous Kafka streaming protects operational performance to guarantee the <800ms search NFR. Strict EU-region pinning, mTLS, and OPA Gatekeeper ensure total compliance with EU data residency and GDPR mandates.