## Overview
The Core Telehealth Service is a high-performance Go-based container that manages consultations, prescriptions, and AI symptom checking. It enforces strict cross-border compliance, data residency, and traceability for patients in the EU and US.

## Key Elements
- **Consultation Manager**: Handles scheduling, session lifecycle, and real-time coordination.
- **Prescription Coordinator**: Manages e-prescription workflows routed to regional integration gateways.
- **Consent & Policy Engine**: Enforces GDPR/HIPAA data residency and verifies purpose-based patient consents.
- **Audit & Traceability Logger**: Captures cryptographically signed audit trails for AI recommendations and cross-region data access.
- **Symptom Checker Orchestrator**: Manages secure interactions with the AI Inference Wrapper and ensures model version logging.
- **LiveKit SFU Media Server**: Manages video streaming sessions.
- **US FHIR Adapter & EU E-Prescription Gateway**: Translates prescriptions to regional standards.
- **Cloud SQL PostgreSQL & Cloud Storage**: Persists domain data and audit logs.

## Relationships
- Consultation Manager -> LiveKit SFU Media Server: Coordinates video rooms via [gRPC]
- Prescription Coordinator -> US FHIR Adapter & EU E-Prescription Gateway: Dispatches prescriptions via [gRPC]
- Symptom Checker Orchestrator -> AI Inference Wrapper: Requests urgency recommendations via [gRPC/HTTPS]
- All Components -> Cloud SQL PostgreSQL & Cloud Storage: Persists transactional and audit data via [SQL/TCP]
- All Components -> Consent & Policy Engine: Intercepts data access for policy verification via [In-Memory Go Interfaces]

## Technology Stack
- **Go**: Chosen for high-throughput, low-latency business logic implementation.
- **gRPC**: Protocol for fast, strongly-typed internal component and gateway communication.
- **Cloud SQL PostgreSQL**: Relational database for transactional data and audit trails.
- **LiveKit (GKE)**: SFU media server for handling unstable internet connections and video streams.
- **Cloud Storage (GCP)**: Object storage for medical files and logs.

## Rationale
This component architecture uses Go for performance and domain-driven modularity to isolate compliance logic. The mandatory Consent Engine and Audit Logger ensure strict adherence to GDPR, HIPAA, and EU MDR traceability constraints across GCP regions.