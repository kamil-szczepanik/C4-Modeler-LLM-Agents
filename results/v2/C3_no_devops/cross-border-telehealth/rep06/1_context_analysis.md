## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency and compliance using Google Cloud Platform (GCP).

## Key Elements
* Patients and Licensed Clinicians (System Users)
* Local Pharmacies and EU National E-Prescription Networks (External Systems)
* Third-party Video Provider (External System)
* AI Symptom Checker Model Registry (External System)
* Identity Verification Services and Regional Payment Gateways (External Systems)
* Cross-Border Telehealth Platform (Software System deployed in GCP)

## Relationships
* Patients and Clinicians interact with the Platform via HTTPS and WebSockets (WebRTC)
* Platform communicates with EU National E-Prescription Networks via REST/SOAP over HTTPS
* Platform communicates with US Pharmacies via HL7 FHIR over HTTPS
* Platform accesses the AI Symptom Checker Model Registry via gRPC/HTTPS
* Platform integrates with Identity Verification Services and Payment Gateways via HTTPS/REST

## Technology Stack
* GCP (`europe-west3` and `us-central1`) for regional data residency isolation
* WebRTC via Third-party Video Provider for low-bandwidth video consultations
* OAuth 2.0 / OpenID Connect with TLS 1.3 for authentication and transport security
* HL7 FHIR for US interoperability; REST/SOAP for EU e-prescription standards
* WORM audit logging service for HIPAA/GDPR forensic accountability

## Rationale
This architecture guarantees compliance with GDPR and HIPAA through isolated GCP regions and Customer-Managed Encryption Keys. It ensures rural availability via resilient WebRTC streaming and maintains traceability for medical device regulations.