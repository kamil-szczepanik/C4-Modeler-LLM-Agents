## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and traceable medical AI inference.

## Key Elements
* API Router & Validation Component (FastAPI)
* Pseudonymization & Redaction Component
* Regional AI Gateway Client
* Circuit Breaker & Fallback Component
* Audit & Traceability Logger
* GCP Cloud SQL (PostgreSQL) and Cloud Storage with Cloud KMS

## Relationships
* API Router -> Pseudonymization Component: Passes raw payloads via in-memory Python calls
* Pseudonymization Component -> Regional AI Client: Passes sanitized payloads via in-memory Python calls
* Regional AI Client -> Circuit Breaker / Fallback: Executes inference via gRPC
* Audit & Traceability Logger -> Cloud SQL & Cloud Storage: Writes audit logs via TCP/mTLS with CMEK and WORM policies

## Technology Stack
* Python / FastAPI: Core framework for the AI Inference Wrapper Service due to asynchronous performance and ML ecosystem compatibility
* SQLAlchemy: ORM for secure database interactions over TCP/mTLS
* GCP Cloud KMS & Bucket Lock: Provides customer-managed encryption keys (CMEK) and immutable object storage for compliance

## Rationale
This component architecture isolates AI inference while enforcing regional data residency and strict pseudonymization to satisfy EU MDR and HIPAA mandates. Dedicated circuit-breaking and audit logging ensure high availability and complete traceability under strict latency and regulatory constraints.