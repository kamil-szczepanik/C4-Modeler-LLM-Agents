## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and robust performance for unstable network connections.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- API Gateway & Routing Layer (Google Cloud Load Balancing, Apigee)
- Core Telehealth Service and Integration Service (Go / Camel-K on GKE)
- Video Media Server (WebRTC SFU on GKE) with internal components: SFU Core Router, ABR Controller, TURN/STUN Relay Module, Media Recording & Compliance Logger
- AI Inference Wrapper (Python on Vertex AI) and AI Model Registry
- Audit & Traceability Ledger (Cloud Pub/Sub, BigQuery)
- Datastores (Cloud SQL PostgreSQL, Cloud Storage)
- External Systems: Identity & Consent Provider, EU National E-Prescription Gateways, US Surescripts/Pharmacy Clearinghouses

## Relationships
- Patients & Clinicians -> Video Media Server: Streams video consultations [WebRTC via UDP/TCP]
- SFU Core Router -> APIs & Signaling Service: Session setup [gRPC / Protobuf]
- SFU Core Router -> Media Recording & Compliance Logger: Forwards RTP streams [Internal gRPC/RTP]
- Media Recording & Compliance Logger -> Datastores (Cloud SQL PostgreSQL / Cloud Storage): Persists encrypted media chunks [HTTPS / GCP IAM]
- Integration Service -> EU National E-Prescription Gateways / US Surescripts: Sends e-prescriptions [REST / HL7 FHIR / National Standards]

## Technology Stack
- Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for localized data residency
- Google Kubernetes Engine (GKE) running Go and Python services for core container orchestration
- Pion WebRTC, Coturn, and GStreamer for media handling and NAT traversal
- Vertex AI for the traceable AI symptom checker
- Cloud SQL PostgreSQL and Cloud Storage for regionalized persistence
- BigQuery and Cloud Pub/Sub for audit logging and compliance tracking

## Rationale
This GCP-native architecture strictly enforces regional data boundaries to satisfy GDPR and HIPAA mandates. Decomposing the Video Media Server with specialized ABR and TURN components ensures resilient, low-bandwidth video consultations for rural patients.