## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, HIPAA/GDPR compliance, and high availability in rural environments.]

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Client Applications (Flutter / Web)
- API Gateway (Envoy / Google Cloud Endpoints)
- Core Telehealth Service (Go)
- AI Inference Service (Python / FastAPI)
- Interoperability Service (Java / Spring Boot)
- Containerized SFUs (mediasoup)
- Google Kubernetes Engine (GKE) in `europe-west3` and `us-central1`
- PostgreSQL Databases with CMEK and Dead-Letter Queue (DLQ)

## Relationships
- Client Applications -> API Gateway: Accesses platform features [HTTPS / gRPC]
- API Gateway -> AI Inference Service: Routes AI symptom check requests [gRPC over Istio mTLS mesh]
- AI Inference Service -> PostgreSQL Databases: Persists and retrieves encrypted audit/inference data [CMEK encrypted connection]
- GKE GPU Node Pools -> Cloud Storage Buckets: Pulls region-locked model weights [VPC Service Controls]

## Technology Stack
- Google Cloud Platform (GCP): Multi-region target cloud ensuring regional compliance
- Python / FastAPI: Core framework for the AI Inference Service
- ONNX Runtime / PyTorch: Localized model execution engines
- spaCy / Regex: Synchronous safety guardrail and keyword filtering
- GCP Confidential VMs (AMD SEV-SNP): Protects in-memory data during GPU inference

## Rationale
[This architecture enforces regional data segregation and end-to-end encryption to satisfy strict HIPAA, GDPR, and EU MDR compliance mandates. Decoupled async audit pipelines and CPU/GPU isolation ensure high availability, audit traceability, and resilience for rural users.]