## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers in a hybrid cloud environment. The architecture ensures HIPAA and GDPR compliance, high availability (99.99%), and robust audit tracking.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- Hybrid API Gateway (Kong / Envoy)
- EMR Service Container (Java / Spring Boot)
- Scheduling Service Container (Node.js / TypeScript)
- Billing Service Container (Go)
- Integration Service Container (Apache Camel / FHIR Server)
- Clinical Database (PostgreSQL)
- Audit & Observability Sidecar (FluentBit / Prometheus)
- Secure WORM Storage & Central Observability Platform

## Relationships
- Patient Portal -> API Gateway / BFF Container (HTTPS/REST)
- Lab & Imaging Systems -> Integration Service Container (HL7 FHIR over HTTPS)
- Insurance Payment Gateway -> Billing Service Container (TLS 1.3)
- Identity Provider -> API Gateway / BFF Container (OIDC/SAML 2.0)
- API Gateway / BFF Container -> Backend Containers (gRPC over mTLS)
- EMR Service Container -> Clinical Database (TLS 1.3)
- Audit & Observability Sidecar -> Secure WORM Storage (HTTPS/TLS 1.3 with Object Lock)

## Technology Stack
- Kong / Envoy: Ingress routing, TLS termination, and WAF protection.
- Java / Spring Boot & Node.js / TypeScript: Resilient clinical and scheduling microservices.
- Go: High-performance billing and claim processing.
- PostgreSQL: Distributed clinical database with AES-256 and field-level encryption.
- FluentBit / Prometheus: Tamper-evident logging, PII sanitization, and metrics collection.

## Rationale
This hybrid architecture uses secure containerization and strict cryptographic controls to satisfy strict HIPAA and GDPR mandates. Active-active high availability and gRPC over mTLS communication ensure sub-second performance for critical clinical workflows.