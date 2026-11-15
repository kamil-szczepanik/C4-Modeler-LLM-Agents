## Overview
The Core Telehealth Service orchestrates cross-border video consultations, e-prescriptions, and AI symptom checking on Google Kubernetes Engine. It enforces strict regional data residency and compliance for patients in the EU and US.

## Key Elements
- **Consultation Orchestrator (Go):** Manages session lifecycles and workflow coordination.
- **E-Prescription Workflow Engine (Go):** Coordinates regional pharmacy routing.
- **Consent & Privacy Manager (Go):** Evaluates granular patient consent policies.
- **Audit & Traceability Logger (Go):** Captures immutable compliance and AI logs.
- **Infrastructure & Security:** GCP VPC Service Controls, Istio Service Mesh, Cloud SQL PostgreSQL, and Cloud KMS.

## Relationships
- **Consultation Orchestrator -> Consent & Privacy Manager:** Queries active consent [Internal gRPC via mTLS]
- **E-Prescription Workflow Engine -> Audit & Traceability Logger:** Emits compliance events [In-memory channel / internal event bus]
- **Core Telehealth Service -> Cloud SQL PostgreSQL:** Persists operational state and PHI [pgx driver over TLS]
- **Core Telehealth Service -> Video Consultation Service:** Manages video sessions [WebRTC / gRPC]

## Technology Stack
- **Go (Golang):** Chosen for low-latency performance and high concurrency in distributed GKE regions.
- **Istio Service Mesh:** Enforces zero-trust mTLS, SPIFFE/SPIRE workload identities, and traffic splitting.
- **GCP VPC Service Controls:** Physically enforces regional data residency between `europe-west3` and `us-central1`.
- **Cloud SQL PostgreSQL:** Provides regional, isolated relational storage with regional connection pooling.
- **Cloud KMS & Secret Manager:** Secures PHI with customer-managed encryption keys (CMEK) and runtime secret injection.

## Rationale
This architecture uses regional isolation and cryptographic audit controls to ensure strict GDPR and HIPAA compliance while maintaining low-latency orchestration. Go-based components and Istio service mesh policies provide the resilience required for unstable rural connections.