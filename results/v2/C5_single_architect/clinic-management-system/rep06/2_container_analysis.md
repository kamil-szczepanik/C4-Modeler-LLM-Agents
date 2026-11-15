## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- **Users**: Patient / User, Clinician / Staff, Hospital Administrator
- **API Gateway**: NGINX / Envoy proxy handling TLS termination, rate limiting, and JWT validation
- **Web Application**: React / TypeScript Single Page Application served via NGINX
- **Core Clinic Service**: Java / Spring Boot service managing patient registration and EMR audit trails
- **Scheduling Service**: Go service handling appointment scheduling and resource clash checks
- **Billing Service**: Node.js service managing billing and insurance claim submissions
- **Integration Service**: Apache Camel / Spring Integration handling HL7 FHIR translations
- **Event Broker**: Apache Kafka / RabbitMQ for asynchronous domain events
- **Datastores**: PostgreSQL (transactional data with AES-256) and Redis (scheduling locks)
- **External Systems**: Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), SMS / Notification Gateway, Regulatory Compliance / Auditing Authority

## Relationships
- **Web Application** to **API Gateway**: HTTPS / WSS
- **API Gateway** to **Core, Scheduling, Billing, & Integration Services**: gRPC over mTLS
- **Core Clinic Service & Billing Service** to **Event Broker**: AMQP / Kafka protocol for asynchronous events
- **Integration Service** to **External Lab & Imaging Systems**: HL7 FHIR over HTTPS
- **Billing Service** to **Insurance Payment Gateways**: HTTPS

## Technology Stack
- **API Gateway**: NGINX / Envoy for secure, high-performance ingress routing
- **Frontend**: React / TypeScript for responsive user interfaces
- **Backend Services**: Java / Spring Boot (Core), Go (Scheduling), Node.js (Billing) for domain-specific performance and scalability
- **Integration**: Apache Camel / Spring Integration for HL7 FHIR interoperability
- **Messaging**: Apache Kafka / RabbitMQ for decoupled, event-driven workflows
- **Databases**: PostgreSQL with AES-256 encryption at rest; Redis for high-speed caching and locking
- **Deployment**: Hybrid cloud across on-premise Kubernetes and AWS (`eu-central-1`) in an active-active topology

## Rationale
This architecture uses an active-active hybrid deployment model across on-premises Kubernetes and AWS to guarantee 99.99% uptime and low-latency access. Microservices communicating via gRPC over mTLS and Apache Kafka, combined with PostgreSQL AES-256 encryption, strictly fulfill HIPAA/GDPR security, interoperability (HL7 FHIR), and high-performance requirements.