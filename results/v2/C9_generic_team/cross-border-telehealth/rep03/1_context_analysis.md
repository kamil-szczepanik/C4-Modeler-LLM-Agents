## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients.]
[Enforces strict regional data residency and compliance via isolated GCP deployments.]

## Key Elements
* Patients and Licensed Clinicians (End-Users)
* Cross-Border Telehealth Platforms (Isolated Regional Stacks in `europe-west3` and `us-central1`)
* API Gateway / Edge Proxy with Geo-Routing
* Federated Consent & Identity Provider (IdP)
* Anti-Corruption Layer (ACL)
* CQRS Audit Logger & WORM Storage
* External Systems: US HL7 FHIR Providers, EU National E-Prescription Gateways, Regional Pharmacy Networks

## Relationships
* Patients to API Gateway via HTTPS/WebRTC (Adaptive streaming for low bandwidth)
* API Gateway to Regional Stacks via internal gRPC/HTTPS
* Regional Stacks to US HL7 FHIR Providers and EU National E-Prescription Gateways via REST/FHIR/National Protocols
* Regional Stacks to CQRS Audit Logger via Asynchronous Pub/Sub Events

## Technology Stack
* Cloud Platform: GCP (`europe-west3` for EU, `us-central1` for US) for isolated regional data residency
* Streaming/Communication: WebRTC with adaptive codecs for degraded connections (<300 kbit/s)
* Storage: Write-Once-Read-Many (WORM) storage and append-only buckets for AI audit logging
* Messaging: Regionally isolated GCP Pub/Sub for asynchronous event-driven communication
* Interoperability: HL7 FHIR (US) and national e-prescription standards (EU) via custom Anti-Corruption Layers

## Rationale
[Isolated regional deployments guarantee absolute GDPR and HIPAA compliance while preventing cross-border telemetry and data leakage.]
[Decoupled CQRS patterns and federated identity ensure high availability, regulatory traceability, and resilient performance over unstable rural connections.]