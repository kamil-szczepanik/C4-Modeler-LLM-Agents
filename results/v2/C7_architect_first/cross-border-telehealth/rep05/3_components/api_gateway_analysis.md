## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and high availability for unstable rural connections.

## Key Elements
- Web & Mobile App (Flutter / TypeScript)
- API Gateway container (Google Cloud API Gateway) with internal components: Policy Enforcement Proxy (Envoy Proxy), Auth & Rate Limiter (Envoy Filter / Lua), Signaling Proxy (NGINX), and Protocol Translation Bridge
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript)
- Video Media Server (LiveKit / WebRTC)
- Cloud SQL (PostgreSQL) and Google Cloud Storage
- Google Cloud Pub/Sub

## Relationships
- Web & Mobile App -> API Gateway: Sends API requests and WebSocket messages [HTTPS / WSS]
- Policy Enforcement Proxy -> Core Services Container: Dispatches validated, consent-checked requests [gRPC / mTLS]
- Signaling Proxy -> Video Media Server: Relays real-time session metadata [WSS]
- Region Router -> Regional Gateways: Routes traffic to `europe-west3` and `us-central1` [Cloud Load Balancing]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency (R-05).
- Envoy Proxy & Envoy Filter / Lua: Powers the Policy Enforcement Proxy and Auth & Rate Limiter for JWT validation and routing.
- Spring Boot & FastAPI: Implements backend business logic and the AI symptom checker.
- LiveKit & WebRTC: Delivers scalable video consultations.
- PostgreSQL & Google Cloud Storage: Secures persistent health data per region.

## Rationale
Regional API gateways deployed in GCP paired with JWT-based policy enforcement guarantee GDPR and HIPAA compliance while maintaining data residency. Protocol translation and robust signaling proxies ensure continuous, degraded-mode availability for rural patients.