## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent security controls, and strict compliance with HIPAA and GDPR mandates.

## Key Elements
- Front-Desk Receptionists
- Clinicians
- Billing Specialists
- IT/Compliance Administrators
- Patients
- Lab & Imaging Systems
- Insurance Clearinghouses
- Identity Provider (IdP)
- Patient Portal / Mobile App
- Unified API Gateway
- Patient Registration Microservice (Spring Boot)
  - Registration Controller (Spring MVC)
  - Patient Matching Engine (Java / Algorithms)
  - Eligibility Verification Service (Spring Cloud OpenFeign)
  - Eligibility Circuit Breaker Wrapper (Resilience4j)
  - Audit & Compliance Interceptor (Spring AspectJ)
  - Registration Data Repository (Spring Data JPA)
- EMR Microservice (Go / gRPC)
- Scheduling Microservice (Spring Boot)
- Billing Microservice (Node.js / Express)
- Async Claims Processing Worker (Background Worker)
- Message Broker (Apache Kafka)
- Distributed Cache (Redis Enterprise)
- Cloud-Native Distributed SQL Database (CockroachDB)

## Relationships
- Patient Portal / Mobile App -> Unified API Gateway (HTTPS / REST and WebSocket via OIDC/OAuth 2.0)
- Front-Desk Receptionists -> Unified API Gateway (HTTPS / REST)
- Clinicians -> Unified API Gateway (HTTPS / REST)
- Billing Specialists -> Unified API Gateway (HTTPS / REST)
- IT/Compliance Administrators -> Unified API Gateway (HTTPS / REST)
- Unified API Gateway -> Patient Registration Microservice (HTTP / REST)
- Registration Controller -> Patient Matching Engine (In-Memory Method Call)
- Registration Controller -> Eligibility Circuit Breaker Wrapper (In-Memory Method Call)
- Eligibility Circuit Breaker Wrapper -> Eligibility Verification Service (HTTPS / JSON with Circuit Breaker)
- Registration Controller -> Audit & Compliance Interceptor (AOP / AspectJ)
- Audit & Compliance Interceptor -> Registration Data Repository (JDBC / TLS)
- Registration Controller -> Registration Data Repository (JDBC / TLS)
- Registration Data Repository -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Unified API Gateway -> EMR Microservice (gRPC)
- Unified API Gateway -> Scheduling Microservice (HTTP / REST)
- Unified API Gateway -> Billing Microservice (HTTP / REST)
- EMR Microservice -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Scheduling Microservice -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Billing Microservice -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Billing Microservice -> Message Broker (Apache Kafka Protocol)
- Async Claims Processing Worker -> Message Broker (Apache Kafka Protocol)
- Clinic Management System -> Lab & Imaging Systems (HL7 FHIR over HTTPS)
- Clinic Management System -> Insurance Clearinghouses (Secure EDI / HTTPS APIs)
- Clinic Management System -> Identity Provider (IdP) (OIDC/SAML 2.0 over HTTPS)
- on-prem-k8s -> eu-central-1 (Encrypted IPsec site-to-site VPN and mutual TLS)

## Technology Stack
- Spring Boot: Implements Java-based microservices for patient registration and scheduling.
- Go: Powers high-performance EMR microservices via gRPC.
- Node.js / Express: Handles billing microservices and integrations.
- CockroachDB: Provides active-active distributed SQL storage with Raft consensus.
- Apache Kafka: Enables asynchronous, non-blocking claims processing messaging.
- Redis Enterprise: Delivers distributed session caching and message brokering.
- HashiCorp Vault: Secures and manages external API credentials.
- Istio: Enforces mutual TLS (mTLS) and service-to-service security within Kubernetes.

## Rationale
This architecture uses an active-active hybrid cloud model with CockroachDB and resilient microservices to guarantee 99.99% availability and low-latency performance. Strict component isolation, AES-256 encryption, and immutable audit trails ensure full compliance with HIPAA and GDPR mandates.