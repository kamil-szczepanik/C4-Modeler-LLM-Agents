## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- **Users**: Patients, Licensed Clinicians, Pharmacies, Compliance Officers/Auditors
- **Core Systems**: Regional GCP Deployments (`europe-west3`, `us-central1`), API Gateways, WebRTC SFUs
- **External Systems**: EU National E-Prescription Gateways, US Pharmacy Networks, External Identity Providers (eIDAS, Login.gov), Regional Payment Gateways (Stripe EU/US)

## Relationships
- Patients and Clinicians interact with Regional API Gateways via HTTPS and WebSockets
- Regional API Gateways communicate with internal microservices using mTLS
- Regional deployments interface with EU/US Pharmacy Networks and E-Prescription Gateways via REST, SOAP, and HL7 FHIR over HTTPS
- External IdPs authenticate users via OIDC/SAML

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for data residency
- **Networking/Routing**: GCP Cloud Load Balancing with Geo-routing and regional API Gateways for perimeter enforcement
- **Video/Streaming**: WebRTC Selective Forwarding Units (SFUs) with adaptive bitrate streaming for degraded connectivity
- **Security/Auth**: OAuth 2.0 / OIDC with FAPI profiles, Cloud KMS (CMEK) for regional encryption, and edge-evaluated ABAC
- **Logging/Compliance**: GCP Cloud Logging and Pub/Sub with decoupled, regionally isolated telemetry stacks

## Rationale
This architecture uses multi-region GCP deployments with strict network boundaries and localized key management to satisfy GDPR and HIPAA data residency mandates. Regionally isolated observability stacks, WebRTC SFUs, and edge ABAC ensure EU MDR traceability and continuous availability for rural users.