## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, regulatory compliance, and resilience for unstable rural connections.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- API Gateway (Istio Service Mesh / Envoy)
- Regional GKE Clusters (Google Kubernetes Engine)
- WebRTC SFU (Mediasoup / coturn)
- AI Symptom Checker Container (Python / TensorFlow)
- Google Cloud WAF & Google Cloud Storage (WORM)

## Relationships
- Patients & Clinicians -> Google Cloud WAF: HTTP/HTTPS traffic [HTTPS/TLS 1.3]
- Google Cloud WAF -> API Gateway: Filtered incoming traffic [HTTPS/TLS 1.3]
- Patients & Clinicians -> WebRTC SFU: Direct media streaming [WebRTC via UDP/TCP]
- API Gateway -> Regional GKE Clusters: Microservices routing [Istio mTLS with SPIFFE IDs]
- API Gateway -> AI Symptom Checker: Symptom analysis requests [gRPC / HTTPS]

## Technology Stack
- Google Cloud Platform (GCP): Multi-region cloud provider for `europe-west3` and `us-central1` isolation.
- Envoy / Istio Service Mesh: Edge routing, rate-limiting, circuit breaking, and mTLS enforcement.
- Mediasoup / coturn: Dedicated media streaming containers to prevent gateway bottlenecks.
- OpenTelemetry & Prometheus: Distributed tracing and real-time latency monitoring.

## Rationale
Geo-distributed Envoy gateways enforce strict data residency at the network edge to satisfy GDPR and HIPAA requirements. Offloading media to Mediasoup and applying Envoy rate-limiting ensures high availability and resilience for rural users with unstable connections.