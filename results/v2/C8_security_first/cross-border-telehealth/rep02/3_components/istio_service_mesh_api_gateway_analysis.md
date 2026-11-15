## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a regionally isolated Istio service mesh to enforce strict data residency and regulatory compliance.

## Key Elements
- Patients & Licensed Clinicians
- External Identity Providers (IdP) & Local Pharmacies
- Istio Service Mesh & API Gateway (Istio, Envoy proxy)
- Regional Backend-for-Frontend (BFF) (Node.js, GraphQL)
- Mediasoup SFU (WebRTC media server)
- Consent Manager & AI Triage Service
- E-Prescription Adapter & Regional WORM Storage (GCP Storage)

## Relationships
- Patients & Clinicians -> Istio Ingress Gateway: [HTTPS (TLS 1.3), DTLS-SRTP for video]
- Istio Ingress Gateway -> Regional BFF: [gRPC over mTLS]
- Istio Ingress Gateway -> Mediasoup SFU: [UDP / DTLS-SRTP bypassing sidecars]
- Istio Ingress Gateway -> Consent Manager: [gRPC over mTLS via Ext_Authz]
- Istio Ingress Gateway -> External IdP: [OAuth 2.0 / OIDC]

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for regional data residency.
- Istio & Envoy: Manages multi-region traffic routing, mTLS, geo-restrictions, and rate limiting.
- Mediasoup SFU: Handles real-time video/audio streams with UDP/DTLS-SRTP.
- Node.js & GraphQL: Powers the regional Backend-for-Frontend (BFF) services.
- OpenTelemetry & Prometheus: Captures distributed traces and metrics for observability.

## Rationale
Regional Istio deployments ensure health data never crosses jurisdictional boundaries, satisfying GDPR and HIPAA requirements. Edge resilience features, traffic prioritization, and direct media routing maintain low-latency video consultations for rural patients on unstable connections.