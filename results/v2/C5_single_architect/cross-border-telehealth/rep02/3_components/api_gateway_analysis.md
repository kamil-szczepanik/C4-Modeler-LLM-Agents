## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict data residency, regulatory compliance, and resilience for low-bandwidth connections.

## Key Elements
- **Users**: Patients (EU/US) and Licensed Clinicians.
- **External Systems**: AI Symptom Checker Service, National e-Prescription Gateways (EU), Pharmacy Systems (US), Third-party Video Infrastructure.
- **Containers**: Web & Mobile App (Flutter/React), API Gateway (Google Cloud API Gateway/Envoy), Core Telehealth Service (Go/Spring Boot), AI Symptom Checker Orchestrator (Python/FastAPI), E-Prescription Integration Service (Node.js/Java), Media Relay & Signaling Service (WebRTC/LiveKit), Cloud SQL PostgreSQL, Memorystore Redis.
- **API Gateway Components**: Geo-Routing & Region Enforcer, Authentication & Consent Verifier, Protocol & Payload Translator, Rate Limiting & Degradation Handler.

## Relationships
- **Web App / Mobile App** -> **Geo-Routing Component**: Sends application traffic and real-time signaling [HTTPS and WSS].
- **Geo-Routing Component** -> **Rate Limiting & Degradation Handler**: Routes filtered traffic [Internal gRPC].
- **Rate Limiting & Degradation Handler** -> **Authentication & Consent Verifier**: Verifies tokens and consent [Internal gRPC].
- **Authentication & Consent Verifier** -> **Core Telehealth, AI, & E-Prescription Services**: Forwards authorized requests [gRPC over GCP VPC].
- **API Gateway** -> **Media Relay & Signaling Service**: Routes media and signaling traffic [gRPC over GCP VPC].

## Technology Stack
- **Google Cloud Platform (GCP)**: Target cloud environment across `europe-west3` and `us-central1` regions for regional data isolation.
- **Envoy Proxy / Google Cloud API Gateway**: Powers edge routing, protocol translation, and custom Lua filters for JWT/consent inspection.
- **WebRTC / LiveKit**: Enables low-bandwidth video consultations supporting degraded modes below 300 kbit/s.
- **Go / Spring Boot, Python / FastAPI, Node.js / Java**: Implements core backend microservices and orchestration.
- **Cloud SQL PostgreSQL & Memorystore Redis**: Handles persistent data storage and caching per regional boundaries.

## Rationale
This architecture enforces GDPR and HIPAA compliance by routing and storing EU and US health data strictly within regional GCP boundaries. Furthermore, Envoy-based rate limiting and WebRTC support ensure high availability and continuous video consultations even over unstable rural internet connections.