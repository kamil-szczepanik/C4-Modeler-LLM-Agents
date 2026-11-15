## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability for rural users across GCP regions.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Envoy and Google Cloud Load Balancing)
- AI Symptom Checker Service (Python / FastAPI container)
- Vertex AI Model Registry and Regional Endpoints
- Google Cloud Storage (WORM Object Lock Storage)

## Relationships
- Patients -> API Gateway: Client requests [HTTPS / WebRTC]
- API Gateway -> AI Symptom Checker Service: Internal routing [gRPC over mTLS]
- AI Symptom Checker Service -> Vertex AI: Regional inference [REST / gRPC over VPC Service Controls]
- AI Symptom Checker Service -> Google Cloud Storage: Audit logging [HTTPS / Cloud KMS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud utilizing `europe-west3` and `us-central1` regions
- FastAPI / Python: Container runtime for the AI Symptom Checker Service
- Google Cloud Vertex AI: Regional model hosting ensuring data locality
- Google Cloud Storage with Object Lock: WORM storage for immutable compliance logs
- Google Cloud KMS: Customer-managed encryption keys (CMEK) for region-specific data protection

## Rationale
Regional GCP deployment with CMEK and WORM storage satisfies strict GDPR and HIPAA data residency mandates. Decoupled Vertex AI endpoints with gRPC over mTLS ensure low-latency, secure AI inference and traceable EU MDR compliance.