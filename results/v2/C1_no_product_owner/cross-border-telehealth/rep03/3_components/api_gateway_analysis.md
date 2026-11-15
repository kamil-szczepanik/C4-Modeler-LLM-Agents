## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability for unstable connections.

## Key Elements
- Patients and Clinicians (End Users)
- Google Cloud API Gateway / Envoy (API Gateway Container)
- Routing & Regional Affinity Controller
- Authentication & Authorization Filter
- Resilience & Rate Limiting Module
- Payload Inspection & Schema Validator
- Core Telehealth Service, Video Consultation Service, AI Symptom Checker Container, and Integration Service (Microservices)
- Regional IdPs, EU National e-Prescription Gateways, and US Pharmacy Networks (External Systems)

## Relationships
- Web & Mobile Client Apps -> Routing & Regional Affinity Controller: Sends client requests and WebRTC signaling [HTTPS/WSS]
- Routing & Regional Affinity Controller -> Payload Inspection & Schema Validator: Passes ingress traffic for validation [Internal gRPC]
- Payload Inspection & Schema Validator -> Core Telehealth Service: Forwards sanitized requests via service mesh [gRPC over Istio mTLS]
- API Gateway -> External Systems: Connects to regional e-prescription gateways and pharmacy networks [HTTPS/REST]

## Technology Stack
- Google Cloud Platform (GCP in `europe-west3` and `us-central1`): Enforces strict geographical data residency.
- Envoy Proxy & Google Cloud API Gateway: Provides edge routing, localized multi-region deployment, and WAF protection.
- Google Kubernetes Engine (GKE) & Istio Service Mesh: Manages microservices with strict mTLS and SPIFFE ID validation.
- JWT with Token-Embedded Consent: Enables local cryptographic authorization without synchronous database lookups.
- Native Protobuf Schema Validation: Minimizes CPU overhead for low-bandwidth connections.

## Rationale
This architecture uses localized edge instances and token-embedded consent to enforce GDPR and HIPAA data residency while maintaining performance. Native Envoy schema validation and circuit breaking secure the platform and preserve availability for unstable rural connections.