## Overview
• Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
• Enforces strict regional data residency, privacy compliance, and EU MDR traceability using GCP multi-region infrastructure.

## Key Elements
• Patients and Licensed Clinicians (End Users)
• Local Pharmacy Networks and National Health Authorities (External Systems)
• Web / Mobile Clients (Multi-region Clients)
• WebRTC SFU / TLS 1.3 (Edge Routing & Video Containers)
• Regional Istio Ingress Gateways in `europe-west3` and `us-central1` (API Gateway)
• E-Prescription Routing Container (GCP Pub/Sub & Cryptographic Digital Signatures)
• AI Symptom Checker Container (AI/ML Runtime)
• Consent Management Service (OAuth 2.0 / OIDC)

## Relationships
• Web / Mobile Clients -> Regional Istio Ingress Gateways: HTTPS, WRTC/TLS 1.3
• Regional Istio Ingress Gateways -> Consent Management Service: OAuth 2.0 / OIDC
• Regional Istio Ingress Gateways -> AI Symptom Checker Container: mTLS with model version headers and request signing
• Regional Istio Ingress Gateways -> E-Prescription Routing Container: mTLS via GCP Pub/Sub

## Technology Stack
• Cloud Provider: Google Cloud Platform (GCP) across `europe-west3` (EU) and `us-central1` (US) for regional data isolation.
• Service Mesh & API Gateway: Istio Ingress with SPIFFE/SPIRE for mTLS, geo-aware routing, circuit breaking, and canary deployments.
• Security & Identity: OAuth 2.0 / OIDC for consent management; WAF and token-bucket rate limiting for edge protection.
• Observability & Analytics: OpenTelemetry for distributed tracing and eBPF-based telemetry for privacy-safe metering.

## Rationale
• Regional Istio gateways enforce strict data residency boundaries, ensuring EU health data stays in `europe-west3` and US data in `us-central1` per GDPR and HIPAA.
• Gateway-level rate limiting, adaptive timeouts, and OpenTelemetry logging guarantee high availability for rural connections and full audit traceability for EU MDR compliance.