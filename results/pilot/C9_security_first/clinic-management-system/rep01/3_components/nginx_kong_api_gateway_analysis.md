## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It delivers high-availability clinical operations across hybrid cloud and on-premise infrastructure.]

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- Third-Party Lab & Imaging Systems, External Payment Gateways, Insurance Clearinghouses
- React SPA Frontend (React, CDN/Nginx)
- NGINX/Kong API Gateway (Kong, Kubernetes Ingress)
- Patient Service, Scheduling Service, EMR Service, Billing Service (Java, Spring Boot, gRPC)
- Apache Camel Integration Service (Apache Camel)
- Distributed PostgreSQL Database, Apache Kafka Event Broker (SASL/SCRAM)

## Relationships
- React SPA Frontend -> NGINX/Kong API Gateway: Sends API requests [HTTPS/WSS, OAuth2/OIDC, MFA]
- NGINX/Kong API Gateway -> Patient, Scheduling, EMR, Billing Services: Routes internal requests [gRPC, mTLS]
- EMR Service & Apache Camel -> Third-Party Lab & Imaging Systems: Interoperates [HL7 FHIR, HTTPS]
- Microservices -> Distributed PostgreSQL Database: Reads/writes encrypted data [TCP/IP, AES-256]
- Microservices -> Apache Kafka Event Broker: Publishes audit logs and events [SASL/SCRAM, TLS]

## Technology Stack
- React: Powers frontend SPA for rapid EMR screen loads (< 1s P95)
- Kong API Gateway: Handles perimeter security, WAF, routing, and JWT validation
- Java Spring Boot: Implements robust microservices for clinical business logic
- gRPC with mTLS: Provides low-latency, secure inter-service communication
- PostgreSQL: Stores encrypted patient data ensuring 10-year retention and ACID compliance
- Apache Kafka: Enables event-driven messaging and audit trailing
- Apache Camel: Facilitates HL7 FHIR interoperability with external systems

## Rationale
[This hybrid architecture utilizes active-active Kubernetes deployments and DB-less Kong edge routing to guarantee 99.99% uptime. Strict encryption, gRPC mTLS, and immutable audit logs ensure full HIPAA and GDPR compliance.]