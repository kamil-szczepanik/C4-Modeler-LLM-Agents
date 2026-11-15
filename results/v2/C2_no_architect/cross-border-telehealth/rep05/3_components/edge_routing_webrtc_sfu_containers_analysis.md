## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency while ensuring high availability for rural users over unstable connections.

## Key Elements
- Multi-region Web/Mobile Clients
- Edge Routing & WebRTC SFU Containers (Envoy, Mediasoup/Jitsi)
- Google Kubernetes Engine (GKE) regional clusters (`europe-west3`, `us-central1`)
- API Gateway with Istio Service Mesh (mTLS)
- E-Prescription Routing Container (GCP Pub/Sub)
- AI Symptom Checker Container
- Consent Management Service

## Relationships
- Multi-region Web/Mobile Clients -> Edge Routing & WebRTC SFU Containers: Video streaming and signaling [WebRTC, DTLS-SRTP, TLS 1.3]
- Edge Routing & WebRTC SFU Containers -> API Gateway: Backend microservice requests [mTLS, gRPC/HTTPS]
- API Gateway -> E-Prescription Routing Container: Asynchronous prescription dispatch [GCP Pub/Sub]
- Clients -> Consent Management Service: Purpose-based consent validation [OAuth 2.0 / OIDC]

## Technology Stack
- Google Cloud Platform (GCP): Multi-region deployment (`europe-west3`, `us-central1`) ensuring data residency.
- Envoy & Mediasoup/Jitsi: Edge routing, geo-IP validation, adaptive bitrate control, and WebRTC SFU media forwarding.
- GKE Confidential Computing: Encrypted memory nodes preventing persistent media storage (GDPR/HIPAA compliance).
- Prometheus & Grafana: Real-time telemetry monitoring packet loss, jitter, and fallback durations without PII logging.
- OAuth 2.0 / OIDC: Token-based authentication and regional claims at the edge proxy.

## Rationale
Regional GKE clusters paired with geo-pinned edge routing guarantee that EU health data remains strictly in `europe-west3` and US data in `us-central1`. WebRTC SFU optimization with adaptive bitrate control and memory-encrypted nodes directly satisfies the requirement for rural accessibility and strict medical privacy compliance.