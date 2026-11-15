## Overview
The AI Orchestration Service securely processes patient symptom checker requests for a cross-border telehealth platform operating in the EU and US. It enforces regulatory compliance, regional data residency, and high availability while delivering traceable AI-driven care urgency recommendations.

## Key Elements
- **API Router & Validator:** FastAPI and Pydantic component validating payloads and enforcing JWT consent scopes.
- **Prompt & Context Assembler:** Prepares localized prompts and strips PII/PHI.
- **Inference Client:** Interacts with GCP Vertex AI via gRPC/mTLS.
- **Audit Logger:** Captures immutable inputs, model versions, and outputs.
- **Resilience Handler:** Implements circuit breaking and fallback urgency recommendations.
- **Regional WORM Storage:** GCP Cloud Storage secured via Cloud KMS and object retention policies.

## Relationships
- **Regional API Gateway / BFF -> API Router & Validator:** Forwards requests via gRPC, mTLS, and Istio Service Mesh.
- **Inference Client -> Vertex AI:** Executes remote model calls via gRPC/HTTPS within VPC Service Controls (`europe-west3`, `us-central1`).
- **Audit Logger -> Regional WORM Storage:** Asynchronously flushes immutable logs via HTTPS using Cloud KMS.

## Technology Stack
- **Python / FastAPI:** Chosen for asynchronous request handling and fast ML ecosystem integration.
- **GCP Cloud Run:** Deployed with `min-instances > 0` to eliminate cold starts.
- **GCP Vertex AI:** Managed machine learning backend for symptom inference.
- **GCP Secret Manager:** Dynamic retrieval of credentials and keys without hardcoding.
- **OpenTelemetry:** Distributed tracing across the Istio service mesh and FastAPI.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data processing and stripping patient identifiers before third-party AI invocation. The inclusion of automated fallback mechanisms, bounded async logging, and immutable WORM storage satisfies medical device accountability rules while guaranteeing high availability in low-bandwidth conditions.