## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for clinical environments. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and interoperability with external healthcare systems.

## Key Elements
- External Labs, Imaging Systems & Insurance Gateways
- API Gateway (NGINX/Kong)
- Identity Service (Keycloak)
- Patient, EMR, Appointment, and Billing Services (Spring Boot containers)
- HL7 FHIR Integration Engine (Apache Camel)
  - FHIR Route Orchestrator
  - Data Transformation Processor (HAPI FHIR)
  - Validation & Compliance Interceptor
  - External Protocol Adapter
- Event Broker (Apache Kafka)
- Primary Database & Tiered Storage (PostgreSQL & S3-compatible WORM)

## Relationships
- External Systems -> HL7 FHIR Integration Engine: Exchanges clinical data via mTLS and [HL7 FHIR APIs]
- HL7 FHIR Integration Engine -> Event Broker: Publishes asynchronous messages via [AMQP]
- Integration Engine -> Primary Database: Manages persistent state via [JDBC over TLS]
- Internal Microservices -> API Gateway: Routes client requests via [HTTPS/REST]

## Technology Stack
- Integration Engine: Apache Camel with HAPI FHIR libraries for parsing and transformation
- Backend Services: Java / Spring Boot containers
- Messaging & State: Apache Kafka and Redis for decoupled scaling and durability
- Database: PostgreSQL with S3-compatible WORM storage for ≥ 10-year audit retention
- Infrastructure: Kubernetes (on-prem-k8s and AWS eu-central-1) with Istio service mesh

## Rationale
This architecture uses a stateless, horizontally scalable hybrid Kubernetes design to meet 99.99% availability and high-throughput clinical performance. Dedicated security boundary isolation, AES-256 encryption, and HL7 FHIR standards guarantee strict regulatory compliance.