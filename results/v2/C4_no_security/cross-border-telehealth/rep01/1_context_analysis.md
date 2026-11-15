## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for EU and US patients. The system strictly enforces regional data residency while ensuring compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Cross-Border Telehealth Platform (GCP regions `europe-west3` and `us-central1`)
- AI Symptom Checker Engine (External Medical Device)
- EU National E-Prescription Gateways and US Pharmacy Networks
- Notification Service (Twilio/FCM)
- Identity Providers (EU eID / US OAuth/SAML)

## Relationships
- Patients and Clinicians interact with the Platform via HTTPS and WebRTC
- Platform connects to external Pharmacy Networks and E-Prescription Gateways via secured APIs (TLS 1.3)
- Platform integrates with the External AI Symptom Checker Engine via REST/gRPC (TLS 1.3) with payload logging
- Platform utilizes regional asynchronous message queues for Notification Services

## Technology Stack
- Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict data residency
- WebRTC with adaptive bitrate fallback for video consultations below 300 kbit/s
- Cloud CDN and regional Edge PoPs for low-bandwidth rural availability
- HL7 FHIR for US interoperability and national standards for EU e-prescriptions
- Cryptographically immutable audit logging systems per region

## Rationale
This architecture guarantees strict regional data isolation to satisfy GDPR and HIPAA requirements while maintaining high availability for low-bandwidth rural users. Externalizing and logging AI interactions ensures full compliance and traceability under the EU MDR.