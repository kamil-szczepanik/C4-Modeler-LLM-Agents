## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to securely manage patient admissions, EMRs, scheduling, and billing. It provides high availability, strict HIPAA/GDPR compliance, and interoperability via FHIR APIs.

## Key Elements
- **Frontend Web App**: React SPA for user interaction
- **API Gateway**: Kong / Nginx entry point handling inbound routing and security
- **Identity & Access Proxy**: OAuth2 Proxy / Keycloak Sidecar for authentication
- **Domain Services**: Patient & Scheduling Service (Java/Spring Boot), EMR Service (Node.js/TypeScript), Billing & Claims Service (.NET Core)
- **Integration Broker**: Apache Camel / Python for HL7 FHIR APIs
- **Databases & Storage**: PostgreSQL (Patient DB), EMR DB (MongoDB), Redis (Distributed Cache), AWS S3 / MinIO WORM (Audit Data Store)
- **Messaging & Logging**: Apache Kafka / RabbitMQ (Async Broker), Fluentbit / Vector (Log Shipper)

## Relationships
- **Frontend Web App** -> **API Gateway**: Client requests [HTTPS]
- **API Gateway** -> **Identity & Access Proxy**: Authentication [Internal gRPC]
- **API Gateway** -> **Domain Services**: Traffic routing [gRPC / HTTP/2]
- **API Gateway** -> **Audit & Compliance Log Shipper**: Access log streaming [Fluentbit/Syslog]
- **FHIR Integration Broker** -> **External Labs & Imaging Systems**: Interoperability [HL7 FHIR REST APIs]

## Technology Stack
- **Kong / Nginx**: API Gateway and core proxying for robust traffic management and TLS 1.3 termination
- **Java, Node.js, .NET Core**: Polyglot microservices tailored to specific domain performance and data needs
- **PostgreSQL & MongoDB**: Relational and document databases optimized for structured patient data and flexible EMR records
- **Apache Kafka**: Asynchronous message broker ensuring decoupled, high-throughput communication

## Rationale
This hybrid microservices architecture ensures 99.99% high availability via active-active deployment and containerized redundancy. Strict security controls, AES-256 encryption, and dedicated audit logging satisfy mandatory HIPAA and GDPR compliance regulations.