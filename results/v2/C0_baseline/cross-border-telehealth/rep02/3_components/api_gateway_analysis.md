## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring high availability for users with unstable internet connections.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web / Mobile Client (React / React Native)
- API Gateway (Envoy / Cloud Endpoints with WAF, Geo-Router, and xDS Client)
- Core Telehealth Service (Node.js / NestJS)
- AI Symptom Service (Python / FastAPI)
- Localization, Billing, and Control Plane Services
- Google Cloud SQL (PostgreSQL) and GCP Cloud Storage WORM buckets

## Relationships
- Web / Mobile Client -> API Gateway: Client requests and media streams [HTTPS (TLS 1.3) and WSS]
- API Gateway -> Core Telehealth Service: Internal backend requests [gRPC over mTLS, Regional VPC]
- API Gateway -> AI Symptom Service: AI symptom check requests with consent metadata [gRPC over mTLS]
- API Gateway (xDS Client) -> Control Plane: Dynamic routing updates [gRPC]

## Technology Stack
- GCP (regions: europe-west3, us-central1): Chosen for regional control and strict data residency compliance (R-05).
- Envoy / Cloud Endpoints: Selected as the API Gateway for edge routing, WAF integration, and rate limiting.
- Node.js / NestJS & Python / FastAPI: Utilized for scalable backend services and AI integration.
- gRPC over mTLS: Implemented for secure, high-performance internal service communication.

## Rationale
This architecture enforces region-specific data separation to comply with GDPR and HIPAA mandates while utilizing an Envoy-based API Gateway for robust edge routing. Additionally, it integrates adaptive rate-limiting and TURN/STUN relays to guarantee reliable service for rural users facing unstable internet connections.