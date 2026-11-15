## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability (99.99%), strict data retention, and HIPAA/GDPR compliance across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- API Gateway / BFF Container (Kong / Envoy)
- EMR Service Container (Java / Spring Boot)
- Scheduling Service Container (Node.js / TypeScript)
- Billing Service Container (Go)
- Integration Service Container (Apache Camel / FHIR Server)
- Clinical Database (PostgreSQL)
- Audit & Observability Sidecar (FluentBit / Prometheus)
- Internal EMR Components: EMR API Controller Component, Security & Compliance Policy Component, Clinical Record Domain Component, Audit Trail Interceptor Component

## Relationships
- Patient Portal -> API Gateway / BFF Container (HTTPS/REST)
- Identity Provider -> API Gateway / BFF Container (OIDC/SAML 2.0)
- API Gateway / BFF Container -> EMR Service Container (gRPC over mTLS)
- EMR API Controller Component -> Security & Compliance Policy Component (In-memory method calls)
- Security & Compliance Policy Component -> Clinical Record Domain Component (In-memory method calls)
- Clinical Record Domain Component -> Clinical Database (JDBC via TLS 1.3)
- Audit Trail Interceptor Component -> Notification Gateway (HTTPS/REST)

## Technology Stack
- Java / Spring Boot: Chosen for the EMR Service Container to provide robust enterprise features and sub-second P95 performance.
- PostgreSQL: Serves as the Clinical Database, providing reliable ACID transactions with AES-256 encryption at rest.
- Spring Security & AspectJ: Used for RBAC/ABAC enforcement and non-invasive audit logging.
- FluentBit / Prometheus: Powers the Audit & Observability Sidecar for metrics collection and tamper-evident logging.

## Rationale
This architecture combines Spring Boot's enterprise reliability with strict hybrid-cloud security measures to meet sub-second EMR load times and 99.99% availability targets. Modular internal components and encrypted auditing guarantee compliance with HIPAA and GDPR mandates without sacrificing performance.