## Overview
[A secure, multi-region telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and resilient delivery for rural, low-bandwidth users.]

## Key Elements
* Patients and Clinicians (Primary Users)
* Regional Application Services Container (GCP GKE clusters in europe-west3 and us-central1)
* Consultation Orchestrator Microservice (Spring Boot)
* Prescription Manager Microservice (Spring Boot)
* Consent & Context Enforcer Microservice (Spring Boot with OPA sidecar)
* Video Consultation Service (Twilio / WebRTC Media Server)
* AI Symptom Checker (Vertex AI endpoints)
* Data & Audit Tier (Cloud SQL / Cloud Spanner)

## Relationships
* API Gateway -> Regional Application Services: Routes validated client requests [gRPC over Istio mTLS]
* Consultation Orchestrator -> Video Consultation Service: Manages video sessions and adaptive bitrate streaming [WebRTC / gRPC]
* Prescription Manager -> Interoperability Adapter: Translates clinical orders to regional standards [gRPC]
* Consent & Context Enforcer -> Local OPA Sidecar: Validates local authorization and consent policies [Local OPA evaluation]
* All Components -> Data & Audit Tier: Persists patient data with regional isolation and OpenTelemetry tracing [PostgreSQL wire protocol / gRPC]

## Technology Stack
* Google Kubernetes Engine (GKE): Regional container orchestration in europe-west3 and us-central1 for strict data residency (R-05)
* Spring Boot: Microservice framework for internal orchestration logic
* Open Policy Agent (OPA): Sidecar for decentralized authorization and consent enforcement (R-04)
* Istio Service Mesh: Manages mTLS encryption in transit and traffic routing for degraded network modes (R-06)
* OpenTelemetry: End-to-end distributed tracing for auditability and compliance (R-07)
* GCP Cloud KMS & Secret Manager: Cryptographic isolation using Customer-Managed Encryption Keys (CMEK) and runtime secret injection

## Rationale
[This architecture enforces regional data boundaries and regulatory compliance via dedicated GCP regions and OPA enforcement. It guarantees high availability and auditability for healthcare workflows through resilient microservices, Istio traffic policies, and OpenTelemetry tracing.]