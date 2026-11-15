## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US while strictly enforcing regional data residency and compliance.]

## Key Elements
[
• Patients (EU/US) and Licensed Clinicians
• AI Inference Orchestrator (Python / FastAPI)
• API Handler Component, Consent Validator Component, Payload Sanitizer/Encryption Component, Inference Router Component, Audit Logging Component
• Regional Cloud Spanner and Regional BigQuery
• Consent Management Service and AI Symptom Checker Engine
]

## Relationships
[
• API Handler Component -> Consent Validator Component: Internal verification [In-memory / gRPC]
• AI Inference Orchestrator -> Consent Management Service: Verifies patient consent [gRPC over mTLS]
• Inference Router Component -> AI Symptom Checker Engine: Queries symptom check logic [HTTPS / gRPC with mTLS and certificate pinning]
• Audit Logging Component -> Regional Cloud Spanner: Synchronous transactional audit write [Google Cloud Client Libraries]
• Audit Logging Component -> Regional BigQuery: Asynchronous batch sync for analytics [Google Cloud Client Libraries]
]

## Technology Stack
[
• Python / FastAPI for the AI Inference Orchestrator backend
• Pydantic for strict payload validation across internal components
• Google Cloud Spanner for encrypted local transactional audit logs and data storage
• Google Cloud BigQuery for analytical data storage
• SPIFFE/SPIRE for mTLS and zero-trust identity authentication
• Prometheus and OpenTelemetry for metrics and tracing
]

## Rationale
[This architecture enforces regional compliance (GDPR/HIPAA/EU MDR) through strict data residency controls, synchronous audit logging, and payload minimization. It maintains high availability for rural, unstable internet connections via local consent caching, bulkhead patterns, and graceful degradation strategies.]