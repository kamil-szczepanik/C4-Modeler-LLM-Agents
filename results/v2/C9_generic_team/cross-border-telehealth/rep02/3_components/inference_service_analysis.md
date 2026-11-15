## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency and regulatory compliance under GDPR, HIPAA, and EU MDR.

## Key Elements
- **Patients & Licensed Clinicians:** End-users accessing care across the EU and US.
- **Inference Service:** Python and gRPC-based container executing the AI symptom checker.
- **AI Model Registry:** External storage for versioned, cryptographically verified model artifacts.
- **Middleware Audit Interceptor:** Component capturing inputs, model versions, and outputs for R-07 compliance.
- **Local Ephemeral Buffer / DLQ:** Local caching mechanism for audit payloads during telemetry outages.

## Relationships
- **Inference Service -> AI Model Registry:** Fetches versioned model artifacts [gRPC].
- **API Gateway / Workers -> Inference Service:** Invokes symptom checks and streams telemetry [gRPC, TLS].
- **Inference Service -> Telemetry/Audit Collector:** Dispatches immutable audit logs and traces [gRPC/HTTPS].

## Technology Stack
- **Python & gRPC:** Core technology stack for the Inference Service to ensure strong typing and high-performance serialization.
- **Protocol Buffers:** Utilized for strict schema validation and payload sanitization before inference execution.
- **Local Ephemeral Storage:** Used for local caching and DLQ fallback during audit collection outages.

## Rationale
This architecture ensures strict EU MDR traceability and accountability (R-07) through immutable audit logging and model version pinning. Furthermore, local fallback buffers and request sanitization protect system availability and data privacy under strict healthcare regulations.