## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, appointments, and billing for healthcare facilities. It ensures strict HIPAA and GDPR compliance while maintaining 99.99% availability and high-performance clinical workflows.

## Key Elements
- **Users**: Patients, Clinical Staff, Administrative & Billing Staff, Clinic Administrators/Compliance Officers.
- **External Systems**: Lab and Imaging Systems.
- **Containers**: API Gateway, Patient Portal, EMR & Billing Containers, Analytics & Audit Reporting Container, Patient Notification Microservice.
- **Infrastructure**: On-Premises Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`), ArgoCD Control Plane, Istio Service Mesh, HashiCorp Vault.

## Relationships
- Patients & Staff interact with the API Gateway via HTTPS / OAuth2 / OIDC.
- Inter-container traffic communicates via gRPC / HTTPS secured with mTLS over Istio Service Mesh.
- External Lab & Imaging Systems integrate via HL7 FHIR APIs.
- EMR & Billing containers connect to encrypted PostgreSQL databases using PgBouncer connection pooling.

## Technology Stack
- **Orchestration & GitOps**: Kubernetes (`on-prem-k8s`, `eu-central-1`) managed via ArgoCD for multi-cloud consistency.
- **Security & Mesh**: Istio Service Mesh (mTLS), HashiCorp Vault (Secrets), OPA/Gatekeeper (Policy), Cosign/Sigstore (Image Signing), Falco/Tetragon (eBPF Runtime Security).
- **Observability**: OpenTelemetry with payload scrubbing, Datadog/Prometheus for tracing and monitoring.
- **Data & Resilience**: PostgreSQL with AES-256 encryption at rest, PgBouncer, AWS S3 with Object Lock for 10-year retention.

## Rationale
This architecture isolates Protected Health Information (PHI) within a zero-trust microsegmentation zone to satisfy rigorous HIPAA and GDPR regulations. Furthermore, decoupling resource-heavy analytics and billing tasks protects core EMR performance, ensuring clinician screen loads remain under 1 second.