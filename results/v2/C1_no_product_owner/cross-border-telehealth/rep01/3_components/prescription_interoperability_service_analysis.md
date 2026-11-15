## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It guarantees strict regional data residency, HIPAA/GDPR compliance, and interoperability with regional health standards.

## Key Elements
- Prescription Domain Controller (Java, Spring Boot)
- FHIR Adapter Component (Java / HAPI FHIR)
- EU E-Prescription Gateway Component (Java / Apache Camel)
- Circuit Breaker / Resilience Interceptor (Resilience4j)
- Data Access Repository (Spring Data JPA)
- Consent & Audit Service (Java, Spring Boot)
- Google Cloud SQL (PostgreSQL) and Google Cloud Pub/Sub
- Istio Service Mesh, GCP KMS, GCP Secret Manager, ArgoCD

## Relationships
- Prescription Domain Controller -> Consent & Audit Service: Validates patient consent [gRPC over TLS]
- Prescription Domain Controller -> Circuit Breaker Component: Triggers dispatch [In-memory Java calls]
- Circuit Breaker Component -> FHIR Adapter & EU E-Prescription Gateway: Invokes external dispatch [Java method calls]
- FHIR Adapter -> US Pharmacies: Fulfills US prescriptions [REST over TLS 1.3 / mTLS, HL7 FHIR]
- EU E-Prescription Gateway -> National Pharmacies (EU): Fulfills EU prescriptions [Secure APIs over mTLS, national standards]
- Services -> Google Cloud SQL & Pub/Sub: Regional data persistence and DLQ [Secure local drivers and CMEK encryption]

## Technology Stack
- Java / Spring Boot: Core container framework for robust business logic
- HAPI FHIR & Apache Camel: Standardized adapters for US HL7 FHIR and EU e-prescription protocols
- Resilience4j: Circuit breaking and fault tolerance for unstable external pharmacies
- Google Cloud SQL & Pub/Sub: Regional persistence and encrypted dead-letter queues meeting data residency rules
- GCP KMS & Secret Manager: Cryptographic isolation via CMEK and secure dynamic secret injection
- Istio Service Mesh: Zero-trust mTLS service-to-service communication and distributed tracing

## Rationale
This architecture uses rigorous regional separation via ArgoCD and Spring Data JPA to ensure EU health data remains in `europe-west3` and US data in `us-central1`. Resilience4j circuit breakers, Google Cloud Pub/Sub DLQs, and Istio mTLS guarantee high availability and strict HIPAA/GDPR compliance despite unstable connections.