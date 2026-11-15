## Overview
The Consultation Service is a Go-based microservice managing real-time video consultations and WebRTC signaling for the Cross-Border Telehealth Platform. It ensures secure, low-latency communication while strictly enforcing regional data residency across the EU and US.

## Key Elements
- **Signaling Manager (Go)**: Handles WebSocket connections and WebRTC signaling exchange.
- **Session Controller (Go)**: Manages consultation lifecycle states and cryptographically signed JWT authorization tokens.
- **Media Relay Proxy (Go/C++ binding)**: SFU-based media router featuring a Degraded Mode Fallback Controller for low-bandwidth environments (<300 kbit/s).
- **Audit Logger Interceptor & Event Publisher (Go)**: Captures sanitized lifecycle events and streams them asynchronously.
- **Infrastructure**: GCP (`europe-west3` and `us-central1`), Kubernetes, Istio Service Mesh, Google Memorystore (Redis), Google Cloud SQL, and GCS.

## Relationships
- **API Gateway/BFF -> Session Controller**: Internal routing [gRPC over TLS via Istio mTLS]
- **Signaling Manager -> Google Memorystore (Redis)**: Real-time peer connection states [TCP]
- **Media Relay Proxy -> Clients**: WebRTC media streams [DTLS-SRTP over UDP]
- **Media Relay Proxy -> Cloud Storage (GCS)**: Session recording chunks [HTTPS]
- **Event Publisher -> Consent & Audit Service**: Asynchronous telemetry [gRPC with region-bound topics]

## Technology Stack
- **Go**: Chosen for high concurrency, low memory footprint, and efficient handling of real-time video streaming workloads.
- **WebRTC (DTLS-SRTP / SFU)**: Provides end-to-end encrypted media transport and Selective Forwarding Unit routing for bandwidth adaptation.
- **Google Memorystore (Redis) & Cloud SQL**: Delivers regionalized state management and data persistence complying with GDPR and HIPAA.
- **Istio Service Mesh**: Secures internal service-to-service communication via mTLS.

## Rationale
This architecture ensures high availability and low-latency video streaming in unstable rural network conditions via dynamic audio-fallback mechanisms. Strict regional isolation and tokenized authorization guarantee compliance with GDPR and HIPAA data residency mandates.