## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and interoperability with regional pharmacy standards.

## Key Elements
- Clinical Core Component (Java, Spring Boot)
- Prescription Workflow Orchestrator (Java, Spring Boot / Temporal SDK)
- FHIR US Adapter Component (Java, Spring Boot / HAPI FHIR)
- EU e-Prescription Adapter Component (Java, Spring Boot)
- Consent Enforcer Component (Java, Spring Boot / Interceptor)
- Cloud SQL (PostgreSQL with GCP CMEK)
- Regional Message Broker (GCP Pub/Sub)
- National e-Prescription Gateways (EU) and US Pharmacy Systems

## Relationships
- Clinical Core Component -> Consent Enforcer Component: Validates patient consent [In-process Java method call]
- Clinical Core Component -> Cloud SQL: Reads and writes clinical data [JDBC, PostgreSQL Protocol / KMS]
- Prescription Workflow Orchestrator -> EU e-Prescription Adapter / FHIR US Adapter: Delegates external transmissions [gRPC]
- EU e-Prescription Adapter / FHIR US Adapter -> National Gateways & Pharmacy Systems: Transmits prescriptions [REST/gRPC, HL7 FHIR over mTLS]

## Technology Stack
- Java & Spring Boot: Chosen for enterprise reliability and robust ecosystem support in core clinical services
- Temporal SDK: Provides durable execution and resilient retries for unreliable external pharmacy endpoints
- HAPI FHIR: Facilitates standards-compliant HL7 FHIR data translation for US interoperability
- GCP Cloud SQL & CMEK: Ensures region-isolated data storage with strict cryptographic boundaries
- OpenTelemetry: Enables distributed tracing across regional services

## Rationale
Strict regional infrastructure separation in GCP (`europe-west3` and `us-central1`) guarantees that EU and US health data never cross borders, fulfilling GDPR and HIPAA mandates. In-process consent enforcement and resilient workflow orchestration ensure high availability and accountability even under adverse network conditions.