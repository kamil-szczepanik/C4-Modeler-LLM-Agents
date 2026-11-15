## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and low-bandwidth resilience on GCP.

## Key Elements
- Patients and Clinicians (Users)
- GCP Global HTTPS Load Balancer with Geo-routing
- Envoy API Gateway (Google Cloud Armor)
- Backend Service & Consent & Policy Service (GKE, Open Policy Agent)
- AI Symptom Checker Service (FastAPI, GKE)
- SFU Media Relay (LiveKit / Mediasoup, WebRTC) containing ICE/TURN Server, SFU Core Routing Engine, ABR Controller, Telemetry & QoS Agent, Token Auth & Session Validator, and Media Recorder / Audit Interceptor
- Integration Adapter Container
- Cloud SQL for PostgreSQL & Memorystore for Redis
- GCP Cloud Storage with Object Retention (WORM)

## Relationships
- Patients and Clinicians -> GCP Global HTTPS Load Balancer: Accesses platform [HTTPS]
- GCP Global HTTPS Load Balancer -> Envoy API Gateway: Routes regional traffic [HTTPS]
- Envoy API Gateway -> Backend Service & Consent & Policy Service: Forwards authenticated requests [gRPC/mTLS]
- Patients and Clinicians -> SFU Media Relay: Streams video consultations [UDP (ICE/STUN/TURN)]
- Token Auth & Session Validator -> Backend Service: Verifies participant access tokens [gRPC/mTLS]
- SFU Core Routing Engine -> Backend Service: Reports call session states and metrics [gRPC]
- Media Recorder / Audit Interceptor -> GCP Cloud Storage: Persists encrypted compliance recordings [HTTPS]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Target cloud infrastructure ensuring regional data isolation.
- LiveKit / Mediasoup: SFU media relay engine providing real-time video processing.
- GKE & FastAPI: Container orchestration and microservice APIs.
- Cloud SQL for PostgreSQL & Memorystore for Redis: Relational data storage and caching.
- WebRTC, WSS, gRPC, and mTLS: Low-latency communication and secure service protocols.

## Rationale
This architecture ensures strict compliance with GDPR and HIPAA by locking EU and US health data into regional GCP boundaries. The modular SFU Media Relay design supports unstable rural connections through adaptive bitrate control and localized degradation modes.