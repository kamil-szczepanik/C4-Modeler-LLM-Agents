## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and compliance using GCP infrastructure.

## Key Elements
- Patients & Clinicians (Users)
- External Pharmacies & Identity Providers (External Systems)
- Web & Mobile Frontend Applications (Flutter / React)
- API Gateway (Envoy / Google Cloud API Gateway)
- Consultation Service (Go, WebRTC SFU)
- AI Symptom Checker Service (Python / FastAPI)
- E-Prescription & Interoperability Service (Node.js / Java)
- Data Storage Layer (Cloud SQL PostgreSQL + Cloud Storage)
- GCP Global HTTP(S) Load Balancer & Cloud Armor

## Relationships
- Web & Mobile Frontend -> GCP Global Load Balancer: Ingress traffic [HTTPS/REST, WSS]
- GCP Global Load Balancer -> API Gateway: Regional ingress traffic [HTTPS]
- API Gateway -> Consultation Service: Routes consultation requests [gRPC over mTLS]
- API Gateway -> AI Symptom Checker Service: Routes symptom checking requests with W3C Trace Context [gRPC over mTLS]
- API Gateway -> E-Prescription & Interoperability Service: Routes e-prescription requests [gRPC over mTLS]
- Auth Component -> External Identity Providers: Token validation [OIDC/JWKS over HTTPS]

## Technology Stack
- **Cloud Provider:** GCP (regions: europe-west3, us-central1) for strict data residency compliance (GDPR/HIPAA).
- **API Gateway:** Envoy managed via Google Cloud API Gateway for edge routing, rate limiting, and TLS 1.3 termination.
- **Load Balancing:** GCP Global HTTP(S) Load Balancer with Cloud Armor and Regional NEGs to prevent cross-border data leaks.
- **Communication Protocols:** gRPC over mTLS for secure internal service communication; WSS for client signaling.
- **Observability:** Google Cloud Managed Service for Prometheus and regional Cloud Logging buckets for PII-redacted audit trails.

## Rationale
The multi-region GCP deployment guarantees that EU patient data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA mandates. Offloading heavy media tunneling to the Consultation Service while using Envoy for edge routing and load shedding ensures system availability and low latency for rural users.