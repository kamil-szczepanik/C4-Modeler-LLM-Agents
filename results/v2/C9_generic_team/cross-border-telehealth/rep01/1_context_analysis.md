## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data isolation to comply with GDPR and HIPAA mandates.

## Key Elements
* Patients and Clinicians (Client Applications)
* Global Traffic Director / API Gateway
* Regional Stacks (`europe-west3` for EU, `us-central1` for US)
* AI Symptom Checker Service
* Regional Audit and Compliance Logging Subsystem
* External Identity and Consent Provider
* National E-Prescription Gateways and Pharmacy Networks
* External Notification and Messaging Service
* External Payment Gateways and Billing Systems

## Relationships
* Client Applications interact with the Global Traffic Director via HTTPS and WebSockets.
* Global Traffic Director routes regional traffic to `europe-west3` or `us-central1` via mTLS.
* Regional Stacks communicate with National E-Prescription Gateways using HL7 FHIR (US) and national standards (EU).
* Regional Stacks integrate with External Identity and Consent Providers using OpenID Connect (OIDC).
* Regional Stacks process payments via External Payment Gateways using REST APIs over HTTPS.

## Technology Stack
* Google Cloud Platform (GCP): Selected for regional availability in `europe-west3` and `us-central1`.
* HL7 FHIR: Enforces interoperability standards for US healthcare data exchange.
* WebSockets and Adaptive Bitrate Streaming: Ensures video consultations operate in degraded modes below 300 kbit/s.
* mTLS: Secures all internal inter-service and cross-boundary communications.

## Rationale
Isolating infrastructure into GCP `europe-west3` and `us-central1` guarantees that EU and US health data remain strictly within their respective jurisdictions to satisfy GDPR and HIPAA. Decoupled regional boundaries and explicit API gateways maintain high availability, traceability, and low-bandwidth resilience.