## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US while enforcing strict regional data residency. It operates on Google Cloud Platform (GCP) with isolated regional deployments in `europe-west3` and `us-central1` to ensure GDPR and HIPAA compliance.

## Key Elements
* Patients [person]
* Licensed Clinicians [person]
* Compliance Officers / Auditors [person]
* Web Application Container (`React / Next.js`)
* API Gateway Container (`Envoy / GCP API Gateway`)
* Core Services Container (`Go / Node.js microservices`)
* AI Symptom Checker Container (`Python / FastAPI + Vertex AI`)
* Media Relay Container (`Janus / WebRTC SFU`)
* E-Prescription Integration Container (`Java / Spring Boot`)
* Databases (`GCP Cloud SQL for PostgreSQL`)
* EU National E-Prescription Gateways [externalSystem]
* US Pharmacy Networks (Surescripts) [externalSystem]
* Identity Providers (eIDAS / OAuth2/OIDC) [externalSystem]
* Regional Payment & Insurance Gateways [externalSystem]

## Relationships
* Patients / Licensed Clinicians -> Web Application Container (HTTPS)
* Web Application Container -> API Gateway Container (HTTPS / REST & GraphQL)
* Patients / Licensed Clinicians -> Media Relay Container (WebRTC / DTLS-SRTP, UDP)
* API Gateway Container -> Core Services Container (gRPC over mTLS)
* API Gateway Container -> AI Symptom Checker Container (gRPC over mTLS)
* Core Services Container -> E-Prescription Integration Container (gRPC over mTLS)
* Core Services Container -> Databases (TCP / SSL)
* E-Prescription Integration Container -> EU National E-Prescription Gateways / US Pharmacy Networks (HTTPS / mTLS / HL7 FHIR)

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud provider ensuring regional isolation and data residency.
* Google Kubernetes Engine (GKE) with Istio: Container orchestration and service mesh providing mandatory mTLS for internal interconnects.
* Janus SFU: WebRTC Selective Forwarding Unit providing dynamic adaptive bitrate streaming for low-bandwidth rural connections.
* Python / FastAPI + Vertex AI: AI framework for processing symptom inputs and generating traceable, versioned recommendations.
* GCP Cloud SQL for PostgreSQL: Relational database secured via Cloud KMS Customer-Managed Encryption Keys (CMEK).

## Rationale
This architecture uses isolated regional GCP deployments to strictly satisfy GDPR and HIPAA data residency mandates. Furthermore, the integration of dedicated media relays and gRPC over mTLS guarantees low-bandwidth video resilience and secure cross-border interoperability.