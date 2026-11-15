## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical IT operations while adhering to strict HIPAA, GDPR, and 10-year data retention mandates.

## Key Elements
- **Database Migration Container (Kubernetes Job):** Executes declarative, version-locked database schema updates during deployments.
- **Core Domain Containers (Kubernetes Pods):** Handle business logic for patient registration, scheduling, EMR, and billing.
- **Integration / FHIR Adapter Container:** Manages HL7 FHIR interactions with external lab and imaging systems.
- **Audit Logging & Compliance Container:** Captures immutable DDL and system audit trails encrypted with AES-256.
- **Observability Container:** Aggregates structured JSON logs and metrics via OpenTelemetry.

## Relationships
- **Database Migration Container** executes DDL schema updates against the production database using least-privilege credentials.
- **Core Domain Containers** communicate via gRPC/REST over Kubernetes internal networking and expose endpoints via API Gateway.
- **Integration Adapter** connects to external lab/imaging systems via HL7 FHIR over HTTPS.
- **Migration Engine** reports structured execution logs to the **Observability Container** via stdout.

## Technology Stack
- **Kubernetes (on-prem-k8s & eu-central-1):** Hybrid orchestration platform providing high availability (99.99%) and active-active scaling.
- **Helm Hooks / Init Containers:** Manages explicit dependency ordering to ensure migrations finish before core application traffic routes.
- **Distributed Advisory Locks:** Enforces single-instance migration execution in multi-replica Kubernetes environments.
- **Structured JSON Logging:** Standardizes application and migration log parsing for centralized monitoring.

## Rationale
This architecture uses Kubernetes Jobs and expand-and-contract schema patterns to achieve zero-downtime deployments under 99.99% availability constraints. Strict credential scoping, immutable version tagging, and automated pre-deployment validation ensure regulatory compliance and robust data integrity.