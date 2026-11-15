## Overview
The Circulation & Member Service manages loans, fines, and patron PII for the Library Management System. It ensures secure, EU-compliant operations and frictionless self-service workflows for patrons and staff.

## Key Elements
- Circulation & Member Service (Node.js / NestJS Container)
- Loan Management Controller & Service (TypeScript / NestJS)
- Fine & Payment Processor Component (TypeScript / NestJS)
- Event Publisher & Notification Event Dispatcher (TypeScript / NestJS)
- Member Profile & PII Manager (TypeScript / NestJS)
- Dispute Management Handler (TypeScript / NestJS)
- External Systems: EU Identity Provider, EU-compliant Payment Gateway, EU Cloud Hosting Provider (Frankfurt), Message Broker (Apache Kafka / RabbitMQ), Database (PostgreSQL)

## Relationships
- API Gateway -> Circulation & Member Service: Routes circulation and member requests [gRPC over mTLS]
- Circulation & Member Service -> Database: Reads/writes transactional data and PII [SQL over TLS with AES-256]
- Circulation & Member Service -> Message Broker: Emits domain events [AMQP/TLS with SASL/SCRAM]
- Fine & Payment Processor -> EU-compliant Payment Gateway: Processes tokenized payments [HTTPS/TLS 1.3]
- Notification Event Dispatcher -> Notification Worker: Triggers alerts [gRPC/AMQP]

## Technology Stack
- Node.js / NestJS: Chosen for scalable, modular microservice architecture
- TypeScript: Ensures type safety across all internal service components
- TypeORM / Prisma: Provides robust database abstraction and TCP communication
- AES-256: Implemented for application-level PII encryption and database storage to meet EU data residency requirements
- JWT: Enforces strict RBAC/ABAC and ownership validation

## Rationale
This architecture guarantees strict EU data residency and GDPR compliance via localized Frankfurt hosting and field-level PII encryption. It maintains high transactional integrity and reduces PCI-DSS scope through tokenized payment handling.