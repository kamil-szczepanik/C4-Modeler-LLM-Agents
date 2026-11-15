## Overview
- Manages patient admissions, scheduling, electronic medical records (EMR), and billing for clinics.
- Ensures HIPAA, GDPR, and 99.99% availability constraints in a hybrid cloud environment.

## Key Elements
- API Router & Auth Middleware (TypeScript / Fastify)
- Patient & Scheduling Engine (TypeScript)
- EMR Core & Audit Service (TypeScript)
- Data Access Repository (Knex.js / node-postgres)
- In-Memory Caching Layer (Redis)
- Billing & Claims Service (Java Spring Boot)
- PostgreSQL with CloudNativePG
- Apache Kafka

## Relationships
- EMR & Patient Service -> Billing & Claims Service: Billing integration and workflows via gRPC over mTLS
- EMR Core -> Apache Kafka: Publishes domain events (e.g., PatientAdmitted) via TLS and SASL/SCRAM
- Data Access Repository -> PostgreSQL: Reads and writes encrypted records via TLS and AES-256
- Data Access Repository -> Redis: Caches clinic schedules and patient lookups via TCP

## Technology Stack
- Node.js / Fastify: High-performance backend runtime for sub-second EMR screen loads (R-07)
- TypeScript: Strongly typed codebase for maintainability and clinical safety
- PostgreSQL (CloudNativePG): Relational persistence with AES-256 encryption at rest (R-05)
- Redis: In-memory caching for low-latency patient and schedule lookups
- Apache Kafka: Event broker for asynchronous messaging using SASL/SCRAM and TLS
- gRPC over mTLS: Secure, low-latency inter-service communication

## Rationale
- Decomposes the EMR service into internal components to isolate business logic and meet the <1s P95 latency target.
- Enforces multi-layer security, encryption, and audit trails to guarantee strict HIPAA and GDPR compliance.