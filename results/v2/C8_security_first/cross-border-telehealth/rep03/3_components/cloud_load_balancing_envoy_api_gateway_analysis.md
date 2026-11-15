## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency, low-bandwidth optimization, and regulatory compliance.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web/Mobile Client Application (Flutter / React)
- GCP External HTTP(S) Load Balancer & GCP Cloud Armor Security Policy
- Envoy Edge Proxy (Envoy with Ext-Authz, Localization, and WASM/Lua filters)
- Core Telehealth & Consent Container (Go)
- AI Symptom Checker Container (Python / FastAPI)
- Prescription Integration Container (Go)
- Break-Glass Identity Provider (IdP) and Immutable Storage

## Relationships
- Web/Mobile Client Application -> GCP External HTTP(S) Load Balancer: Sends client requests with low-bandwidth adaptation [HTTPS / gRPC (<300 kbit/s)]
- GCP External HTTP(S) Load Balancer -> GCP Cloud Armor Security Policy: Evaluates security rules [HTTPS]
- GCP Cloud Armor Security Policy -> Envoy Edge Proxy: Forwards filtered traffic [HTTPS]
- Envoy Edge Proxy -> Core Telehealth & Consent Container: Routes API requests [gRPC over mTLS]
- Envoy Edge Proxy -> AI Symptom Checker Container: Routes traceable AI requests [gRPC over mTLS]

## Technology Stack
- GCP Cloud Load Balancing & Cloud Armor: Edge routing and DDoS mitigation for regional separation
- Envoy Proxy: Traffic shaping, WASM/Lua filtering, W3C trace injection, and TLS 1.3 termination
- SPIFFE/SPIRE & GCP Certificate Authority Service: Zero-trust workload identity and automated certificate rotation
- Go & Python (FastAPI): High-performance backend services for telehealth logic and AI processing
- OpenTelemetry: Region-isolated distributed tracing enforcing data residency constraints

## Rationale
Regional GCP deployments (`europe-west3` and `us-central1`) with edge Envoy gateways guarantee GDPR and HIPAA data residency compliance. Modular Envoy filters and gRPC over mTLS maintain strict security, zero-trust communication, and low-bandwidth resilience for rural users.