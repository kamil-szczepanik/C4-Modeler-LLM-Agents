## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient records, scheduling, billing, and clinical workflows. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance for critical medical data.

## Key Elements
- **Users**: Patients, Clinicians, and Hospital Administrators
- **External Systems**: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateways, and Insurance Clearinghouses
- **API Gateway & Resilience**: Kong/Nginx gateway with Envoy sidecar circuit breakers and bulkheads
- **Core Microservices**: Patient Portal Service, Patient & Scheduling Service, EMR Service, Billing Service, and Integration Service
- **Data & Messaging**: PostgreSQL databases with read replicas, Apache Kafka event broker, and HashiCorp Vault for secrets management
- **Infrastructure**: Hybrid deployment spanning on-premise Kubernetes and AWS `eu-central-1` with Falco runtime security

## Relationships
- Users & External Systems -> (HTTPS/REST/GraphQL/mTLS) -> API Gateway
- API Gateway -> (gRPC / Internal Mesh with mTLS) -> Microservices (Patient Portal, Scheduling, EMR, Billing, Integration)
- Microservices -> (TCP / TLS) -> PostgreSQL Databases & Apache Kafka Event Broker
- Integration Service -> (HL7 FHIR APIs) -> External Lab & Imaging Systems
- Billing Service -> (HTTPS) -> Payment Gateways & Insurance Clearinghouses

## Technology Stack
- **API Gateway / Mesh**: Kong, Nginx, and Envoy sidecars for routing, mTLS, and circuit breaking
- **Backend Services**: Node.js/TypeScript (Patient/Scheduling), Java/Spring Boot (EMR), Python/FastAPI (Billing), Apache Camel (Integration)
- **Data & Messaging**: PostgreSQL with read replicas, Apache Kafka for event-driven asynchronous processing
- **Security & Infrastructure**: HashiCorp Vault, AWS KMS with on-prem HSM, Falco runtime monitoring, Kubernetes (on-prem and AWS `eu-central-1`)

## Rationale
The hybrid microservices architecture ensures 99.99% availability and active-active resilience across on-premise and cloud environments. Strict isolation patterns, AES-256 encryption, and local-cache fallbacks protect patient safety, clinical continuity, and regulatory compliance under all network conditions.