## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It ensures high availability, 10-year data retention, and strict compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Practitioners, Administrators
- API Gateway Container
- Core Domain & Read-Model Containers
- Background Worker Container
- Integration / Adapter Container
- Asynchronous Message Broker (Kafka/RabbitMQ)
- Centralized Audit Logging Service

## Relationships
- Users -> API Gateway Container: Accesses system via HTTPS/MFA [TLS 1.3]
- API Gateway Container -> Core Domain Containers: Routes requests [gRPC/REST]
- Core Domain Containers -> Asynchronous Message Broker: Publishes events [AMQP/Kafka Protocol]
- Asynchronous Message Broker -> Background Worker Container: Consumes asynchronous tasks [Kafka/RabbitMQ]
- Background Worker Container -> Centralized Audit Logging Service: Sends scrubbed audit logs [HTTPS/TLS]

## Technology Stack
- Kubernetes (on-prem-k8s & AWS eu-central-1): Enables active-active 99.99% availability and Horizontal Pod Autoscaling.
- Apache Kafka / RabbitMQ: Powers reliable asynchronous messaging and event streaming.
- Redis: Facilitates state management, caching, and task lease locking.
- AES-256: Secures data at rest across all storage tiers.
- HL7 FHIR: Provides interoperability for lab and imaging systems.

## Rationale
This hybrid architecture combines on-premise Kubernetes clusters with AWS cloud regions to guarantee 99.99% high availability and data sovereignty compliance. Utilizing asynchronous message brokers and decoupled background workers ensures high-performance electronic medical record processing under strict security and audit constraints.