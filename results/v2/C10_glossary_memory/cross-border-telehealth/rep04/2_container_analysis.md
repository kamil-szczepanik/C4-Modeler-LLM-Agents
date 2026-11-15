## Overview
[Cross-Border Telehealth Platform] is a secure telehealth system delivering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance using GCP regions `europe-west3` and `us-central1`.

## Key Elements
- Patients [person, context]
- Licensed Clinicians [person, context]
- Pharmacies [externalSystem, context]
- External Pharmacies [externalSystem, context]
- Regional Identity & Consent Providers [externalSystem, context]
- AI Model Providers / Medical Devices [externalSystem, context]
- Patient Web/Mobile App [container]
- Clinician Portal [container]
- API Gateway & Routing Service [container]
- Core Telehealth Service [container]
- E-Prescription Interoperability Service [container]
- AI Symptom Checker Service [container]
- Database Cluster [container]

## Relationships
- Patients -> Cross-Border Telehealth Platform via HTTPS / WebSockets (adaptive codec)
- Licensed Clinicians -> Cross-Border Telehealth Platform via HTTPS
- Cross-Border Telehealth Platform -> External Pharmacies via TLS / Mutual TLS
- Cross-Border Telehealth Platform -> AI Model Providers / Medical Devices via HTTPS (REST/gRPC with payload masking)
- Cross-Border Telehealth Platform -> Regional Identity & Consent Providers via OAuth2 / OpenID Connect

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`
- Flutter / React Native: Powers the Patient Web/Mobile App with local state caching for unstable connections
- React SPA: Powers the Clinician Portal
- Envoy Proxy / Istio: Manages API gateway routing, Istio service mesh mTLS, and Canary deployments
- Node.js / Go: Powers the Core Telehealth Service handling consultations and consent
- Spring Boot / Apache Camel: Powers the E-Prescription Interoperability Service translating HL7 FHIR and national EU standards
- Python / FastAPI: Powers the AI Symptom Checker Service with local PII/PHI masking
- Cloud Spanner / PostgreSQL: Regional data stores secured with Google Cloud KMS CMEK
- GKE & WebRTC SFU: Container orchestration and adaptive bitrate video streaming

## Rationale
The architecture strictly enforces GDPR and HIPAA via regional GCP isolation (`europe-west3` and `us-central1`) and Envoy/Istio security controls. Containerized microservices ensure high availability under unstable internet connections and maintain strict traceability for AI medical device compliance.