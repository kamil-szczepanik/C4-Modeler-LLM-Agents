## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and regulatory compliance.

## Key Elements
- **Patients and Clinicians**: End users accessing telehealth services via client applications.
- **Client Apps**: Flutter / React Native mobile and web applications.
- **API Gateway**: Google Cloud API Gateway / Envoy managing entry points.
- **Core Telehealth Service**: Go / gRPC & REST service managing primary telehealth logic.
- **Video Consultation Service**: Mediasoup SFU on GCE handling video streams.
- **AI Symptom Checker**: Python / FastAPI + PyTorch container assessing care urgency.
- **Integration Service**: Java / Spring Boot service connecting to external pharmacy networks.
- **Message Broker**: Google Cloud Pub/Sub managing asynchronous messaging with regional topics (`eu-events`, `us-events`), Schema Registry, and Dead Letter Queues.
- **Infrastructure**: Google Kubernetes Engine (GKE) and Istio Service Mesh across `europe-west3` and `us-central1`.

## Relationships
- Client Apps -> API Gateway: Invokes APIs via HTTPS / WSS.
- Core Telehealth Service -> Message Broker: Publishes asynchronous events and e-prescription messages via gRPC (`google.pubsub.v1.Publisher`).
- Message Broker -> Integration Service: Delivers payloads via push/pull subscriptions using HTTPS/gRPC.
- Integration Service -> Dead Letter Queues: Manages manual replay and inspection of failed e-prescriptions via Cloud Pub/Sub API (`gRPC`).

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3`, `us-central1`) for region-locked infrastructure.
- **Message Broker**: Google Cloud Pub/Sub with regional topics for strict data residency.
- **Encryption**: Cloud KMS with Customer-Managed Encryption Keys (CMEK) for application-layer encryption.
- **Security & Networking**: Istio Service Mesh with mTLS and Workload Identity Federation.
- **Observability**: OpenTelemetry and Google Cloud Monitoring for tracing and backlog metrics.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating EU and US health data into regional GCP locations using partitioned Pub/Sub topics and regional CMEK encryption. The messaging design supports high availability and resilience for rural users with unstable connections through extended message retention and Dead Letter Queues.