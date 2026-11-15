## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability for rural users.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Patient Portal (React/Flutter SPA)
- API Gateway / Region Router (Cloud Endpoints/Envoy)
- Core Telehealth Service, AI Gateway, Interoperability Adapter, and Audit & Compliance Reporting Service (GKE microservices)
- WebRTC SFU Media Server (LiveKit/Janus)
- Data Layer (Cloud SQL PostgreSQL, Firestore, Cloud Storage)
- External Systems: AI Symptom Checker Engine, EU National E-Prescription Gateways, US Pharmacy Networks, Identity Providers

## Relationships
- Patients/Clinicians interact with the Patient Portal via HTTPS and WSS
- Patient Portal communicates with the API Gateway via HTTPS/WSS
- Regional microservices communicate internally via gRPC over internal VPC networks
- Interoperability Adapter integrates with external EU e-prescription gateways and US pharmacy networks via mTLS
- AI Gateway connects to the external AI Symptom Checker Engine via mTLS

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP regions `europe-west3` and `us-central1`) for regional data isolation
- **Orchestration**: Google Kubernetes Engine (GKE) with Istio service mesh for microservices and circuit breaking
- **Backend Languages**: Node.js, Go, and Python (FastAPI) for high-performance service execution
- **Frontend**: React and Flutter with local IndexedDB caching for offline resilience
- **Media**: WebRTC SFU (LiveKit/Janus) with dynamic bitrate scaling for unstable connections
- **Databases**: Cloud SQL (PostgreSQL) for transactional data and Firestore for state caching

## Rationale
Isolated regional deployments in `europe-west3` and `us-central1` strictly satisfy GDPR, HIPAA, and data residency constraints. Containerized edge caching, adaptive WebRTC streaming, and dedicated interoperability adapters ensure low-bandwidth resilience and seamless cross-border medical integration.