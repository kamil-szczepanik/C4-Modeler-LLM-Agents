## Overview
- Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.
- Designed with strict regional data residency, high availability for rural areas, and regulatory compliance (GDPR, HIPAA, EU MDR).

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Region Router
- Offline-First Patient Mobile/Web App
- Consent Management Container
- Core Business Logic & Video Consultation Containers
- Traceability Logging Container
- FHIR/E-Prescription Adapter Containers
- Event-Driven Integration Bus
- Regional Caches

## Relationships
- Patients and Licensed Clinicians -> API Gateway / Region Router: Connects via HTTPS and WebSockets
- Offline-First Patient Mobile/Web App -> API Gateway / Region Router: Synchronizes state and sends requests using REST and gRPC with idempotency keys
- API Gateway / Region Router -> Consent Management Container: Enforces authorization middleware via internal APIs
- API Gateway / Region Router -> Core Business Logic & Video Consultation Containers: Routes traffic to regional boundaries using gRPC and REST over mTLS

## Technology Stack
- Google Cloud Platform (GCP): Cloud provider for infrastructure deployment
- GCP Regions (`europe-west3`, `us-central1`): Enforces data residency for EU and US health data
- Geo-DNS and Anycast IP: Directs global traffic to regional perimeters at the network edge
- GCP Memorystore: Provides fast distributed caching for idempotency validation and read models
- OpenTelemetry Collector: Captures traceable logs and metrics for accountability
- WebRTC: Powers real-time video consultations in regional containers

## Rationale
- Regional GCP perimeters and strict edge routing guarantee GDPR and HIPAA compliance by ensuring EU and US health data never leaves its jurisdiction.
- Edge-level idempotency, compression, and request buffering maintain application availability and data integrity over unstable rural internet connections.