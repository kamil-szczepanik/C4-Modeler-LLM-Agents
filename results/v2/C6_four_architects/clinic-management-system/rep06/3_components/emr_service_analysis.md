## Overview
The Clinic Management System is a hybrid cloud-based healthcare platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing while ensuring strict HIPAA/GDPR compliance and 99.99% availability. It provides secure, interoperable clinical workflows for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Doctor, Nurse, Receptionist, Billing Officer, Patient, Regulatory/Audit Authority
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, Hospital Notification/SMS Gateway
- **Containers**: Frontend Web App (React SPA), API Gateway (Nginx/Kong), Identity & Access Proxy (OAuth2 Proxy/Keycloak Sidecar), Patient & Scheduling Service (Java/Spring Boot), EMR Service (Node.js/TypeScript), Billing & Claims Service (.NET Core), FHIR Integration Broker (Apache Camel/Python), Async Message Broker (Apache Kafka/RabbitMQ), Audit & Compliance Log Shipper (Fluentbit/Vector), Patient DB (PostgreSQL), EMR DB (MongoDB), Distributed Cache (Redis), Audit Data Store (AWS S3/MinIO WORM)
- **EMR Service Components**: EMR API Controller (Express.js/NestJS), Clinical Record Manager, FHIR Transformer Component, Data Access Repository, Audit Event Dispatcher, Cache-Aside Manager, Field-Level Encryption (FLE) Interceptor, Telemetry & Health Probe Interceptor

## Relationships
- API Gateway -> EMR Service: Routes gRPC requests [gRPC]
- EMR Service -> Async Message Broker: Publishes/consumes events [AMQP/TCP]
- EMR Service -> EMR DB: Reads/writes EMR payloads [TLS-encrypted NoSQL driver]
- EMR Service -> Distributed Cache: Retrieves cached EMR data [Redis Protocol over TLS]
- Clinical Record Manager -> FHIR Transformer: Converts records for external sync [In-memory]
- Data Access Repository -> FLE Interceptor: Encrypts/decrypts PHI payloads [In-memory middleware]
- Telemetry Interceptor -> Async Message Broker: Propagates trace context [AMQP headers]

## Technology Stack
- Node.js & TypeScript: Powers the EMR Service for asynchronous, high-performance execution.
- MongoDB: Stores flexible EMR document payloads.
- Redis: Provides distributed caching to ensure EMR screen load times are under 1 second.
- Apache Kafka / RabbitMQ: Handles reliable asynchronous messaging and event distribution.
- OpenTelemetry: Ensures distributed tracing and observability across microservices.

## Rationale
This architecture uses a hybrid cloud deployment and decoupled microservices to achieve high availability (99.99%) and rapid response times. Integrated security features like field-level encryption and immutable audit logging natively satisfy strict HIPAA and GDPR mandates.