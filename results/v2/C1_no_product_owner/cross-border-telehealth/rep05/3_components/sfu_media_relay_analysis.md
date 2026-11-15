## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and low-bandwidth resilience for rural users.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (Go, Envoy)
- Consultation Service (Node.js, WebRTC)
- SFU Media Relay Container (Mediasoup, C++):
  - RTP/RTCP Packet Processor
  - Simulcast & Layer Manager
  - Regional Egress Controller
  - Token Validation & Signaling Agent
- Clinical & Prescription Service (Java, Spring Boot)
- AI Symptom Checker (Python, FastAPI)
- Consent & Policy Engine (Go)
- Regional Message Broker (GCP Pub/Sub)
- Cloud SQL (PostgreSQL)

## Relationships
- Patients/Clinicians -> API Gateway: Client requests [HTTPS / WSS]
- Consultation Service -> Token Validation & Signaling Agent: Validates session token and negotiates ICE/SDP [gRPC over TLS]
- Token Validation & Signaling Agent -> Simulcast & Layer Manager: Passes authorized session context [In-memory C++ API]
- Simulcast & Layer Manager -> RTP/RTCP Packet Processor: Stream routing rules [In-memory C++ API]
- SFU Media Relay -> Regional Egress Controller: Enforces regional boundary drops [Internal C++ policy hook]
- Consultation Service -> SFU Media Relay: Relays video and audio streams [WebRTC/UDP (DTLS-SRTP)]

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for localized data processing.
- Google Kubernetes Engine (GKE): Orchestrates containerized workloads with regional node pools and VPC Service Controls.
- Mediasoup (C++): Powers the SFU Media Relay for high-performance, low-latency video bridging.
- Go & Java (Spring Boot): Used for resilient backend microservices and policy enforcement.
- DTLS-SRTP & mTLS: Encrypts media payloads and service-to-service communication.

## Rationale
The architecture ensures regional compliance by isolating data processing within GCP EU and US regions through dedicated node pools and VPC controls. The C++ Mediasoup-based SFU with simulcast layer management guarantees stable video consultations under constrained bandwidth conditions.