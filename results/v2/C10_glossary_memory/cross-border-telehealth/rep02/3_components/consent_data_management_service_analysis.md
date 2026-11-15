## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It guarantees strict regional data residency, GDPR, HIPAA, and EU MDR compliance using GCP.

## Key Elements
- Patients (EU & US), Licensed Clinicians, Pharmacists (EU/US), Compliance & Regulatory Auditors
- Frontend UI (with localization) (Flutter Web/Mobile)
- Regional API Gateways (GCP Cloud Endpoints/API Gateway)
- Video Streaming Service (WebRTC, UDP/TCP/TLS, TURN)
- AI Symptom Checker Service (AI / GCP, Cloud HSM)
- Consent & Data Management Service (CMEK, GCP) containing: Consent API Controller, Residency Enforcer & Policy Engine, Regional Vault Manager, Consent Event Publisher, Break-Glass Evaluator
- Immutable Logging Service (GCP Cloud Storage, Cloud Logging, Pub/Sub)
- National e-Prescription Gateways (EU), Pharmacy Systems (US), Third-Party Video Infrastructure (WebRTC CPaaS), Regional Identity Providers (eIDAS/OIDC/OAuth 2.0)

## Relationships
- Patients (EU & US) -> Frontend UI (with localization) (HTTPS (TLS 1.3), secure WebSockets, OIDC/OAuth 2.0)
- Frontend UI (with localization) -> Regional API Gateways (HTTPS (REST/GraphQL), TLS 1.3)
- Regional API Gateways -> Consent & Data Management Service (gRPC over mTLS)
- Consent API Controller -> Residency Enforcer & Policy Engine (In-process function calls)
- Residency Enforcer & Policy Engine -> Regional Vault Manager (JDBC over mTLS)
- Residency Enforcer & Policy Engine -> Consent Event Publisher (GCP Pub/Sub)
- Consent API Controller -> Break-Glass Evaluator (In-process validation)
- Break-Glass Evaluator -> Immutable Logging Service (GCP Pub/Sub, regional CMEK)
- Regional API Gateways -> Third-Party Video Infrastructure (WebRTC CPaaS) (WebRTC (UDP/TCP/TLS via TURN))
- Regional API Gateways -> National e-Prescription Gateways (EU) (HTTPS/REST)
- Regional API Gateways -> Pharmacy Systems (US) (HTTPS/REST (HL7 FHIR))

## Technology Stack
- Google Cloud Platform (GCP): Deployment target providing regional isolation (`europe-west3`, `us-central1`)
- Go and Java/Spring Boot: Backend services language stack for high-performance and enterprise compliance
- Open Policy Agent (OPA): Dynamic consent and residency policy evaluation engine
- GCP Cloud KMS & CMEK: Regional key management ensuring zero cross-region key or data leakage
- WebRTC & GCP Pub/Sub: Real-time video streaming and instant cross-region consent revocation event propagation
- OAuth 2.0 / JWT & mTLS (SPIFFE/SPIRE): Strict zero-trust authentication and inter-service transport security

## Rationale
This architecture isolates EU and US health data within designated GCP regions using CMEK and OPA to enforce stringent GDPR and HIPAA compliance. Dedicated micro-components like the Break-Glass Evaluator and Consent Event Publisher ensure secure, auditable emergency access and rapid revocation without violating regional data residency.