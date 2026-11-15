## Overview
Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Ensures GDPR/HIPAA compliance, strict data residency, and reliable access for rural patients.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- API Gateway / Region Router (Cloud Endpoints, Envoy)
- Core Telehealth, AI Gateway, Interoperability, Audit & Compliance Services (GKE, Node.js/Go/Python)
- WebRTC SFU Media Server (LiveKit, Janus)
- Data Layer (Cloud SQL PostgreSQL, Firestore, Cloud Storage)
- Regional Identity Providers & External Pharmacies

## Relationships
- Patients/Clinicians -> API Gateway: Client requests [HTTPS/WSS/QUIC over Anycast]
- API Gateway -> Core/AI/Interoperability/Audit Services: Internal routing [gRPC over VPC]
- API Gateway -> Identity Providers: Token validation [HTTPS]
- Media Server -> Patients: Video streaming [WebRTC]

## Technology Stack
- GCP (europe-west3, us-central1): Cloud provider meeting regional data residency constraints.
- Envoy Proxy & Cloud Endpoints: Edge routing, TLS termination, and Anycast support.
- HTTP/3 (QUIC) & WSS: Optimizes connectivity for unstable rural connections.
- GKE & Python/Go/Node.js: Containerized microservices architecture.
- OpenTelemetry & ArgoCD: Distributed tracing and GitOps infrastructure management.

## Rationale
Anycast routing and HTTP/3 edge termination guarantee low latency and resilience for rural users. Envoy-based geo-fencing and context injection enforce strict data residency and compliance without modifying core microservices.