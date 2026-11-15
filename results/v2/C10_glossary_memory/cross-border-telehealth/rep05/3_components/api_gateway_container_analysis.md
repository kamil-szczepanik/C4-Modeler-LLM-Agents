## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US while enforcing strict data residency and regulatory compliance. The architecture utilizes GCP to isolate regional workloads in `europe-west3` and `us-central1`.

## Key Elements
- Patients and Licensed Clinicians (Persons)
- Web Application Container (React / Next.js)
- API Gateway Container (Envoy / GCP API Gateway) with internal components: Rate Limiting Component, Geo-Router Component, Auth & Token Introspection Component, Upstream Proxy Component
- Core Services Container (Go / Node.js microservices)
- AI Symptom Checker Container (Python / FastAPI + Vertex AI)
- Media Relay Container (Janus / WebRTC SFU)
- E-Prescription Integration Container (Java / Spring Boot)
- Databases (GCP Cloud SQL for PostgreSQL)
- External Systems: EU National E-Prescription Gateways, US Pharmacy Networks (Surescripts), Identity Providers (eIDAS / OAuth2/OIDC), Regional Payment & Insurance Gateways

## Relationships
- Patients -> Web Application Container [HTTPS]
- Web Application Container -> API Gateway Container [HTTPS / REST & GraphQL]
- API Gateway Container -> Identity Providers (eIDAS / OAuth2/OIDC) [HTTPS / OIDC]
- API Gateway Container -> Core Services Container [gRPC over mTLS with regional awareness]
- API Gateway Container -> AI Symptom Checker Container [gRPC over mTLS]
- Patients / Licensed Clinicians -> Media Relay Container [WebRTC / DTLS-SRTP, UDP]
- Core Services Container -> Databases [TCP / SSL]
- E-Prescription Integration Container -> EU National E-Prescription Gateways & US Pharmacy Networks [HTTPS / mTLS / HL7 FHIR]

## Technology Stack
- GCP Global External HTTPS Load Balancer: Provides low-latency anycast entry points.
- Envoy Proxy: Powers the API Gateway Container with WASM/Lua filters, rate limiting, and outlier detection.
- gRPC over mTLS: Ensures secure, high-performance inter-container communication.
- GCP Cloud SQL for PostgreSQL: Secured via CMEK for relational data storage with regional isolation.
- WebRTC (Janus SFU): Enables real-time video consultations supporting degraded network modes.

## Rationale
This architecture guarantees strict regional data residency (GDPR and HIPAA compliance) by routing traffic at the API gateway edge. It also ensures high availability, traceability for AI medical recommendations, and resilience for users with unstable internet connections.