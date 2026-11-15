## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR, and HIPAA compliance on GCP.

## Key Elements
- Patients & Clinicians (Users)
- Flutter / TypeScript Mobile/Web App
- GCP Cloud API Gateway
- Go / gRPC Core Telehealth Service
- LiveKit (GKE) SFU Media Server
- Python / FastAPI AI Inference Wrapper
- Node.js / TypeScript **US FHIR Adapter** (comprising FHIR Router, FHIR Mapping Engine, Pharmacy Integration Client, US Persistence Repository, and Audit Logger components)
- Java / Spring Boot EU E-Prescription Gateway
- GCP Cloud SQL PostgreSQL & Cloud Storage

## Relationships
- API Gateway -> US FHIR Adapter: Routes US-specific integration requests [gRPC and HTTPS]
- FHIR Router -> FHIR Mapping Engine: Delegates transformation [In-process function calls]
- FHIR Router -> Audit Logging Component: Emits audit events [In-process event emitter]
- US Persistence Repository -> Audit Logging Component: Enforces mandatory access logging [In-process]
- US Persistence Repository -> Cloud SQL PostgreSQL & Cloud Storage: Persists US-specific data [SQL / TCP, locked to `us-central1`]
- Pharmacy Integration Client -> External Pharmacy Systems: Sends e-prescriptions [HTTPS/REST]

## Technology Stack
- Node.js / TypeScript: Selected for the US FHIR Adapter to ensure rapid development, robust typing, and seamless integration with existing services.
- NestJS: Used for the FHIR Router/Controller to provide native dependency injection and strict DTO validation.
- GCP Cloud SQL PostgreSQL: Stores regional health data securely with strict geographic isolation (`us-central1` and `europe-west3`).

## Rationale
This component architecture enforces strict regional data residency and HIPAA compliance by isolating US operations within `us-central1`. The internal modularity of the US FHIR Adapter ensures reliable interoperability via HL7 FHIR standards while maintaining immutable audit trails.