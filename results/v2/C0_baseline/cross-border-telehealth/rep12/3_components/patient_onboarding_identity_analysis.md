## Overview
This system is a cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability for rural users.

## Key Elements
- Patients and Licensed Clinicians
- Web/Mobile Client Applications (Flutter / React Native)
- Cloud Load Balancing / API Gateway (OAuth2/OIDC, TLS 1.3)
- Patient Onboarding & Identity Container (Cloud Run & GKE)
- `Edge Registration API` (Cloud Run / Node.js or Go)
- `Identity Core Engine` (GKE / Spring Boot)
- `Data Residency Router` & `Regional Data Store Gateway`
- External Identity Providers (eIDAS for EU, ID-Matching for US)
- Google Cloud KMS (CMEK) and Google Secret Manager
- Google Cloud Pub/Sub, BigQuery, and Cloud Monitoring

## Relationships
- Web/Mobile Client -> Cloud Load Balancing / API Gateway: Routes client requests via HTTPS/REST [TLS 1.3]
- Cloud Load Balancing / API Gateway -> Edge Registration API: Forwards authenticated onboarding requests [gRPC over mTLS]
- Edge Registration API -> Identity Core Engine: Delegates processing of identity workflows [Internal gRPC over mTLS]
- Identity Core Engine -> External Identity Providers: Authenticates users and performs identity verification [HTTPS/REST, signed JWTs]
- Identity Core Engine -> Regional Data Store Gateway: Enforces geo-partitioning and stores profile data [gRPC over mTLS]
- Services -> Google Cloud KMS: Encrypts data at rest using regional Customer-Managed Encryption Keys [Google Cloud API]

## Technology Stack
- **Cloud Provider:** GCP (`europe-west3` and `us-central1`) for regional data isolation and multi-region deployment.
- **Compute:** Cloud Run for stateless edge APIs (low latency, scale-to-zero) and Google Kubernetes Engine (GKE) for core identity microservices.
- **Frameworks:** Spring Boot for heavy identity engine logic; Node.js or Go for lightweight edge routing.
- **Security & Compliance:** Google Cloud KMS (CMEK), Google Cloud Armor, reCAPTCHA Enterprise, OAuth2/OIDC with PKCE, and mTLS for internal transport.
- **Observability:** OpenTelemetry, Google Cloud Logging, and BigQuery for audit logging.

## Rationale
This architecture uses a hybrid Cloud Run and GKE deployment model to balance ultra-low latency for unstable rural connections with robust backend identity processing. Regional VPC Service Controls, CMEK encryption, and dedicated data gateways physically enforce GDPR and HIPAA data residency mandates.