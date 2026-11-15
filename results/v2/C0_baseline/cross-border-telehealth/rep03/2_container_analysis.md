## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance with GDPR and HIPAA mandates.

## Key Elements
- Patients and Licensed Clinicians (Users)
- Google Cloud API Gateway / Region Router
- React / Flutter Web and Mobile Apps
- Go / Spring Boot Core Telehealth Backends (EU/US)
- LiveKit / WebRTC SFU Video Media Servers (EU/US)
- Python / FastAPI + TensorFlow AI Symptom Checker Container
- Open Policy Agent (OPA) Consent Management Container
- E-Prescription Integration Service
- Google Cloud SQL & Cloud Storage
- External: National E-Prescription Gateways (EU), Surescripts/Pharmacy Networks (US), Regional IDPs, Stripe/Insurance APIs, Global TURN/STUN Edge Relays

## Relationships
- Patients/Clinicians interact with Web/Mobile Apps via HTTPS and WebSockets.
- API Gateway routes incoming traffic to regional VPCs using geo-routing.
- Services communicate internally via gRPC over Istio mTLS mesh.
- Core Backends query regional Cloud SQL databases and enforce rules via regional OPA containers.
- E-Prescription Service connects to national EU standards and US Surescripts networks via REST and HL7 FHIR.
- AI Symptom Checker logs inputs and model versions to regional Cloud Storage with CMEK.

## Technology Stack
- GCP (`europe-west3` and `us-central1`): Primary cloud provider and regions for strict data residency.
- GKE Autopilot & ArgoCD: Container orchestration and GitOps deployment.
- Go and Spring Boot: Core microservices for high-performance backend logic.
- React and Flutter: Frontend web and mobile application frameworks.
- LiveKit and WebRTC SFU: Video streaming supporting degraded-mode (<300 kbit/s) connections.
- Python, FastAPI, and TensorFlow: AI Symptom Checker implementation.
- Open Policy Agent (OPA): Real-time authorization and consent evaluation.
- Google Cloud KMS & Secret Manager: CMEK encryption and zero-trust secret injection.

## Rationale
Regional container isolation in GCP guarantees that EU patient data stays in `europe-west3` and US data stays in `us-central1`, satisfying GDPR and HIPAA constraints. Dedicated OPA authorization containers and immutable AI audit logging ensure verifiable compliance and traceability for cross-border medical workflows.