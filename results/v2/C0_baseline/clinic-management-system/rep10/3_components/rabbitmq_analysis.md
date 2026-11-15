## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMR, scheduling, and billing. It ensures high availability, strict security compliance, and robust asynchronous event-driven integration.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers, Compliance Officers
- External Insurance/Clearinghouse System, External Laboratory & Imaging System
- React / TypeScript Web Application, NGINX / Envoy API Gateway
- Node.js / Go EMR & Scheduling Services, Java / Spring Boot Billing & Integration Services
- Python / FastAPI Notification Service, PostgreSQL, Redis, HashiCorp Vault
- RabbitMQ Message Broker (Exchange Router, Quorum Queues, Dead Letter Exchange)

## Relationships
- Web Application -> API Gateway: Routes user requests [HTTPS]
- API Gateway -> Microservices: Forwards authorized API requests [gRPC / HTTPS]
- EMR, Billing, & Scheduling Services -> RabbitMQ: Publishes and consumes events [AMQP over TLS / mTLS]
- RabbitMQ Exchange Router -> Quorum Queues: Routes messages [AMQP]
- Quorum Queues -> Dead Letter Exchange: Forwards failed messages on consumer rejection [AMQP]
- DLX -> Audit & Review Queue -> Integration Service: Persists failed events [AMQP / TLS]
- Microservices -> PostgreSQL: Persists clinical and financial data [TLS / AES-256]
- Microservices -> HashiCorp Vault: Retrieves secrets and credentials [HTTPS / mTLS]

## Technology Stack
- Hybrid Cloud (Kubernetes on-prem, AWS eu-central-1): Ensures high availability and active-active deployment.
- RabbitMQ (Quorum Queues & DLX): Provides reliable at-least-once messaging and clinical audit trails.
- PostgreSQL & Redis: Secures structured data with AES-256 encryption and high-performance caching.
- Mutual TLS (mTLS) & SCRAM-SHA-256: Secures inter-service and broker communication for HIPAA/GDPR compliance.
- HashiCorp Vault: Centralizes dynamic secrets management and automated rotation.

## Rationale
This architecture uses decoupled microservices and a resilient messaging backbone to meet the strict 99.99% availability and data retention requirements. Multi-layered encryption, RBAC, and virtual host isolation ensure total HIPAA and GDPR compliance for sensitive clinical workflows.