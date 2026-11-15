## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, regulatory compliance, and resilience for low-bandwidth rural users.

## Key Elements
- Patients (EU & US) and Licensed Clinicians (System Users)
- External Pharmacies (EU & US)
- API Gateway & Edge Service with Envoy Sidecar Proxy
- Core Telehealth Services (User Profiles, Video Sessions, Consent Management)
- AI Symptom Checker Engine
- E-Prescription Integration Service
- Regional Data Tier (Cloud SQL, WORM Cloud Storage)
- GCP Regional Infrastructure (`europe-west3` and `us-central1`)

## Relationships
- Patients & Clinicians to API Gateway: HTTPS / WebRTC
- API Gateway to Core Telehealth Services: gRPC / REST over internal VPC
- AI Symptom Checker to Regional WORM Storage: Secure audit logging over HTTPS
- E-Prescription Service to External Pharmacies: HL7 FHIR (US) and National Standards (EU) via Mutual TLS / HTTPS

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider utilizing `europe-west3` and `us-central1` regions for regional isolation
- Kubernetes (GKE): Orchestrates stateless microservices across independent regional clusters
- Envoy Proxy: Sidecar proxy handling WebRTC traffic shaping and adaptive bitrate throttling for low-bandwidth resilience
- Cloud SQL: Region-locked managed databases guaranteeing GDPR and HIPAA data residency compliance
- Cloud Storage (WORM / Bucket Lock): Secures immutable AI symptom-checker decision logs for audit traceability

## Rationale
The federated regional architecture on GCP strictly enforces GDPR and HIPAA data residency constraints by keeping EU health data in `europe-west3` and US data in `us-central1`. Edge termination, Envoy sidecars, and immutable WORM logging ensure high availability for low-bandwidth rural users and rigorous audit traceability for EU MDR compliance.