## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, high availability (99.99%), and a 10-year data retention policy.

## Key Elements
- API Ingress Controller (Envoy / Kong)
- Patient Portal Service, Scheduling Service, EMR Service, Billing Service
- HL7 FHIR Integration Service (Microservice / Kubernetes)
- Analytics Service (AWS eu-central-1)
- PostgreSQL Database & Apache Kafka Message Broker
- External Vault / Hardware Security Module (HSM)
- External Labs/Imaging, Insurance Clearinghouses, Payment Gateways

## Relationships
- Clinic Management System -> External Labs/Imaging: Exchanges clinical data [HL7 FHIR REST APIs, mTLS]
- HL7 FHIR Integration Service -> Apache Kafka: Streams asynchronous events [gRPC, Transactional Outbox Pattern]
- Services -> PostgreSQL Database: Persists encrypted data [AES-256, TLS 1.3]

## Technology Stack
- Kubernetes: Container orchestration for microservices across on-prem and cloud
- Java / Spring Boot & HAPI FHIR / Apache Camel: Core runtime and libraries for FHIR R4 parsing and data transformation
- Apache Kafka: Event broker for reliable message streaming
- PostgreSQL: Relational database with TDE and row-level security
- Vault / HSM: Dynamic key management and encryption

## Rationale
The hybrid architecture utilizes Kubernetes and active-active topologies to achieve 99.99% availability and low-latency EMR access (<1s P95). Strict encryption standards, OAuth 2.0 SMART-on-FHIR, and transactional outbox patterns guarantee HIPAA/GDPR compliance and zero data loss.