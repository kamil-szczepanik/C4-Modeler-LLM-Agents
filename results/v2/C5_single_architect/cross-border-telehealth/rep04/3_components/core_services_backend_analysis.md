## Overview
The Core Services Backend is a Go-based microservice responsible for orchestrating consultations, prescriptions, and audit logs while enforcing regional data residency and consent policies. It processes healthcare operations securely for patients and clinicians across EU and US deployments.

## Key Elements
- Patient & Clinician Management Component (Go, Gin/Fiber)
- Consultation Coordinator Component (Go)
- Prescription Management Component (Go)
- Audit & Traceability Component (Go)
- Region-Aware Data Router Component (Go)
- Cloud SQL PostgreSQL (GCP Database)
- Interoperability Adapter (Node.js/TypeScript)

## Relationships
- Consultation Coordinator -> Cloud SQL PostgreSQL: Persists booking states [TCP/SQL]
- Prescription Management -> Interoperability Adapter: Dispatches prescription payloads [gRPC]
- Audit & Traceability -> Cloud SQL PostgreSQL: Writes tamper-evident audit trails [TCP/SQL]
- Patient & Clinician Management, Consultation Coordinator, Prescription Management -> Region-Aware Data Router: Delegates persistence operations [In-process Go interface]
- Region-Aware Data Router -> Cloud SQL PostgreSQL: Executes region-isolated transactional queries [TCP/SQL]

## Technology Stack
- Go: Chosen for optimal concurrency, performance, and fast startup times
- Gin/Fiber: High-performance HTTP micro-frameworks for routing and profile management
- Cloud SQL PostgreSQL: Relational database deployed regionally in `europe-west3` and `us-central1` for data residency compliance
- gRPC: Efficient inter-service communication protocol for prescription routing
- TCP/SQL: Standard database connection protocol for transactional data persistence

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by routing queries regionally and filtering data based on patient consent. The modular Go-based component structure enables high availability and precise audit logging for medical traceability.