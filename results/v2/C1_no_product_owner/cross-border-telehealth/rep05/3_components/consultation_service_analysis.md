## Overview
The Consultation Service component manages video consultations, WebRTC signaling, and session lifecycles for the Cross-Border Telehealth Platform. It enforces regional data compliance, graceful degradation on low-bandwidth connections, and secure patient consent validation across GCP regions.

## Key Elements
* Session Controller (Node.js, TypeScript, NestJS)
* Signaling Manager (Node.js)
* Data Residency Enforcer (Middleware)
* Degraded-Mode Monitor (Component)
* Consent Enforcer Interceptor (Component)
* Telemetry Adaptor (OpenTelemetry SDK)
* SFU Media Relay (Mediasoup, C++)
* Regional Message Broker (GCP Pub/Sub)

## Relationships
* API Gateway -> Session Controller: Routes incoming consultation requests [gRPC over mTLS]
* Session Controller -> Consent & Policy Engine: Validates regional data sharing consent [gRPC over mTLS]
* Session Controller -> Regional Message Broker: Publishes session state changes and metrics [gRPC over mTLS]
* Signaling Manager -> SFU Media Relay: Manages room allocations and orchestrates media streams [gRPC]
* Signaling Manager -> Client: Exchanges SDP offers/answers [WebSockets with short-lived JWTs]

## Technology Stack
* Node.js with TypeScript and NestJS: Powers the Consultation Service components for asynchronous handling.
* OpenTelemetry SDK: Enables distributed tracing and metric collection across microservices.
* Google Kubernetes Engine (GKE): Orchestrates containerized deployments in `europe-west3` and `us-central1` with network policies.
* WebRTC with DTLS-SRTP: Secures end-to-end video and audio media transmission.

## Rationale
This architecture uses Node.js and containerized GKE deployments to handle real-time WebRTC signaling while meeting stringent EU and US data residency rules. Integrated telemetry, strict security controls, and dynamic bitrate monitoring ensure low-bandwidth resilience and regulatory compliance.