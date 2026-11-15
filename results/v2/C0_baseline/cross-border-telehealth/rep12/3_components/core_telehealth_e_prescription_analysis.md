## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US under a single provider. The architecture enforces regional data residency, GDPR and HIPAA compliance, and reliable operations during unstable internet connections.]

## Key Elements
- Patients, Licensed Clinicians, Pharmacies, Compliance Officers/Auditors
- EU National E-Prescription Gateways, US Pharmacy Networks, External Identity Providers, Regional Payment Gateways
- Web/Mobile Client Applications (Flutter / React Native)
- Cloud Load Balancing / API Gateway (OAuth2/OIDC, TLS 1.3)
- Video Consultation Service (LiveKit WebRTC SFU on GKE)
- AI Symptom Checker (Python / FastAPI on Cloud Run)
- Consent Management Service (Spring Boot on GKE)
- Core Telehealth & E-Prescription (Spring Boot on GKE)
- Internal Components: Telehealth Workflow Manager, E-Prescription Engine, Consent Enforcement Interceptor, Prescription Dispatcher Adapter, Dead-Letter & Retry Queue Handler, Crypto & Signing Service
- Google Cloud Pub/Sub, Google Cloud Logging, BigQuery, Google Cloud KMS (CMEK), Google Secret Manager

## Relationships
- Cloud Load Balancing / API Gateway -> Core Telehealth & E-Prescription [gRPC over mTLS]
- Consent Enforcement Interceptor -> Consent Management Service [gRPC with JIT validation]
- Core Telehealth & E-Prescription -> EU National E-Prescription Gateways [REST, HL7 FHIR over HTTPS, mTLS]
- Core Telehealth & E-Prescription -> US Pharmacy Networks [REST, HL7 FHIR over HTTPS, mTLS]
- Prescription Dispatcher Adapter -> Dead-Letter & Retry Queue Handler [In-process Java method call]
- Dead-Letter & Retry Queue Handler -> Cloud Pub/Sub [Google Cloud Pub/Sub with envelope encryption]
- E-Prescription Engine -> Crypto & Signing Service [In-process Java method call]
- Core Telehealth & E-Prescription -> Cloud Logging & BigQuery [Google Cloud Logging, BigQuery]

## Technology Stack
- GCP (regions: europe-west3, us-central1) for physical data residency enforcement
- GKE (Google Kubernetes Engine) and Cloud Run for containerized microservices deployment
- Spring Boot / Spring Security / Spring Integration for Java-based backend components
- Python / FastAPI for the AI Symptom Checker container
- LiveKit WebRTC SFU for video consultations with degraded network adaptation (<300 kbit/s)
- HL7 FHIR for US interoperability and national standards for EU e-prescriptions
- Google Cloud KMS (CMEK) and BouncyCastle for cryptographic signing, envelope encryption, and PHI protection
- Google Secret Manager for mTLS client certificate pinning
- Google Cloud Pub/Sub for asynchronous messaging, retries, and dead-letter queueing
- Resilience4j for circuit breaking and fault tolerance

## Rationale
[This architecture enforces strict regional data residency via isolated GCP regions and GKE node pools while maintaining low-latency cross-border workflows. Robust security controls, including JIT consent enforcement, envelope encryption, and cryptographic signing, ensure full HIPAA, GDPR, and EU MDR compliance.]