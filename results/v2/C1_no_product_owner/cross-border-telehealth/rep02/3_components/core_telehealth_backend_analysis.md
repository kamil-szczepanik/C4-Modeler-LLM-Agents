## Overview
The Core Telehealth Backend is a secure, regionally isolated microservice built to manage cross-border video consultations, e-prescriptions, and AI symptom checking under strict healthcare compliance frameworks. It enforces regional data residency and low-bandwidth resiliency for patients across the EU and the US.

## Key Elements
- **Core Telehealth Backend**: Go-based container running on GKE (Anthos).
- **Consent & Policy Engine**: Go component for ABAC/RBAC and regional tenant isolation.
- **Consultation Coordinator**: Go component managing session states and workflows.
- **Resiliency & Fallback Manager**: Go component handling low-bandwidth modes and Protobuf serialization.
- **Audit Logging Daemon**: Fluentbit/OTel sidecar container for tamper-resistant log shipping.
- **GCP Infrastructure**: GKE, Anthos Service Mesh, Cloud SQL, WORM Storage, Cloud KMS, and Secret Manager.

## Relationships
- **GCP API Gateway -> Core Telehealth Backend**: Routes validated client requests via mTLS and Anthos Service Mesh (Istio).
- **Core Telehealth Backend -> AI Symptom Checker Service**: Sends analysis requests via gRPC over mTLS.
- **Core Telehealth Backend -> EU E-Prescriptions Adapter & US Interoperability Service**: Integrates with regional healthcare gateways via gRPC over mTLS.
- **Core Telehealth Backend -> GCP Cloud SQL & WORM Storage**: Persists transactional data and compliance logs using CMEK encryption.

## Technology Stack
- **Go**: Chosen for high performance and low concurrency overhead to support degraded network modes.
- **Protobuf**: Utilized for compact binary data serialization under low-bandwidth conditions (<300 kbit/s).
- **Istio Service Mesh**: Enforces mTLS, circuit breaking, and zero-trust service-to-service authorization.
- **GKE & Anthos**: Enables regionally isolated deployments in `europe-west3` and `us-central1`.
- **Cloud KMS**: Provides regionally segregated Customer-Managed Encryption Keys to enforce data residency.

## Rationale
This architecture guarantees strict regional data residency and regulatory compliance (GDPR/HIPAA) through isolated deployments and CMEK encryption. The Go-based backend with an OTel sidecar and dedicated fallback management ensures high availability and accountability even over unstable rural internet connections.