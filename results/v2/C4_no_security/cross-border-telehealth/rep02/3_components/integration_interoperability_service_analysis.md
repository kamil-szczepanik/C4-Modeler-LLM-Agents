## Overview
The Cross-Border Telehealth Platform delivers secure video consultations, e-prescriptions, and AI symptom checking to patients across the EU and US. The architecture enforces strict regional data isolation to maintain GDPR and HIPAA compliance while bridging disparate national healthcare systems.

## Key Elements
- Patients (EU & US) and Licensed Clinicians (Primary Users)
- Web Frontend (PWA built with Next.js / React)
- API Gateway (Envoy and Cloud Load Balancing)
- Core Backend Services (Go / Spring Boot)
- AI Symptom Checker (Python / FastAPI)
- Integration / Interoperability Service (Java / Spring Boot / Apache Camel)
- Media Relaying Service (LiveKit SFU/MCU)
- Data Storage (Cloud SQL PostgreSQL and Cloud Storage)
- Regional Messaging & Buffering (Cloud Pub/Sub with Dead Letter Queue)
- External Pharmacies (US & EU National Adapters via eHDSI/NCPeH)

## Relationships
- Web Frontend -> API Gateway: Client requests [HTTPS / WSS]
- API Gateway -> Core Backend Services: API routing [gRPC]
- Core Backend Services -> Integration / Interoperability Service: Triggers prescription workflows [gRPC]
- Integration / Interoperability Service -> External Pharmacies: Sends e-prescriptions [HL7 FHIR / HTTPS / NCPeH]
- Integration / Interoperability Service -> Cloud Pub/Sub: Publishes delivery audit events [PubSub API / gRPC]
- Media Relaying Service -> Patients & Clinicians: Handles real-time video streaming [WebRTC]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for data residency.
- Java (Spring Boot / Apache Camel): Core runtime and routing engine for enterprise healthcare interoperability.
- Cloud Pub/Sub: Asynchronous event messaging and Dead Letter Queue management.
- Redis (Memorystore): Distributed cache ensuring idempotency and deduplication.
- OpenTelemetry: Distributed tracing and observability across microservices.

## Rationale
Regional deployment isolation guarantees that EU health data remains in `europe-west3` and US data in `us-central1`, satisfying GDPR and HIPAA constraints. Apache Camel and HL7 FHIR/national adapters ensure seamless interoperability with diverse regional pharmacy networks.