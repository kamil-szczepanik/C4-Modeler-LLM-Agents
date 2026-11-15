## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability (99.99%), strict regulatory compliance, and seamless clinical interoperability.

## Key Elements
- Hospital Staff (Users)
- Patient Portal, External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Regulatory Audit System
- API Gateway & Edge Router (Kong/Envoy)
- Web Application Frontend (React SPA, Nginx)
- Patient Service, Scheduling Service, EMR Service, Billing Service (Spring Boot, Kubernetes)
- Integration Service (Apache Camel/Node.js) featuring FHIR Translator, Message Router, and mTLS Client components
- Data Persistence Layer (PostgreSQL with AES-256 and HSM-managed column encryption)
- Message Broker Container (Geo-local Apache Kafka clusters with MirrorMaker)

## Relationships
- Integration Service -> External Lab & Imaging Systems: Exchanges clinical data securely [HTTPS / mTLS / HL7 FHIR REST API with Resilience4j Circuit Breaker]
- Message Router -> Message Broker: Consumes and publishes integration events [Kafka Protocol / TCP with Kafka Topic ACLs]
- Message Router -> FHIR Translator: Dispatches raw integration events [Internal Direct Route with W3C Trace Context]
- Web Application Frontend -> API Gateway: Routes client requests [HTTPS / REST / OAuth2]

## Technology Stack
- Apache Camel: Provides enterprise integration patterns for complex FHIR R4 mapping
- Apache Kafka: Enables geo-distributed event streaming with MirrorMaker and consumer lag scaling
- Spring Boot: Powers microservices containers on Kubernetes
- PostgreSQL & HSM: Ensures secure, encrypted data storage meeting HIPAA/GDPR constraints
- HashiCorp Vault / cert-manager: Automates mTLS certificate rotation for hybrid infrastructure
- Resilience4j: Implements circuit breaking for external integrations

## Rationale
This architecture uses microservices and event-driven messaging to achieve 99.99% active-active uptime and sub-second EMR performance. Robust security controls, FHIR standards, and automated hybrid infrastructure ensure full HIPAA and GDPR compliance.