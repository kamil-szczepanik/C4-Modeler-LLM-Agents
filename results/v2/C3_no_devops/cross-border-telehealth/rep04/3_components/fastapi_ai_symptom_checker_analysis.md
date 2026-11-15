## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regulatory compliance (GDPR, HIPAA, EU MDR) and regional data residency while supporting rural users with unstable internet connections.

## Key Elements
*   **API Router / Controller:** Handles incoming gRPC requests using protocol buffers.
*   **Consent & Region Enforcer Middleware:** Validates data residency headers and consent tokens.
*   **Inference Orchestrator:** Manages calls to the Third-Party AI Model Provider and validates response integrity.
*   **Audit Logger Component:** Asynchronously writes signed immutable audit trails to GCP Cloud Pub/Sub.
*   **Guardrail & Localization Interceptor:** Appends localized clinical disclaimers and urgency-based calls-to-action.

## Relationships
*   **Kong API Gateway/BFF -> FastAPI AI Symptom Checker:** Routes symptom check requests via gRPC over mTLS using Anthos Service Mesh.
*   **Inference Orchestrator -> Third-Party AI Model Provider:** Transmits sanitized payloads over TLS 1.3 with payload encryption.
*   **Audit Logger Component -> GCP Cloud Pub/Sub:** Publishes cryptographically signed audit logs asynchronously.

## Technology Stack
*   **Python 3.11+:** Core runtime language chosen for rapid development and AI ecosystem compatibility.
*   **FastAPI & Pydantic:** High-performance web framework and data validation for lightweight payload delivery.
*   **gRPC (`grpcio`) & Protocol Buffers:** Low-overhead binary serialization for optimized performance on low-bandwidth connections.
*   **GCP Cloud KMS & Cloud Pub/Sub:** Used for asymmetric key signing and secure, region-isolated audit logging.

## Rationale
This architecture guarantees low-latency payloads and non-blocking interceptors to maintain performance for rural patients on unstable connections. Furthermore, it embeds zero-trust controls, cryptographic audit logging, and localized guardrails to satisfy strict GDPR, HIPAA, and EU MDR mandates.