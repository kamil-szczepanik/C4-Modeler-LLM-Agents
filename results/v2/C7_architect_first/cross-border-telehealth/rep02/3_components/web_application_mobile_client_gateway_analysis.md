## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Enforces strict regional data residency and compliance via GCP multi-region deployment.

## Key Elements
- Patients, Licensed Clinicians, Local Pharmacists, Compliance Auditors, Platform Administrators
- Web Application & Mobile Client Gateway (React / React Native)
- Client Routing & Auth Interceptor (Envoy Proxy)
- Offline Resilience Cache (Redux Persist / SQLCipher)
- Session & WebSocket Multiplexer (Node.js / Socket.io)
- Consent Enforcement Interceptor (Node.js Middleware)
- API Gateway (Node.js / Go)
- AI Symptom Checker Service (Python / FastAPI, Vertex AI)
- WebRTC Video Session Orchestrator (WebRTC, STUN/TURN)
- Database and Storage (Google Cloud SQL PostgreSQL, Google Cloud Storage WORM)
- Service Mesh (Istio Service Mesh, Envoy proxy)

## Relationships
- Patients / Clinicians / Pharmacists / Auditors / Administrators -> Web Application & Mobile Client Gateway [HTTPS / JSON over REST and WebSockets]
- Client Routing & Auth Interceptor -> Consent Enforcement Interceptor [Internal HTTP/2]
- Consent Enforcement Interceptor -> API Gateway [gRPC over Istio service mesh mTLS]
- Session & WebSocket Multiplexer -> API Gateway [WebSockets]
- Web Application & Mobile Client Gateway -> API Gateway [HTTPS / JSON over REST and WebSockets]

## Technology Stack
- React / React Native: Cross-platform frontend supporting multilingual UI and accessibility.
- Envoy Proxy: Edge routing, TLS termination, WAF, rate limiting, and circuit breaking.
- SQLCipher: Client-side storage encryption for PHI protection on mobile devices.
- Node.js / Socket.io: Real-time event streaming and persistent connection multiplexing.
- Istio Service Mesh / Envoy: Mutual TLS (mTLS) zero-trust internal communication.
- Google Cloud Platform (GCP): Multi-region deployment in `europe-west3` and `us-central1` using GKE, Cloud SQL, and Cloud Load Balancing.

## Rationale
This architecture enforces GDPR and HIPAA data residency constraints by isolating EU and US traffic at the edge while utilizing zero-trust service mesh encryption internally. It guarantees high availability and rural accessibility through offline caching, circuit breaking, and resilient WebSocket multiplexing.