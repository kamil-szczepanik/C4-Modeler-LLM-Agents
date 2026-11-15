## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient admissions, EMRs, scheduling, and billing while ensuring 99.99% availability and HIPAA/GDPR compliance. It implements OpenTelemetry sidecars to provide rigorous observability without impacting core clinical workflows.

## Key Elements
*   **Containers:** Web Frontend, Patient Portal / Mobile App, API Gateway, EMR Service, Billing / Claims Service, OpenTelemetry sidecars, Audit Logging sidecars, Dynamic Secrets Manager (HashiCorp Vault)
*   **Infrastructure:** on-prem-k8s cluster, AWS (`eu-central-1`)
*   **External Systems:** Insurance / Payer System, Lab & Imaging Systems (HL7 FHIR)

## Relationships
*   **Application to Sidecar:** Internal gRPC communication via localhost
*   **Sidecar to Backend:** OTLP over mTLS using SPIFFE/SPIRE identities across hybrid boundaries
*   **GitOps Controller to Sidecar:** ArgoCD deploying mutations and configurations

## Technology Stack
*   **Observability:** OpenTelemetry Collectors configured via GitOps (ArgoCD) for distributed tracing and performance monitoring.
*   **Security & Identity:** SPIFFE/SPIRE for mTLS transport, HashiCorp Vault for secrets, AES-256 for local disk buffer encryption at rest.
*   **Infrastructure:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) with mutating admission webhooks.

## Rationale
This architecture ensures continuous high availability (99.99%) by isolating sidecar resource limits and liveness probes from the primary clinical application path. Strict mTLS, cryptographic configuration verification, and regex-based PHI/PII data sanitization guarantee compliance with HIPAA and GDPR.