## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across hybrid environments.

## Key Elements
* Patients, Doctors, Nurses, and Administrative Staff
* Global Traffic Manager / WAF
* API Gateway (Envoy)
* Identity & Access Management (Keycloak)
* Core Services (Node.js / Spring Boot)
* FHIR Interoperability Engine (HAPI FHIR / Apache Camel)
* Regional Databases (PostgreSQL / CockroachDB)
* SIEM & Audit Platform

## Relationships
* Patients, Doctors, Nurses, Administrative Staff -> API Gateway: Accesses clinical workflows via [HTTPS / TLS / OAuth2/OIDC]
* Global Traffic Manager / WAF -> API Gateway: Routes external traffic via [HTTPS] with mTLS attestation
* API Gateway -> Identity & Access Management: Validates JWT tokens and validates scopes via [OAuth2/OIDC]
* API Gateway -> Core Services: Routes ingress traffic via [gRPC over mTLS] with circuit breaking
* API Gateway -> FHIR Interoperability Engine: Routes lab and imaging API calls via [gRPC / mTLS]
* API Gateway -> SIEM & Audit Platform: Exports scrubbed access logs and OpenTelemetry metrics via [OTLP / HTTPS]

## Technology Stack
* Envoy: Selected as API Gateway for gRPC-web support, native tracing, and fine-grained rate-limiting filters.
* Keycloak: Handles IAM, token validation, and OAuth2 introspection.
* PostgreSQL / CockroachDB: Regional databases ensuring active-active replication and high availability.
* OpenTelemetry: Emits spans and traces for latency tracking.

## Rationale
This hybrid architecture uses Envoy and multi-region deployment to meet stringent 99.99% availability and <1s P95 performance SLAs. Strict mTLS, JWT scope validation, and log-scrubbing ensure full HIPAA and GDPR compliance.