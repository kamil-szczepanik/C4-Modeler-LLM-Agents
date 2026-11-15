## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency clinical workflows.

## Key Elements
- **Users**: Patients, Clinic Staff/Receptionists, Clinicians/Doctors, Billing Specialists, System Administrators.
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Payment Gateway.
- **Frontend Container**: Single Page Application (React, TypeScript) served via CDN/Nginx.
- **Gateway & Mesh**: API Gateway (Kong / Envoy) and Istio Service Mesh.
- **Backend Containers**: Core Services Container, EMR Service Container, Integration Service Container, Notification Container, and Audit & Compliance Container.
- **Databases & Brokers**: PostgreSQL (AES-256), ClickHouse, and Apache Kafka.

## Relationships
- Patients & Staff -> API Gateway (HTTPS/WSS).
- API Gateway -> Core Services & EMR Containers (gRPC/REST over Istio mTLS).
- Integration Service Container -> Lab & Imaging Systems (HL7 FHIR APIs).
- All Containers -> Audit & Compliance Container (Kafka, TLS + SASL).
- Core/EMR Containers -> PostgreSQL (Encrypted connection).

## Technology Stack
- **Frontend**: React, TypeScript for responsive user interfaces.
- **Backend Core**: Go, Spring Boot, Node.js for scalable microservices.
- **Infrastructure & Mesh**: Kubernetes (on-prem-k8s, eu-central-1), Istio for mTLS and workload identity.
- **Messaging & Data**: Apache Kafka, RabbitMQ, PostgreSQL, ClickHouse.
- **Security**: OAuth2/OIDC, HashiCorp Vault, AES-256 encryption.

## Rationale
This architecture uses container isolation and service mesh mTLS to meet strict HIPAA/GDPR security mandates. Asynchronous event streaming via Kafka protects core EMR and scheduling performance, ensuring 99.99% availability and sub-second response times.