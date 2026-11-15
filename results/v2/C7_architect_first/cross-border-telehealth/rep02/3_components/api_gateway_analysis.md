## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a localized API Gateway to enforce regional data residency and compliance.

## Key Elements
- Patients, Licensed Clinicians, Local Pharmacists, Compliance Auditors, Platform Administrators
- Web Application & Mobile Client Gateway (React / React Native)
- API Gateway Internal Components: Routing & Regional Affinity Router, Authentication & Authorization Filter, Rate Limiting & Circuit Breaker, Interoperability Protocol Adapter (Go)
- Downstream Containers: AI Symptom Checker Service (Python / FastAPI, Vertex AI), WebRTC Video Session Orchestrator, Google Cloud SQL PostgreSQL, Google Cloud Storage WORM
- External Systems: National EU E-Prescription Gateways, US Pharmacy Systems, WebRTC Video Infrastructure

## Relationships
- Web Application & Mobile Client Gateway -> API Gateway: Client requests [HTTPS / JSON over REST and WebSockets]
- Routing & Regional Affinity Router -> Downstream Services: Internal communication [gRPC over mTLS via Istio Service Mesh]
- Interoperability Protocol Adapter -> External Gateways: E-prescription transmission [mTLS and regional APIs / HTTPS]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider utilizing `europe-west3` and `us-central1` for strict data residency.
- Go: Chosen for building the high-performance API Gateway components.
- Istio Service Mesh & Envoy: Provides internal service-to-service security via mTLS and traffic shaping.
- Google Kubernetes Engine (GKE): Hosts containerized microservices with horizontal pod autoscaling.
- Google Secret Manager: Manages external API keys and mutual TLS certificates securely at runtime.

## Rationale
The decentralized, regional API Gateway architecture ensures strict compliance with EU GDPR and US HIPAA by enforcing data residency per region. Istio-enforced mTLS, granular consent scopes, and robust protocol adapters guarantee secure interoperability and auditability across international healthcare boundaries.