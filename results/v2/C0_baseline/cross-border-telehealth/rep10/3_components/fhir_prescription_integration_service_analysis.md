## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency and regulatory compliance across both jurisdictions.

## Key Elements
- Patients (EU / US), Licensed Clinicians, Local Pharmacies, Compliance Auditors
- Regional API Gateway / BFF (Node.js, GraphQL)
- FHIR & Prescription Integration Service (.NET Core)
- Prescription Orchestrator, FHIR Adapter, EU Gateway Adapter, Validation & Mapping Validator
- Regional WORM Storage (GCP Cloud Storage, Cloud KMS)
- National e-Prescription Gateways and US Pharmacy Networks

## Relationships
- Regional API Gateway -> FHIR & Prescription Integration Service [gRPC, mTLS, Istio Service Mesh]
- FHIR & Prescription Integration Service -> National Gateways / Pharmacy Networks [REST/FHIR, SOAP, mTLS]
- FHIR & Prescription Integration Service -> Regional WORM Storage [TLS 1.3, Cloud KMS]
- Prescription Orchestrator -> MassTransit & Notification Event Consumer [In-Process Bus]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud utilizing `europe-west3` and `us-central1` for regional data residency.
- .NET Core & C#: Powers the FHIR & Prescription Integration Service with high performance.
- MassTransit & Transactional Outbox: Ensures zero message loss when communicating with unstable pharmacy networks.
- GCP Cloud KMS & HSM: Handles field-level encryption, audit logging checksums, and cryptographic payload signing for legal non-repudiation.
- Istio Service Mesh & Polly: Provides mTLS, gRPC rate limiting, and circuit breakers for resilience against gateway failures.

## Rationale
This architecture enforces strict regional data residency and HIPAA/GDPR compliance by isolating data processing to dedicated GCP regions. Asynchronous messaging and transactional outboxes guarantee reliable cross-border e-prescription delivery despite unstable network connections.