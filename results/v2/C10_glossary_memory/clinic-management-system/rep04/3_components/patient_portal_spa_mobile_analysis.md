## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA and GDPR compliance while maintaining 99.99% availability and supporting high-performance clinical workflows.

## Key Elements
- **Patients, Clinicians, Billing/Admin Staff, Compliance Officer** (Human Actors)
- **Lab & Imaging Systems, Insurance Clearinghouse / External Billing Provider** (External Systems)
- **Patient Portal SPA/Mobile, Clinician/Admin Workspace SPA** (React/TypeScript Frontends)
- **API Gateway / BFF** (Envoy/Kong)
- **Core Services Container** (Java/Spring Boot)
- **Billing Service Container** (Node.js/TypeScript)
- **Integration Service Container** (Apache Camel / Spring Integration)
- **Audit & Compliance Logging Container** (WORM-compliant storage / Spring Integration)
- **PostgreSQL & HL7 FHIR Compliant Data Stores** (PostgreSQL with AES-256 at rest)
- **Message Broker** (RabbitMQ/Kafka)

## Relationships
- Users -> API Gateway / BFF: HTTPS (TLS 1.3, OAuth2/OIDC, MFA)
- API Gateway / BFF -> Core Services Container / Billing Service Container: gRPC over mTLS
- Core Services Container -> PostgreSQL & HL7 FHIR Compliant Data Stores: JDBC (AES-256 at rest)
- Billing Service Container -> Message Broker: AMQP
- Integration Service Container -> Lab & Imaging Systems: HL7 FHIR over REST/JSON (TLS 1.3)
- Billing Service Container -> Insurance Clearinghouse / External Billing Provider: HTTPS / EDI X12

## Technology Stack
- **React/TypeScript:** High-performance SPAs for patient and clinician workspaces ensuring responsive UI.
- **Java/Spring Boot:** Robust domain logic execution for core clinical services.
- **Node.js/TypeScript:** Lightweight isolated handling for financial and billing services.
- **PostgreSQL:** Relational persistence with AES-256 encryption at rest for secure data storage.
- **Envoy/Kong:** API Gateway for reverse proxy, routing, and token exchange.
- **Apache Camel / Spring Integration:** Translation adapters for HL7 FHIR interoperability.
- **RabbitMQ/Kafka:** Asynchronous messaging for resilient claim submissions.

## Rationale
This hybrid architecture isolates critical clinical and financial workloads across on-premises Kubernetes and cloud regions to meet strict data retention and security mandates. Utilizing microservices with gRPC over mTLS, event-driven messaging, and HL7 FHIR integration ensures high availability (99.99%), scalability, and seamless interoperability.