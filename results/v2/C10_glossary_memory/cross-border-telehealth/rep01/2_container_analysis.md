## Overview
[Cross-Border Telehealth Platform [softwareSystem, context]: A unified cross-border telehealth SaaS platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US, enforcing strict regional data residency and compliance using isolated cloud deployments.]

## Key Elements
• [Patients & Licensed Clinicians [person, context]]
• [Pharmacies & Regional Health Authorities/Payers [externalSystem, context]]
• [AI Triage Model Provider [externalSystem, context] (GCP Vertex AI)]
• [Identity & Consent Providers [externalSystem, context]]
• [Web & Mobile Apps [container, Flutter/React]]
• [API Gateway & BFF [container, Envoy/Go]]
• [Core Telehealth Service [container, Java/Spring Boot]]
• [AI Triage Service [container, Python/FastAPI]]
• [Consent & Audit Ledger [container, PostgreSQL]]
• [E-Prescription Dispatcher [container, Go]]

## Relationships
• [Patients & Licensed Clinicians -> Cross-Border Telehealth Platform (HTTPS/WebRTC)]
• [Cross-Border Telehealth Platform -> Pharmacies & Regional Health Authorities/Payers (REST / HL7 FHIR)]
• [Cross-Border Telehealth Platform -> AI Triage Model Provider (Version-pinned inference APIs (mTLS))]
• [Cross-Border Telehealth Platform -> Identity & Consent Providers (OIDC / SAML)]

## Technology Stack
• [Google Cloud Platform (GCP): Target cloud provider utilizing regions europe-west3 and us-central1 for strict regional data residency.]
• [Istio Service Mesh: Enforces mTLS and zero-trust traffic segmentation within regional clusters.]
• [PostgreSQL: Serves as the Consent & Audit Ledger, secured via Customer-Managed Encryption Keys (CMEK) via Cloud KMS.]
• [Flutter/React: Technologies for building the client-facing Web & Mobile Apps.]
• [Envoy/Go: Powers the API Gateway & BFF container for external traffic routing and TLS termination.]
• [Java/Spring Boot: Implements the Core Telehealth Service business logic.]
• [Python/FastAPI: Powers the AI Triage Service for local PHI/PII sanitization and model interaction.]

## Rationale
[Regionally isolated container clusters in GCP ensure strict adherence to GDPR and HIPAA data residency constraints. Decoupled microservices with localized data storage and strict cryptographic controls maintain traceability, availability under low bandwidth, and secure cross-border compliance.]