## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMR, scheduling, and billing for medium-sized clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and strict interoperability via HL7 FHIR APIs.

## Key Elements
- **Users**: Patient / User, Clinician / Staff, Hospital Administrator
- **External Systems**: Identity Provider (IdP), External Lab & Imaging Systems, Insurance Payment Gateways, SMS / Notification Gateway, Regulatory Compliance Authority
- **Containers**: API Gateway (Envoy), Web Application (React / TypeScript), Core Clinic Service (Java / Spring Boot), Scheduling Service (Go), Billing Service (Node.js), Integration Service (Apache Camel / Spring Integration), Event Broker (Apache Kafka / RabbitMQ), PostgreSQL Database (PostgreSQL with AES-256), Redis Cache (Redis)
- **API Gateway Components**: Listener & TLS Termination, Auth & Authz Filter, Rate Limiting & Throttling Component, Routing & Load Balancing Component, Audit Logging & Telemetry Filter

## Relationships
- **Web Application -> API Gateway**: Sends web traffic and API requests [HTTPS / WSS]
- **API Gateway -> Core Clinic / Scheduling / Billing / Integration Services**: Routes requests [gRPC over mTLS]
- **API Gateway -> Identity Provider (IdP)**: Validates JWTs [HTTPS]
- **Integration Service -> External Lab & Imaging Systems**: Exchanges healthcare data [HL7 FHIR APIs]
- **Services -> PostgreSQL Database**: Persists encrypted data [SQL over TLS / AES-256]

## Technology Stack
- **Envoy**: Chosen for API Gateway to provide native gRPC-web support, dynamic xDS configs, and advanced telemetry.
- **Java / Spring Boot**: Powers Core Clinic Service for robust enterprise reliability.
- **Go**: Used for Scheduling Service to ensure low-latency resource clash checks.
- **Node.js**: Powers Billing Service for rapid asynchronous transaction handling.
- **PostgreSQL**: Used for relational data storage with AES-256 encryption at rest.
- **Apache Kafka / RabbitMQ**: Handles asynchronous messaging for high availability.

## Rationale
This architecture uses active-active hybrid cloud deployment and strict cryptographic controls to meet high availability (99.99%) and HIPAA/GDPR compliance mandates. Microservices communicate via gRPC over mTLS to achieve sub-second P95 performance and seamless clinical interoperability.