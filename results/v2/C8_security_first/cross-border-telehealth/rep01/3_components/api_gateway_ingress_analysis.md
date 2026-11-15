## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Enforces strict regional data residency and compliance via GCP.]

## Key Elements
- Patients and Clinicians (End users)
- Compliance Officer (Auditor)
- API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer with Cloud Armor WAF)
- Video Consultation Service (Mediasoup WebRTC SFU)
- AI Symptom Checker Container (Python / FastAPI, PyTorch)
- E-Prescription Integration Container (Node.js, FHIR protocol adapters)
- Patient Consent & Profile Container (Go)
- Identity Providers (IdP)
- Google Cloud Memorystore (Redis)

## Relationships
- Patients & Clinicians -> API Gateway / Ingress: Accesses platform services [HTTPS / TLS 1.3, OAuth 2.0 / OIDC, FIDO2/WebAuthn]
- API Gateway / Ingress -> Video Consultation Service: Routes video traffic [gRPC over mTLS with SPIFFE IDs]
- API Gateway / Ingress -> AI Symptom Checker Container: Routes AI inference requests [gRPC over mTLS with SPIFFE IDs]
- API Gateway / Ingress -> E-Prescription Integration Container: Routes prescriptions [gRPC over mTLS with SPIFFE IDs]
- API Gateway / Ingress -> Patient Consent & Profile Container: Routes consent management [gRPC over mTLS with SPIFFE IDs]
- API Gateway / Ingress -> Identity Providers (IdP): Authenticates users [OAuth 2.0 / OIDC]
- API Gateway / Ingress -> Google Cloud Memorystore: Validates token blacklists [RESP over TLS]

## Technology Stack
- GCP (europe-west3, us-central1): Enforces physical data residency constraints
- Envoy / GCP HTTPS Load Balancer: Handles ingress routing, rate-limiting, and TLS termination
- Istio (gRPC xDS): Manages dynamic control plane configuration via GitOps
- Google Cloud Armor: Provides WAF and Anycast IP routing protection
- gRPC over mTLS with SPIFFE: Secures internal microservice communication

## Rationale
[Regional deployment across europe-west3 and us-central1 strictly enforces GDPR and HIPAA data residency requirements. Envoy-based edge controls, token revocation, and retry-aware rate limiting ensure low-latency availability for rural connections while maintaining clinical traceability.]