## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency requirements.

## Key Elements
- Circulation Service (Node.js / Express container)
- Circulation API Controller (Express.js)
- Loan Management Engine (TypeScript / Domain Services with BullMQ)
- Fine & Payment Manager (Node.js Service with Payment Webhook Handler)
- Event Publisher (KafkaJS Client)
- Data Access Repository (Prisma ORM)
- Notification Scheduler Component (node-cron / BullMQ)
- PostgreSQL Database and Apache Kafka Event Broker

## Relationships
- API Gateway -> Circulation API Controller: Routes circulation requests [mTLS via Istio Service Mesh]
- Data Access Repository -> PostgreSQL Database: Persists circulation data [AES-256 encryption, EU-hosted]
- Event Publisher -> Apache Kafka Event Broker: Publishes check-out and reminder events [TLS-encrypted event streams]
- Fine & Payment Manager -> Third-Party Payment Gateway: Processes fines [REST/HTTPS with mTLS and HMAC webhook verification]

## Technology Stack
- Node.js / Express: Runtime for the Circulation Service ensuring low-latency operations
- TypeScript: Strongly typed domain logic in the Loan Management Engine
- Prisma ORM: Database interactions ensuring secure data access and EU residency compliance
- Apache Kafka: Asynchronous event messaging for decoupled workflows
- BullMQ / node-cron: Background scheduling for automated grace periods and notifications

## Rationale
The component architecture isolates payment processing, event publishing, and loan logic to maintain high performance under 800ms. Strict security controls and decoupled asynchronous tasks ensure GDPR compliance and reliable user experiences.