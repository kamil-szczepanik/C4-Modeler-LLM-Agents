## Overview
[A secure, multi-region Core Services Container built with Node.js and NestJS that handles consultations, e-prescriptions, and regulatory compliance for the Cross-Border Telehealth Platform.]

## Key Elements
* Consultation Management Component (TypeScript/NestJS Module)
* E-Prescription Routing Component (TypeScript/NestJS Module)
* Consent Enforcement Component (TypeScript/NestJS Module)
* Audit Logging Component (TypeScript/NestJS Module)
* GCP Cloud Run / Google Kubernetes Engine
* GCP Cloud SQL (PostgreSQL with PgBouncer)
* GCP BigQuery
* GCP Secret Manager and Cloud KMS

## Relationships
* GCP Cloud Endpoints / Envoy API Gateway -> Consent Enforcement Component [gRPC over mTLS via Anthos Service Mesh]
* Consent Enforcement Component -> Cloud SQL (PostgreSQL with PgBouncer) [SSL/TLS-encrypted PostgreSQL connections]
* Audit Logging Component -> GCP BigQuery [Asynchronous event stream with cryptographic signing]
* Core Services Container -> GCP Secret Manager [Runtime secret retrieval via IAM]

## Technology Stack
* Node.js / NestJS: Modular framework for backend business logic and micro-module separation.
* TypeScript: Strong typing for reliable data modeling and schema validation via `class-validator`.
* OpenTelemetry: Distributed tracing across all modules and gateway interfaces.
* GCP Secret Manager & KMS: Runtime secret injection and application-layer envelope encryption for PHI.
* Distroless Node.js Base Image: Container hardening with read-only root filesystems and non-root execution.

## Rationale
[This modular NestJS architecture enforces strict regional data isolation and consent controls required for GDPR and HIPAA compliance. Asynchronous eventing, cryptographic audit logging, and distroless container hardening ensure high availability, zero log loss, and robust security for cross-border healthcare workloads.]