## Overview
Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Library Patron and Library Staff (Users)
- External Identity Provider, Digital Content Providers, Third-Party Payment Processor, External Notification Gateway, EU-certified Cloud Provider Infrastructure (External Systems)
- Web Application / API Gateway (Next.js / Node.js TypeScript)
- Catalog Service (Spring Boot Java) & Circulation Service (Spring Boot Java)
- Notification Service (Python FastAPI)
- PostgreSQL (Primary Database) & Elasticsearch (Search Engine)
- Event Bus (Apache Kafka / RabbitMQ with Dead Letter Queues)
- Observability Backend (OpenTelemetry)

## Relationships
- Library Patron / Staff -> HTTPS (TLS 1.3, OAuth2/OIDC) -> API Gateway
- API Gateway -> gRPC / REST -> Catalog Service & Circulation Service
- Catalog Service -> HTTPS -> Digital Content Providers
- Circulation Service -> AMQP / Kafka (mTLS, Payload Encryption) -> Event Bus
- Event Bus -> AMQP / Kafka -> Notification Service & Circulation Service
- API Gateway -> OpenTelemetry -> Observability Backend

## Technology Stack
- Next.js / Node.js TypeScript: Fast, scalable API gateway and client entry point.
- Spring Boot Java: Robust enterprise services for Catalog and Circulation.
- Python FastAPI: Lightweight service for Notification handling.
- PostgreSQL & Elasticsearch: Relational storage and sub-800ms search capability.
- Apache Kafka / RabbitMQ: Event-driven decoupling and asynchronous processing.
- Terraform / OpenTofu: Infrastructure as Code for EU region-locking and GDPR compliance.
- OpenTelemetry: Polyglot distributed tracing.

## Rationale
This container architecture leverages polyglot microservices and an event-driven event bus to ensure asynchronous payment resilience and sub-800ms search speeds. Strict infrastructure pinning and encryption guarantee full compliance with EU-only data residency mandates.