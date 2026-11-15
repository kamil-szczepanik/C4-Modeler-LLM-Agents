## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The system ensures regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and robust availability on unstable connections.

## Key Elements
* Patients (EU & US)
* Licensed Clinicians
* Pharmacies (EU & US)
* EU Telehealth Platform (GCP europe-west3)
* US Telehealth Platform (GCP us-central1)
* Region-isolated AI Symptom Checker instances
* Identity Providers (Auth0 / GCP IAM)
* National e-Prescription Gateways (EU) and US Pharmacy Networks
* Payment Gateways (Stripe)

## Relationships
* Patients and Clinicians interact with regional telehealth platforms via HTTPS/WebRTC
* EU/US Platforms connect to Identity Providers via OAuth2/OIDC
* EU Platform connects to National e-Prescription Gateways via REST/national standards
* US Platform connects to US Pharmacy Networks via HL7 FHIR
* Regional platforms interact with local AI Symptom Checker instances via gRPC/HTTPS with immutable logging
* Cross-region platform communication occurs exclusively via mTLS and consent-gated OAuth2 token exchange

## Technology Stack
* GCP (europe-west3 and us-central1): Chosen for regional isolation and compliance enforcement
* WebRTC: Powers real-time video/audio consultations with dynamic codec downscaling for low-bandwidth connections (<300 kbit/s)
* HL7 FHIR & REST: Ensures interoperability for US health data and e-prescriptions
* Auth0 / GCP IAM: Handles secure authentication via OAuth2/OIDC
* Terraform & Docker: Manages independent GitOps pipelines and immutable container deployments

## Rationale
The multi-region GCP architecture guarantees strict adherence to GDPR and HIPAA data residency constraints by physically isolating EU and US workloads. Deploying region-specific AI symptom checker instances and dynamic WebRTC handling satisfies EU MDR traceability mandates and maintains clinical accessibility for rural users.