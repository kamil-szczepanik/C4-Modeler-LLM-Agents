## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and resilience over unstable connections.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Google Cloud Load Balancing (GCLB) & Apigee (API Gateway & Routing Layer)
- Geo-Routing Policy Engine & WebRTC Signaling Router
- JWT Validation & Consent Enforcement Filter
- Core Telehealth Service, Video Media Server, AI Inference Wrapper, Integration Service, and Audit Ledger (GKE containers)
- External Systems: Identity & Consent Provider, EU E-Prescription Gateways, US Surescripts, AI Model Registry

## Relationships
- Patients & Clinicians -> GCLB / Apigee: Interacts via HTTPS and WSS [HTTPS / WSS]
- GCLB -> Regional GKE Clusters (`europe-west3`, `us-central1`): Routes regional traffic [gRPC / HTTP / mTLS]
- WebRTC Signaling Router -> Video Media Server: Routes SDP offers [TCP / WebRTC]
- Apigee Filter -> Identity & Consent Provider: Validates tokens and verifies consent [HTTPS / REST over OAuth2/OIDC]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency (R-05)
- Google Cloud Load Balancing & Apigee: Handles regional geo-routing, TLS termination, and policy enforcement
- Envoy: Acts as the WebRTC Signaling Router for real-time session negotiation
- Go and Python on Google Kubernetes Engine (GKE): Powers core microservices and Vertex AI integration
- PostgreSQL (Cloud SQL): Stores regional relational and clinical data

## Rationale
Regional GCLB and Apigee deployments guarantee that EU health data never leaves `europe-west3` and US data stays in `us-central1`, satisfying GDPR and HIPAA constraints. Edge routing and dedicated signaling isolation maintain service availability for low-bandwidth users while strictly enforcing consent and traceability.