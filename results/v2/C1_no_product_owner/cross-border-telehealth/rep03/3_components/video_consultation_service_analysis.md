## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance via GCP deployment in `europe-west3` and `us-central1`.

## Key Elements
- **Patients and Clinicians**: End-users accessing the platform via mobile and web apps.
- **Web & Mobile Client Apps**: Flutter / React Native client interfaces.
- **API Gateway**: Google Cloud API Gateway / Envoy managing entry points.
- **Core Telehealth Service**: Go / gRPC & REST orchestrating workflows.
- **Video Consultation Service**: Mediasoup SFU on GCE hosting real-time adaptive WebRTC video streaming.
- **Signaling Component (Node.js/WebSocket)**: Manages peer connection negotiation and room states.
- **Media Routing Component (Mediasoup SFU/C++)**: Handles real-time packet routing, simulcast, and bitrate scaling.
- **Bandwidth Adaptation Component (Go)**: Dynamically downscales streams for degraded mode (<300 kbit/s).
- **Compliance Recording Component (C++/Python)**: Encrypts and streams session audit logs.
- **Telemetry Collector Component (Node.js)**: Gathers WebRTC stats and exposes Prometheus metrics.
- **AI Symptom Checker**: Python / FastAPI + PyTorch container.
- **Databases and Storage**: Cloud SQL PostgreSQL and region-locked Cloud Storage buckets.
- **Infrastructure**: Google Kubernetes Engine (GKE), Istio Service Mesh, and GCP Regional External HTTP(S) Load Balancer.

## Relationships
- Client Apps -> API Gateway [HTTPS/WSS]: Accesses platform services and real-time signaling.
- API Gateway -> Core Telehealth Service [gRPC/REST]: Routes functional requests.
- Core Telehealth Service -> Video Consultation Service [gRPC]: Initiates and manages video sessions.
- Signaling -> Media Routing [In-Process IPC]: Controls SFU worker threads.
- Bandwidth Adaptation -> Media Routing [gRPC]: Adjusts bitrates based on telemetry.
- Telemetry Collector -> Bandwidth Adaptation [In-Process IPC]: Feeds real-time network metrics.
- Media Routing -> Cloud Storage [HTTPS/SRTP]: Stores encrypted session artifacts regionally.

## Technology Stack
- **Compute & Orchestration**: Google Compute Engine (GCE) for Mediasoup SFU; Google Kubernetes Engine (GKE) for containerized microservices.
- **Networking**: WebRTC with DTLS-SRTP for encrypted media; WSS for WebSocket signaling; GCP Regional External HTTP(S) Load Balancer.
- **Languages & Frameworks**: Go (Core/Adaptation), Node.js (Signaling/Telemetry), C++/Python (Media routing/Recording), Python/FastAPI + PyTorch (AI).
- **Data & Compliance**: Cloud SQL PostgreSQL, Cloud Storage with CMEK via GCP Cloud KMS, and VPC Service Controls.

## Rationale
This architecture uses dedicated GCE instances with Mediasoup SFU to ensure raw UDP/WebRTC performance while deploying services across regionally isolated GCP regions (`europe-west3` and `us-central1`). Strict encryption, VPC Service Controls, and dedicated adaptation components simultaneously satisfy regional data residency mandates (GDPR/HIPAA) and low-bandwidth rural connectivity requirements.