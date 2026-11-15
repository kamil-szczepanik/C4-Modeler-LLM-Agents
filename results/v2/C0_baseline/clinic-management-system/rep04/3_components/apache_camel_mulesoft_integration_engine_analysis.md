## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient administration, EMRs, and billing. It provides high availability, stringent compliance, and seamless interoperability.

## Key Elements
- Patients, Clinic Staff, Clinicians, Billing Specialists, Hospital Administrators
- Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway
- Kong/Envoy API Gateway, React SPA, Patient Portal BFF
- Core Services (Java/Spring Boot), Billing Service
- Apache Camel/MuleSoft Integration Engine (FHIR Transformer, Routing Router, DLQ Handler, Audit Interceptor)
- Apache Kafka Event Stream, PostgreSQL, Redis Enterprise, WORM Object Storage

## Relationships
- Patients & Staff -> Kong/Envoy API Gateway [HTTPS/TLS]
- Kong/Envoy -> React SPA & Patient Portal BFF [HTTPS/TLS]
- Core Services -> Apache Camel/MuleSoft Integration Engine [gRPC/REST over TLS]
- Apache Camel/MuleSoft Integration Engine -> External Lab & Imaging Systems [HL7 FHIR APIs over mTLS]
- Apache Camel/MuleSoft Integration Engine -> WORM Object Storage [S3 API over TLS]

## Technology Stack
- Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1): Ensures high availability (99.99%) across environments.
- Apache Camel / MuleSoft: Powers HL7 FHIR clinical data translations and integration routing.
- Apache Kafka: Event streaming and Dead Letter Queue (DLQ) handling.
- PostgreSQL & Redis Enterprise: High-performance transactional persistence and caching.
- AES-256 and JWE: Secures data at rest and encrypts DLQ payloads for HIPAA/GDPR compliance.

## Rationale
This architecture uses active-active hybrid cloud deployment to guarantee the 99.99% availability required for clinical operations. Decoupled integration and storage layers ensure strict HIPAA/GDPR compliance, a 10-year data retention audit trail, and robust interoperability via HL7 FHIR.