## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and regulatory compliance.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Regional API Gateway / BFF (Node.js/GraphQL)
- Consent & Policy Engine Container (.NET)
- Video Session Service (Go)
- AI Orchestration Service (Python/FastAPI)
- FHIR & Prescription Integration Service (.NET)
- GCP Regional Infrastructure (`europe-west3`, `us-central1`)

## Relationships
- Client Apps to Regional API Gateways via HTTPS / GraphQL
- API Gateways to Regional Services via gRPC over mTLS (Istio Service Mesh)
- AI Orchestration Service to Vertex AI via HTTPS / gRPC with VPC Service Controls
- Services to Regional WORM Storage via TLS 1.3 / Cloud KMS

## Technology Stack
- GCP GKE & Vertex AI: Scalable container orchestration and AI model hosting with regional isolation
- Istio Service Mesh: Enforces mTLS, circuit breaking, and service-to-service security
- .NET, Go, Node.js, Python: Microservice runtimes optimized for specific domain tasks
- Cloud KMS & Secret Manager: Regional key segregation and dynamic credential mounting

## Rationale
Independent regional GKE clusters and WORM storage guarantee GDPR and HIPAA compliance while maintaining data residency. gRPC over mTLS and Istio ensure low-latency, secure communication across distributed regional containers.