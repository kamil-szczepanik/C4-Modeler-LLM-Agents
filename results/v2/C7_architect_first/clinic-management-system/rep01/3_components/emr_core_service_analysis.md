## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, 10-year data retention, and strict HIPAA/GDPR compliance across a hybrid Kubernetes cloud architecture.

## Key Elements
- **EMR Core Service**: Java/Spring Boot container handling clinical data processing.
- **EMR Controller Component**: Spring MVC component exposing RESTful endpoints via HTTPS/JSON.
- **Clinical Data Processing Component**: Enforces clinical business logic and emergency break-glass overrides.
- **Break-Glass Interceptor Sub-component**: Validates multi-factor emergency override tokens.
- **Persistence & Audit Repository Component**: Spring Data JPA/Hibernate interface with PostgreSQL utilizing RLS and AES-256 encryption.
- **FHIR Event Publisher Component**: Spring Cloud Stream with Apache Kafka for asynchronous clinical updates.
- **Infrastructure**: Istio Service Mesh, HashiCorp Vault, WORM storage tier, and Prometheus monitoring.

## Relationships
- **API Gateway / Edge Proxy -> EMR Core Service**: Routes client requests securely via mTLS/gRPC.
- **EMR Controller -> Clinical Data Processing**: Delegates requests using direct local method calls.
- **Clinical Data Processing -> Persistence & Audit Repository**: Reads and writes records via TLS/SQL with Row-Level Security.
- **Clinical Data Processing -> FHIR Event Publisher**: Publishes events asynchronously using Spring ApplicationEventPublisher.
- **FHIR Event Publisher -> FHIR Interoperability Service**: Broadcasts clinical updates via Apache Kafka with dynamic Vault tokens.

## Technology Stack
- **Java / Spring Boot**: Core container framework chosen for enterprise reliability and high-performance throughput.
- **PostgreSQL**: Primary data store utilizing AES-256 encryption at rest and Row-Level Security for compliance.
- **Apache Kafka / Spring Cloud Stream**: Asynchronous event backbone for decoupled FHIR interoperability messaging.
- **Istio Service Mesh**: Secures service-to-service communication via mTLS, SPIFFE IDs, and circuit breakers.
- **HashiCorp Vault**: Manages envelope encryption keys, WORM storage secrets, and dynamic Kafka tokens.

## Rationale
This architecture uses a containerized, event-driven microservices pattern deployed on hybrid Kubernetes to achieve 99.99% availability and sub-second P95 latencies. Strict security controls like mTLS, PHI masking, and tamper-proof WORM audit logging ensure full HIPAA and GDPR compliance.