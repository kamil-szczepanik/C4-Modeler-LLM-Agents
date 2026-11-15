## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system enforces strict regional data residency and GDPR/HIPAA compliance while supporting low-bandwidth connections.

## Key Elements
- **Patient & Clinician**: End users accessing the platform via Web/Mobile Client SPA/PWA (Flutter/React).
- **Google Cloud API Gateway**: Entry point for inbound client requests.
- **Data Residency & Consent Router**: Go-based container containing Geo-Routing Policy Engine, Consent Interceptor Middleware, Audit Logger, and Regional Proxy Dispatcher.
- **Core Services Backend**: Go/Spring Boot container managing business logic in `europe-west3` and `us-central1`.
- **AI Symptom Checker Service**: Python/FastAPI container for triage recommendations.
- **Video Streaming Server**: LiveKit WebRTC SFU on Google Kubernetes Engine (GKE).
- **Cloud SQL PostgreSQL**: Regional database instances.
- **External Systems**: National Identity Providers, National Health Registries, External Pharmacy Systems, AI Model Provider API.

## Relationships
- **Patient/Clinician** -> **Google Cloud API Gateway**: Sends HTTPS/WSS requests.
- **Google Cloud API Gateway** -> **Data Residency & Consent Router**: Routes inbound requests [gRPC].
- **Geo-Routing Policy Engine** -> **Consent Interceptor Middleware**: Passes validated regional context [In-memory Go struct].
- **Consent Interceptor Middleware** -> **Regional Proxy Dispatcher**: Triggers inter-region dispatch upon verified consent [In-memory].
- **Regional Proxy Dispatcher** -> **Core Services Backend**: Forwards requests to region-pinned instances [mTLS via gRPC].
- **Consent Interceptor Middleware** -> **Cloud SQL PostgreSQL**: Queries regional consent state [pgx / gRPC].
- **Core Services Backend** -> **AI Symptom Checker Service**: Evaluates symptom urgency [REST/gRPC].
- **Core Services Backend** -> **External Pharmacy Systems**: Sends e-prescriptions via national EU standards and US HL7 FHIR.

## Technology Stack
- **Google Cloud Platform (GCP)**: Targeted cloud provider using `europe-west3` and `us-central1` regions for regional data residency.
- **Go**: Language for API gateway, core backend, and Data Residency & Consent Router due to high throughput and low latency.
- **Python / FastAPI**: Framework for AI Symptom Checker Service to integrate ML libraries.
- **LiveKit (WebRTC SFU)**: Powers real-time video consultations supporting degraded modes below 300 kbit/s.
- **PostgreSQL (Cloud SQL)**: Relational data store isolated per region.
- **gRPC / mTLS**: Protocol for secure, high-performance inter-service communication.

## Rationale
This architecture uses GCP multi-region deployment (`europe-west3` and `us-central1`) combined with a dedicated Data Residency & Consent Router to strictly isolate EU and US health data per GDPR and HIPAA mandates. Go and gRPC provide the low latency and security required for real-time compliance enforcement without degrading video consultation performance.