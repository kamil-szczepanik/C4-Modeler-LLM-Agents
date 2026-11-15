## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention across a hybrid deployment.

## Key Elements
- Frontend Web App (React SPA)
- API Gateway (Nginx/Kong)
- Identity & Access Proxy (OAuth2 Proxy / Keycloak Sidecar)
- Patient & Scheduling Service (Java/Spring Boot)
- EMR Service (Node.js/TypeScript)
- Billing & Claims Service (.NET Core)
- FHIR Integration Broker (Apache Camel / Python)
- Async Message Broker (Apache Kafka / RabbitMQ)
- Audit & Compliance Log Shipper (Fluentbit / Vector)
- Databases: Patient DB (PostgreSQL) & EMR DB (MongoDB)
- Caches & Storage: Distributed Cache (Redis) & Audit Data Store (AWS S3 / MinIO WORM)

## Relationships
- Users -> Frontend Web App (HTTPS)
- Frontend Web App -> API Gateway (HTTPS)
- API Gateway -> Identity & Access Proxy (Internal gRPC)
- API Gateway -> Patient & Scheduling Service & EMR Service (gRPC)
- Services -> Async Message Broker (AMQP/TCP)
- Services -> Databases (TLS-encrypted SQL/NoSQL drivers)
- Audit & Compliance Log Shipper -> Audit Data Store (HTTPS/S3 API)
- Billing & Claims Service -> Insurance Payment Gateway (External HTTPS)
- On-Premises and AWS Kubernetes Clusters -> Istio mTLS over Site-to-Site VPN

## Technology Stack
- Kubernetes: Orchestrates containers across hybrid infrastructure for 99.99% uptime.
- PostgreSQL & MongoDB: Polyglot persistence for structured scheduling and flexible EMR payloads, with AES-256 encryption at rest.
- Apache Kafka: Event-driven decoupling for billing and FHIR synchronization.
- Redis: Sub-second EMR retrieval and session caching.
- Istio & VPN: Secure inter-cluster communication and mTLS encryption.

## Rationale
This hybrid architecture isolates sensitive patient data on-premises while leveraging cloud scalability for public ingress and integrations. Polyglot persistence, event-driven messaging, and WORM storage collectively satisfy strict HIPAA/GDPR compliance, performance, and 10-year retention constraints.