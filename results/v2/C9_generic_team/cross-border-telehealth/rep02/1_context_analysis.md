## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
* Patients and Licensed Clinicians (System Actors)
* EU Platform Instance (`europe-west3`) and US Platform Instance (`us-central1`) (Containers)
* Edge / Adaptive Media Relay (External System)
* EU/US Pharmacies & National E-Prescription Gateways (External Systems)
* AI Model Registry (External System)
* Consent & Identity Provider Boundary / External IdP & Federation Service (External Systems)
* External Notification & Messaging Gateway (External System)
* Telemetry/Audit Collector & Global Clock / NTP (External Systems)
* External Payment and Billing Gateways (External Systems)

## Relationships
* Patients to EU/US Platform Instances via HTTPS (REST/GraphQL) and WebRTC for video
* EU/US Platform Instances to Edge / Adaptive Media Relay via WebRTC/RTP for throttled video streaming (<300 kbit/s)
* EU/US Platform Instances to National E-Prescription Gateways via HL7 FHIR (US) and national e-prescription standards (EU)
* AI Symptom Checker to AI Model Registry via gRPC for version-tracked recommendations
* Platform Instances to Consent & Identity Provider via OAuth2/OIDC for localized token issuance and consent management
* Platform Instances to External Notification & Messaging Gateway via SMTP/SMPP/APNS for asynchronous alerts
* Platform Instances to Telemetry/Audit Collector via TLS for immutable audit logs
* Platform Instances to External Payment Gateways via REST/HTTPS for PCI-DSS compliant billing

## Technology Stack
* Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` to enforce geographic data isolation.
* WebRTC: Powers real-time video consultations with adaptive bitrate streaming.
* HL7 FHIR & National Standards: Ensures interoperability with US and EU health systems.
* OAuth2 / OIDC: Secures authentication and token-based federation.

## Rationale
The two isolated regional GCP deployments guarantee strict compliance with GDPR and HIPAA data residency mandates. Decoupling external gateways for media, payments, notifications, and identity isolates compliance blast radii and maintains system resilience over unstable rural connections.