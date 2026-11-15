## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, compliance with GDPR and HIPAA, and local interoperability.

## Key Elements
* **Patients & Clinicians**: End-users accessing mobile and web clients.
* **API Gateway**: Cloud API Gateway routing ingress traffic.
* **EU E-Prescription Gateway**: Java / Spring Boot container for regional e-prescription integration.
* **Prescription Orchestrator**: Spring Batch/Core component managing workflow state.
* **National Adapter Engine**: Spring Integration component hosting pluggable protocol adapters.
* **Audit & Compliance Logger**: Component recording translation and dispatch actions.
* **Consent Enforcement Interceptor**: Spring Security / Aspect component validating patient consent.
* **External Pharmacy Systems**: National EU pharmacy systems using diverse standards.
* **Cloud SQL PostgreSQL & Cloud Storage**: GCP persistence layer restricted to `europe-west3`.

## Relationships
* **API Gateway -> Consent Enforcement Interceptor**: Routes EU-specific requests via gRPC over mTLS using signed JWTs.
* **Consent Enforcement Interceptor -> National Adapter Engine**: Internal dispatch after consent validation.
* **Prescription Orchestrator -> Cloud SQL PostgreSQL**: Persists region-specific data via JDBC (SQL/TCP, encrypted).
* **National Adapter Engine -> External Pharmacy Systems**: Integrates with national standards via mTLS, SOAP, and REST.

## Technology Stack
* **Java / Spring Boot**: Chosen for the EU E-Prescription Gateway due to robust enterprise integration modules (Spring Integration, Spring Batch).
* **GCP (europe-west3 & us-central1)**: Target cloud provider enforcing regional data residency.
* **gRPC / mTLS**: Used for secure inter-container communication.
* **PostgreSQL / Cloud Storage**: Persistent storage localized to regional GCP buckets and instances.

## Rationale
This architecture uses modular component decomposition within the EU E-Prescription Gateway to isolate regional data and satisfy GDPR residency constraints. Pluggable Spring Integration adapters handle heterogeneous EU pharmacy protocols while maintaining high accountability and consent enforcement.