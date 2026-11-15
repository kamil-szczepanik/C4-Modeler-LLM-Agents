## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and resilient media streaming for unstable connections.]

## Key Elements
* Patients [person, container]
* Licensed Clinicians [person, container]
* Compliance Officers / Auditors [person, container]
* Web Application Container (React / Next.js)
* API Gateway Container (Envoy / GCP API Gateway)
* Core Services Container (Go / Node.js microservices)
* AI Symptom Checker Container (Python / FastAPI + Vertex AI)
* Media Relay Container (Janus / WebRTC SFU)
* E-Prescription Integration Container (Java / Spring Boot)
* Databases (GCP Cloud SQL for PostgreSQL)

## Relationships
* Patients -> Web Application Container [HTTPS]
* Licensed Clinicians -> Web Application Container [HTTPS]
* Web Application Container -> API Gateway Container [HTTPS / REST & GraphQL]
* Patients -> Media Relay Container [WebRTC / DTLS-SRTP, UDP]
* Licensed Clinicians -> Media Relay Container [WebRTC / DTLS-SRTP, UDP]
* API Gateway Container -> Core Services Container [gRPC over mTLS]
* API Gateway Container -> AI Symptom Checker Container [gRPC over mTLS]
* Core Services Container -> E-Prescription Integration Container [gRPC over mTLS]
* Core Services Container -> Databases [TCP / SSL]
* E-Prescription Integration Container -> EU National E-Prescription Gateways [HTTPS / mTLS / HL7 FHIR]
* E-Prescription Integration Container -> US Pharmacy Networks (Surescripts) [HTTPS / mTLS / HL7 FHIR]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance for EU and US health data.
* Janus / WebRTC SFU: Powers real-time video consultations with adaptive bitrate control for degraded network modes (< 300 kbit/s).
* GCP Cloud SQL for PostgreSQL: Provides secure, persistent relational data storage protected via CMEK.
* Python / FastAPI + Vertex AI: Powers traceable, versioned AI symptom-checker recommendations.
* Java / Spring Boot: Handles external interoperability with EU e-prescription gateways and US Surescripts networks.

## Rationale
[This architecture enforces strict regional data residency by deploying independent regional instances in GCP. It guarantees uninterrupted clinical care for rural patients through resilient WebRTC media relaying and adaptive bitrate control.]