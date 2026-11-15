## Overview
[The system is a Library Management System providing a self-service Patron Portal for public and academic library users. Its core purpose is to deliver fast catalogue search, circulation management, and digital resource access while enforcing strict EU-only data residency and privacy mandates.]

## Key Elements
- Library Patrons (Students, researchers, public members)
- API Gateway (Istio Service Mesh / Kubernetes Gateway)
- Patron Portal (Web Frontend / Backend Service)
- Elasticsearch Container (Search & CQRS read store)
- Kafka/Redpanda Event Streaming Container (Apache Kafka / Redpanda)
- EU-hosted Identity Provider (IdP)
- CDN/WAF Edge Services
- Digital Content Vendors / Third-Party E-Resource Providers
- Audit & Event Tracking Container

## Relationships
- Library Patrons -> CDN/WAF Edge Services: Accesses self-service portal [HTTPS]
- CDN/WAF Edge Services -> API Gateway: Routes traffic [HTTPS]
- API Gateway -> Patron Portal: Routes traffic [mTLS]
- Patron Portal -> Elasticsearch Container: Queries catalogue search data using CQRS [REST/TCP]
- Patron Portal -> EU-hosted Identity Provider (IdP): Authenticates users via short-lived signed JWTs [OAuth2/OIDC]
- Patron Portal -> Digital Content Vendors: Accesses e-resources using OAuth2/OIDC token-exchange patterns [HTTPS]
- Patron Portal -> Kafka/Redpanda Event Streaming Container: Publishes notification and audit events asynchronously [TCP]

## Technology Stack
- Kubernetes / Istio Service Mesh: Multi-AZ deployment with HPA tied to latency for resilience and performance.
- Elasticsearch: Backs CQRS architecture to satisfy the <800ms search NFR.
- Apache Kafka / Redpanda: Decouples proactive notifications and audit logging from core transactional traffic.
- OpenTelemetry: Provides end-to-end distributed tracing with PII scrubbing for GDPR compliance.
- TLS 1.3 / mTLS: Secures all service-to-service communication within the mesh.
- OAuth2/OIDC: Manages secure authentication, session handling, and vendor token exchange.

## Rationale
[This architecture ensures high performance and sub-800ms search response times through a dedicated CQRS Elasticsearch backend and edge caching. It rigorously enforces EU-only data residency and GDPR compliance via PII scrubbing, mTLS transit security, and secure token-exchange patterns.]