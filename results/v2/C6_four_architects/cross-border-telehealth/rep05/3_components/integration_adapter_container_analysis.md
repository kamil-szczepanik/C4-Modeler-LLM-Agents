## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and interoperability standards within GCP.

## Key Elements
- Integration Adapter Container
- Internal Ingress Router (Go)
- FHIR Translation Component (Node.js/TypeScript)
- EU National e-Prescription Adapter (Java/Spring Boot)
- AI Gateway Intermediary (Python/FastAPI)
- Adapter Security & Audit Proxy (Sidecar/Envoy)

## Relationships
- Backend Service & Consent & Policy Service -> Internal Ingress Router: gRPC over Istio mTLS
- Internal Ingress Router -> FHIR Translation Component / EU National e-Prescription Adapter: Internal gRPC
- FHIR Translation Component -> External HIEs: REST/FHIR over mTLS (us-central1)
- EU National e-Prescription Adapter -> External Pharmacy Networks: SOAP/REST over mTLS (europe-west3)
- Adapter Security & Audit Proxy -> External Systems: TLS 1.3, mTLS, and region-locked GCP egress

## Technology Stack
- Go: Used for the Internal Ingress Router to handle high-performance tenant-aware gRPC routing.
- Node.js/TypeScript: Powers the FHIR Translation Component for US HL7 FHIR standard transformations.
- Java/Spring Boot: Implements the EU National e-Prescription Adapter for regional compliance.
- Python/FastAPI: Standardizes payloads in the AI Gateway Intermediary for MDR traceability.
- Envoy Proxy: Acts as the Adapter Security & Audit Proxy for strict egress policy and TLS 1.3 enforcement.

## Rationale
This component architecture enforces strict regional data isolation between GCP regions (`europe-west3` and `us-central1`) to satisfy GDPR and HIPAA mandates. Centralized egress control via Envoy ensures complete auditability and compliance for cross-border medical data.