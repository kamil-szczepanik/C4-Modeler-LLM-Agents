## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, regulatory compliance, and resilience for low-bandwidth rural users.

## Key Elements
* Patients (EU & US), Licensed Clinicians, Compliance Officers
* Frontend Client Apps (`Flutter`)
* API Gateway / BFF (`Envoy / gRPC-Web`)
* Video Consultation Service (`WebRTC / SFU - Mediasoup`)
* AI Symptom Checker Container (`Python / FastAPI`)
* E-Prescription Integration Service (`Node.js / Express`)
* Consent & Policy Engine (`Opa / Go`)
* Data Layer (`PostgreSQL / Cloud SQL`)
* External Systems: AI Diagnostic Service, EU National e-Prescription Gateways, US Pharmacy Networks

## Relationships
* Patients and Clinicians interact with Frontend Client Apps via HTTPS and WebRTC.
* Frontend Client Apps communicate with API Gateway / BFF via gRPC-Web and HTTPS.
* API Gateway routes traffic to internal containers protected by mTLS (Anthos Service Mesh).
* Consent & Policy Engine validates data access against regional policies before granting access to Data Layer.
* E-Prescription Integration Service securely connects to external EU Gateways and US Pharmacy Networks via HTTPS / Mutual TLS.

## Technology Stack
* Cloud Platform: Google Cloud Platform (`europe-west3`, `us-central1`) with VPC Service Perimeters for data residency.
* Frontend: `Flutter` for cross-platform web and mobile support.
* Backend Services: `Envoy`, `Mediasoup`, `Python / FastAPI`, `Node.js / Express`, `Opa / Go`.
* Data & Security: `PostgreSQL / Cloud SQL`, Cloud KMS (CMEK), TLS 1.3, SRTP/DTLS-SRTP, OAuth 2.0 / OIDC.
* Observability: OpenTelemetry and Cloud Trace.

## Rationale
The regionalized container architecture strictly enforces GDPR and HIPAA by isolating EU and US data within dedicated GCP regions. Furthermore, adaptive WebRTC streaming, localized consent enforcement, and low-bandwidth optimizations guarantee clinical continuity and regulatory compliance for rural users.