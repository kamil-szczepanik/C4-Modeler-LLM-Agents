## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring HIPAA and GDPR compliance.

## Key Elements
- **Users**: Patients (EU/US), Licensed Clinicians, Local Pharmacies, Regulators, System Administrators, and Caregivers/Guardians.
- **Client Applications**: Flutter/React Native Web and Mobile Apps.
- **Backend Containers**: Kong API Gateway/BFF, Spring Boot Core Telehealth Service, FastAPI AI Symptom Checker, Node.js E-Prescription Service, Java Consent Management Service, and Node.js/Go Billing & Localization Container.
- **Data & Infrastructure**: GCP Cloud SQL (PostgreSQL), GCP Cloud Storage, GCP Cloud Pub/Sub, and Cloud KMS.

## Relationships
- **Clients to API Gateway**: HTTPS and WebSockets using TLS 1.3 and OAuth2/OIDC authentication.
- **Internal Containers**: gRPC and GCP Cloud Pub/Sub protected by mTLS via Anthos Service Mesh.
- **External Integration**: National E-Prescription Gateways and Pharmacy Networks via HL7 FHIR and national standards.

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) to enforce regional data isolation.
- **Backend & API**: Spring Boot, FastAPI, Node.js, and Kong API Gateway for scalable microservices.
- **Security**: Cloud KMS with CMEK, VPC Service Controls, and signed PASETO/JWT tokens for consent enforcement.
- **Messaging**: GCP Cloud Pub/Sub with client-side payload encryption for cross-service events.

## Rationale
This architecture isolates health data within regional boundaries using GCP regions, satisfying GDPR and HIPAA constraints. Dedicated microservices for consent and billing ensure regulatory compliance, security, and traceability under the EU MDR.