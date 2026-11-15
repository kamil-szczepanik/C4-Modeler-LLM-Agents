## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and resilience for unstable rural internet connections.

## Key Elements
- Patients & Clinicians (Users)
- Web/Mobile Frontend App (Flutter/React)
- Regional Media Proxy (Envoy)
- Signaling & Room Manager (Node.js/TypeScript)
- Media Router Node (Mediasoup Worker in C++/Node.js)
- Bandwidth Adaptation Controller (C++)
- Core Telehealth Service (Go/Spring Boot)
- AI Inference Service (Python/FastAPI)
- Regional Data Stores (GCP Cloud SQL/Spanner)

## Relationships
- Web/Mobile Frontend App -> Regional Media Proxy: Transmits media via WebRTC (SRTP/UDP)
- Regional Media Proxy -> Signaling & Room Manager: Manages signaling via gRPC
- Signaling & Room Manager -> Media Router Node: Controls media tracks via IPC (Local Pipe)
- Media Router Node -> Bandwidth Adaptation Controller: Feeds telemetry via Internal Function Call
- Core Telehealth Service -> Signaling & Room Manager: Establishes sessions via gRPC

## Technology Stack
- Mediasoup (C++/Node.js): Powers selective forwarding and simulcast stream adaptation
- Envoy: Enforces data residency boundaries within GCP
- GCP (europe-west3, us-central1): Provides regional cloud infrastructure
- WebRTC (SRTP/UDP): Enables low-latency video and audio transmission

## Rationale
This architecture isolates media traffic regionally via Envoy proxies to satisfy GDPR and HIPAA data residency constraints. Decomposing the video service with Mediasoup and a dedicated Bandwidth Adaptation Controller guarantees resilient, degraded-mode consultations for unstable rural connections.