## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and traceability under EU MDR.

## Key Elements
- **Patients (EU/US) & Licensed Clinicians:** Primary end-users accessing telehealth services.
- **Compliance Auditors / Regional Regulators:** External entities verifying EU MDR and HIPAA compliance.
- **API Gateway (Cloud Endpoints / Envoy):** Manages ingress traffic and routing.
- **Web & Mobile Apps (React / Flutter):** Client interfaces for patients and clinicians.
- **AI Inference & Audit Service (Python / FastAPI):** Container managing symptom checking, traceability, and secure logging.
- **Inference Orchestrator:** FastAPI component handling prompt construction, regional routing, and fallbacks.
- **Model Version & Metadata Manager:** Component tracking model identifiers, weight hashes, and prompts.
- **Audit Log Formatter & Writer:** Component generating cryptographically signed audit payloads.
- **Regional Local Vault / Buffer (SQLite / Cloud SQL):** Local storage for regional data residency.
- **Circuit Breaker & Fallback Policy Engine:** Component managing latency thresholds and deterministic clinical fallbacks.
- **External AI Inference Provider / LLM API:** External service providing AI symptom analysis.
- **Prescription Integration Service (Node.js):** Handles e-prescriptions.

## Relationships
- Web & Mobile Apps -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> Core Telehealth Service & AI Inference & Audit Service: Internal routing [gRPC / HTTPS]
- Inference Orchestrator -> External AI Inference Provider / LLM API: Request AI symptom analysis [HTTPS REST with TLS 1.3/mTLS]
- Audit Log Formatter & Writer -> Regional Local Vault / Buffer: Persist signed logs [In-process / SQL]

## Technology Stack
- **Google Cloud Platform (GCP):** Target cloud provider utilizing `europe-west3` and `us-central1` for regional data residency.
- **Python / FastAPI:** Core language and framework for the AI Inference & Audit Service.
- **GCP Cloud KMS:** Provides cryptographic signing keys and Customer-Managed Encryption Keys (CMEK).
- **GCP Secret Manager:** Injects runtime API keys with regional blast radius containment.
- **SQLite / Cloud SQL:** Used for Regional Local Vault / Buffer persistence.

## Rationale
This architecture ensures strict compliance with GDPR and HIPAA by enforcing regional data isolation in `europe-west3` and `us-central1`. Cryptographically signed audit logs and circuit-breaker fallback policies satisfy EU MDR traceability and rural availability requirements.