## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while supporting secure, cross-border care delivery.

## Key Elements
* Patients and Licensed Clinicians
* EU Telehealth Platform Instance (`europe-west3`)
* US Telehealth Platform Instance (`us-central1`)
* National E-Prescription Gateways (EU) & Surescripts/Pharmacy Networks (US)
* Regional Identity Providers (IDP)
* External Payment Gateways (Stripe / Insurance APIs)
* Global TURN/STUN Edge Relays

## Relationships
* Patients and Clinicians to Platform Instances via HTTPS and WebRTC
* Platform Instances to E-Prescription Gateways via REST and HL7 FHIR over mTLS
* Platform Instances to IDP via OIDC and OAuth2
* Platform Instances to Payment Gateways via HTTPS and REST
* EU and US Platform Instances to each other via gRPC/HTTPS gated by consent tokens

## Technology Stack
* Google Cloud Platform: Deployed in `europe-west3` and `us-central1` for strict regional isolation
* WebRTC: Powers video consultations with adaptive bitrate for low-bandwidth rural connections
* GCP KMS: Provides customer-managed encryption keys (CMEK) segregated per region
* HL7 FHIR & REST: Enables interoperable e-prescription dispatch and pharmacy integration
* WORM Storage: Ensures tamper-proof, append-only logging for AI symptom-checker traceability

## Rationale
This architecture ensures strict compliance with GDPR and HIPAA through isolated regional GCP deployments without cross-region compute failover. It guarantees high availability and regulatory traceability for AI diagnostics while maintaining low-bandwidth resilience for rural users.