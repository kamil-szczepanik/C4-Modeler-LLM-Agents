## Overview
The Library Management System is a comprehensive digital solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures high performance and strict compliance with EU-only data residency constraints.

## Key Elements
- **Users**: Library Patrons, Librarians / Circulation Staff, Library Administrators
- **Containers**: Self-Service Portal, API Gateway, Search Container, Audit & Compliance Container, User Analytics & Feedback Container
- **External Systems**: Notification Gateway, External ILS / Book Supplier Integration, Reporting & Analytics System, Centralized Logging & SIEM Service
- **Security & Infrastructure**: EU-localized HSM, Kubernetes, SPIFFE/SPIRE, ArgoCD

## Relationships
- Self-Service Portal -> API Gateway: Routes requests using mTLS via SPIFFE/SPIRE
- API Gateway -> Search Container: Routes search requests using mTLS via SPIFFE/SPIRE with W3C Trace Context injection
- API Gateway -> Audit & Compliance Container: Routes audit requests using mTLS via SPIFFE/SPIRE
- API Gateway -> User Analytics & Feedback Container: Routes analytics requests using mTLS via SPIFFE/SPIRE

## Technology Stack
- **API Gateway**: Handles OAuth2/OIDC token validation, JWT processing, WAF input sanitization, OpenAPI schema validation, and rate limiting to meet R-05 (<800ms p99 search response).
- **Security Protocols**: mTLS via SPIFFE/SPIRE, W3C Trace Context (`traceparent`) headers, OAuth2 Token Revocation, and Strict CORS/Security Headers.
- **Search Engine**: Elasticsearch / OpenSearch for high-performance cataloguing and retrieval.
- **Deployment & Observability**: Kubernetes, ArgoCD for GitOps, Kafka / Fluentbit sidecars, and EU-localized HSM / Kubernetes Secrets Operator.

## Rationale
This architecture uses an API Gateway with edge security controls, rate limiting, and mTLS to protect sensitive user PII while maintaining sub-800ms search latencies. Declarative GitOps deployment and strict localized secret management ensure continuous compliance with EU data residency mandates.