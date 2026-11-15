## Overview
A multi-region cross-border telehealth platform deployed on GCP provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency while ensuring high availability for unstable rural connections.

## Key Elements
- Patients (EU and US) and Licensed Clinicians (People)
- Regional BFFs and API Gateways (Containers in `europe-west3` and `us-central1`)
- Anti-Corruption Layers (ACLs) and Core Domain Services (Containers)
- AI Symptom Checker and Audit Logging Pipeline (Containers)
- Third-Party Pharmacies and National E-Prescription Endpoints (External Systems)

## Relationships
- Patients/Clinicians interact with Regional BFFs via HTTPS and WebRTC
- Regional BFFs communicate with Core Domain Services and ACLs via gRPC/REST
- ACLs integrate with US systems via HL7 FHIR and EU systems via national e-prescription protocols
- Symptom checker dispatches audit logs to immutable storage via transactional outbox pattern

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce data residency
- **Communication Protocols**: HTTPS, gRPC, and WebRTC with adaptive bitrate streaming for video
- **Interoperability Standards**: HL7 FHIR (US) and national standards (EU) via Anti-Corruption Layers
- **Design Patterns**: CQRS, BFF, Circuit Breakers, and Transactional Outbox for resilience and traceability

## Rationale
The multi-region BFF and ACL architecture cleanly separates regional compliance requirements (GDPR/HIPAA) from core business logic. Client-side state caching and adaptive streaming guarantee continuous video consultations over unstable rural internet connections.