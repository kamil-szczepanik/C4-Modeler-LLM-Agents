## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, privacy, and traceability compliance via GCP.

## Key Elements
- Patients, Licensed Clinicians, Local Pharmacists, Compliance Auditors, Platform Administrators
- National EU E-Prescription Gateways, US Pharmacy Systems, WebRTC Video Infrastructure
- React / React Native (Web Application & Mobile Client Gateway)
- Node.js / Go (API Gateway)
- Python / FastAPI, Vertex AI (AI Symptom Checker Service)
- WebRTC, STUN/TURN (WebRTC Video Session Orchestrator)
- Google Cloud SQL PostgreSQL, Google Cloud Storage WORM (Database and Storage)
- Istio Service Mesh, Envoy proxy (Service Mesh)

## Relationships
- Patients and clinicians interact with the Web Application & Mobile Client Gateway via HTTPS/WSS.
- Client Gateway communicates with the API Gateway via REST/gRPC.
- API Gateway routes internal traffic through the Istio Service Mesh using mTLS (gRPC/HTTP2).
- Data Plane Proxy queries the Consent Management Service via gRPC using the ExtAuthz filter.
- Control Plane pushes routing and security policies to the Data Plane Proxy via gRPC.

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Core cloud infrastructure ensuring regional isolation.
- Istio Service Mesh & Envoy proxy: Enforces strict mTLS and routing policies.
- React & React Native: Cross-platform client delivery for web and mobile.
- Python / FastAPI & Vertex AI: Powers traceable AI symptom recommendations.
- OpenTelemetry & Prometheus: Captures audit logs, metrics, and model versions.

## Rationale
This architecture guarantees strict regional isolation and regulatory compliance with GDPR and HIPAA mandates. The Istio service mesh enforces security and consent-driven access control without compromising availability in low-bandwidth environments.