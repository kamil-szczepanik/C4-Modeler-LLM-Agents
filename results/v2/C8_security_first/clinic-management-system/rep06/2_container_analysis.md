## Overview
- Manages patient admissions, EMR, scheduling, and billing for clinics using a secure hybrid Kubernetes architecture.
- Ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance via zero-trust controls and event-driven microservices.

## Key Elements
- **Users:** Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, Patient
- **External Systems:** External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP)
- **API Gateway:** Kong / Envoy handling TLS, mTLS, and OIDC validation
- **EMR & Scheduling Service:** Java / Spring Boot container backed by encrypted PostgreSQL
- **Billing & Claims Service:** Node.js / TypeScript container with local Redis/RabbitMQ message broker
- **Interoperability Service:** .NET Core / Apache Camel container for HL7 FHIR translation
- **Audit Logger Sidecar:** Lightweight container streaming immutable logs

## Relationships
- **Users to API Gateway:** HTTPS / OAuth 2.0 / OIDC tokens for authentication and request routing
- **API Gateway to EMR & Scheduling Service:** gRPC over mTLS via Istio Service Mesh
- **EMR & Scheduling Service to PostgreSQL:** Encrypted SQL over TLS with AES-256 at rest
- **Billing & Claims Service to Insurance Clearinghouses:** REST / HL7 FHIR over HTTPS with circuit breakers
- **Interoperability Service to External Lab & Imaging Systems:** HL7 FHIR APIs over HTTPS

## Technology Stack
- **Orchestration:** Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1) managed via ArgoCD for GitOps
- **Security:** Istio (Service Mesh), Cosign (image signing), Cilium Tetragon / Falco (eBPF runtime security), Vault (secret management)
- **Messaging & Resilience:** Kafka / RabbitMQ with local dead-letter queues for asynchronous billing and lab integrations
- **Observability:** OpenTelemetry, Prometheus, Grafana for distributed tracing and metrics

## Rationale
- Combines zero-trust security controls, cryptographically signed JWTs, and local caching to satisfy HIPAA/GDPR constraints while maintaining sub-second EMR screen loads.
- Utilizes active-active hybrid Kubernetes clusters, automated state replication, and message broker circuit breakers to guarantee 99.99% availability and billing resilience.