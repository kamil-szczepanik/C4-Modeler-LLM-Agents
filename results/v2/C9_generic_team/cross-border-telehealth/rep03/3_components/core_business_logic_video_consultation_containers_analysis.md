## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces regional data residency and high availability on GCP.

## Key Elements
* WebRTC Media Containers
* Core Business Logic Container
* FHIR/E-Prescription Adapter Containers
* Traceability Logging Container
* GCP Pub/Sub Event Bus
* GCP Memorystore Regional Caches
* GCP Secret Manager

## Relationships
* WebRTC Media Containers -> Patients/Clinicians: Streams video consultations [WebRTC/UDP]
* Core Business Logic Container -> GCP Pub/Sub: Publishes asynchronous events [gRPC/HTTPS]
* Core Business Logic Container -> GCP Memorystore: Stores temporary sync payloads [Redis Protocol]
* Core Business Logic Container -> FHIR/E-Prescription Adapter Containers: Requests prescriptions and external data [gRPC/REST]
* Traceability Logging Container -> Core Business Logic Container: Collects distributed audit logs [OpenTelemetry]

## Technology Stack
* Google Cloud Platform (GCP): Regional deployment provider in europe-west3 and us-central1 ensuring data residency
* WebRTC: Low-latency video streaming protocol supporting degraded network conditions
* OpenTelemetry: Distributed tracing and logging technology for AI recommendation traceability
* GCP Pub/Sub: Asynchronous messaging bus utilizing the Claim Check Pattern for heavy payloads
* GCP Secret Manager: Regional secrets management enforcing strict data residency boundaries

## Rationale
This architecture separates resource-intensive video streaming from I/O-bound business logic, ensuring high availability during degraded network conditions. Hexagonal architecture and Anti-Corruption Layers isolate domain logic from external regional standards while maintaining strict regulatory compliance.