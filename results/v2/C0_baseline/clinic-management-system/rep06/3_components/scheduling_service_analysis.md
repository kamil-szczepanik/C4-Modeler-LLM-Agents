## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% high availability, HIPAA/GDPR compliance, and seamless interoperability across hybrid cloud environments.

## Key Elements
- **Users**: Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, Compliance Officer
- **External Systems**: External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, Identity Provider (IdP), External Notification Gateway
- **Containers**: API Gateway (Kong/NGINX (Envoy)), Patient Portal Frontend (React), Staff Web Application (React), Core Clinical & EMR Service (Java Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service (Go/Spring Boot)
- **Scheduling Service Components**: Appointment API Controller, Clash Detection Engine, Notification Dispatcher, Event Publisher Component
- **Data & Infrastructure**: PostgreSQL databases (PostgreSQL), Redis (Redis), AWS S3 Object Lock (AWS S3), HashiCorp Vault (HashiCorp Vault), Apache Kafka / RabbitMQ

## Relationships
- API Gateway -> Scheduling Service: Routes scheduling requests [OAuth2/OIDC, mTLS]
- Appointment API Controller -> Patient Portal Frontend & API Gateway: Exposes REST/GraphQL endpoints [HTTPS/TLS]
- Clash Detection Engine -> PostgreSQL: Persists appointments and checks availability with OCC [TCP, SQL]
- Clash Detection Engine -> Redis: Manages distributed locks and fast availability caching [TCP, RESP]
- Notification Dispatcher -> External Notification Gateway: Sends SMS/Email reminders [HTTPS/TLS, API with HMAC]
- Event Publisher -> Audit & Compliance Service: Streams tokenized appointment audit events [AMQP/Kafka, TLS]

## Technology Stack
- **Scheduling Service**: Node.js (Fastify) or Python (FastAPI) for rapid appointment workflow iteration
- **API Controller**: Fastify / FastAPI for high-performance routing
- **Clash Detection**: Redis (clustered mode) + PostgreSQL using Optimistic Concurrency Control (OCC) for zero race conditions
- **Worker Queue**: Celery/BullMQ with persistent storage and dead-letter queues (DLQ)
- **Messaging/Events**: Apache Kafka or RabbitMQ for asynchronous lifecycle event publishing
- **Resilience**: Resilience4j circuit breaker pattern for external integrations
- **Security & Secrets**: HashiCorp Vault for runtime secret injection, AES-256 and TLS 1.3 for encryption

## Rationale
This architecture uses an asynchronous, event-driven pattern within the Scheduling Service to decouple non-blocking tasks like notifications and analytics, preserving P95 performance for core appointment workflows. Strict containerization, hybrid deployment strategies, and multi-region clustering fulfill the rigorous 99.99% availability and HIPAA/GDPR compliance requirements.