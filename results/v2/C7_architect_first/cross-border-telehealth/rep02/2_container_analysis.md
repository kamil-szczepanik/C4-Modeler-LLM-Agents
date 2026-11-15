## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients, Licensed Clinicians, Local Pharmacists, Compliance Auditors, Platform Administrators
- React / React Native Web Application & Mobile Client Gateway
- Google Kubernetes Engine (GKE) running Node.js/Go API Gateway and Python/FastAPI AI Symptom Checker Service
- WebRTC Video Session Orchestrator with STUN/TURN edge servers
- Google Cloud SQL PostgreSQL and Google Cloud Storage (WORM with Object Lock)
- Istio Service Mesh with Envoy proxy
- National EU E-Prescription Gateways and US Pharmacy Systems

## Relationships
- Clients connect to Web Application via HTTPS / JSON over REST and WebSockets
- API Gateway communicates with core services via gRPC over mTLS (Istio)
- AI Symptom Checker invokes Vertex AI and writes immutable audit logs to Cloud Storage via WORM
- Interoperability adapters securely transmit e-prescriptions to National EU Gateways and US Pharmacy Systems

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance
- GKE & Istio: Orchestrates container workloads and enforces mTLS service mesh security
- Python / FastAPI & Vertex AI: Powers the AI symptom checker with model monitoring
- Google Cloud SQL & Cloud Storage: Enforces regional encryption via CMEK and WORM audit logging
- Terraform: Manages Infrastructure-as-Code and compliance configuration parity

## Rationale
Multi-region container deployment on GCP naturally satisfies strict GDPR and HIPAA data residency boundaries. Edge-optimized WebRTC and circuit breakers guarantee resilient telehealth delivery even across unstable rural network connections.