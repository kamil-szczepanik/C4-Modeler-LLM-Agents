## Overview
The Clinic Management System manages patient admissions, EMR, scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability, HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
- **Actors**: Clinicians, External Lab Technicians, Hospital Administrators, Receptionists/Front Desk, Billing Specialists, Patients
- **Containers**: Frontend SPAs (React, Nginx), Envoy API Gateway, Domain Microservices (Spring Boot, Kubernetes, Istio), Integration Service (Node.js), Decoupled Data Tier (AWS RDS PostgreSQL, WORM Storage)
- **Integration Service Components**: FHIR Adapter (NestJS/TypeScript), Outbox Message Relay (BullMQ/Redis), Audit Logger (Winston/OpenTelemetry), DLQ Alert Dispatcher (NestJS Event Emitter)
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)

## Relationships
- *Frontend SPAs* -> *Envoy API Gateway*: HTTPS/WSS [REST/GraphQL]
- *Envoy API Gateway* -> *Domain Microservices*: gRPC / HTTPS [Internal API]
- *FHIR Adapter* -> *External Lab & Imaging Systems*: REST/HTTPS [HL7 FHIR with mTLS and OAuth2]
- *Domain Microservices* -> *Outbox Message Relay*: AMQP / Kafka
- *Outbox Message Relay* -> *FHIR Adapter*: Internal Function Call / Event Dispatch
- *Outbox Message Relay* -> *DLQ Alert Dispatcher*: Internal Event [Pub/Sub]
- *DLQ Alert Dispatcher* -> *Internal Notification Service*: REST/gRPC [Internal API]

## Technology Stack
- **Integration Service**: Node.js / NestJS / TypeScript for scalable asynchronous event processing
- **Message Broker & Queue**: Redis and BullMQ for reliable outbox pattern execution and dead-letter queueing
- **Infrastructure & Mesh**: Kubernetes (on-prem-k8s and AWS eu-central-1) with Istio service mesh for mTLS and traffic management
- **Security & Logging**: HashiCorp Vault for secrets management, Winston and OpenTelemetry for audit logging, AES-256 for data at rest

## Rationale
This architecture guarantees 99.99% uptime and strict HIPAA/GDPR compliance through active-active hybrid deployments and encrypted data handling. Decoupled microservices and robust outbox patterns eliminate data loss during external lab communications, safeguarding patient safety and operational efficiency.