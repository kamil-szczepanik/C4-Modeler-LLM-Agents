## Overview
The Library Management System provides item cataloging, circulation, and self-service portals with strict EU data residency. The Integration Service container handles third-party and legacy system communications.

## Key Elements
- Integration Service: Node.js, Express, TypeScript container
- Integration Router / Controller: Express component for internal REST endpoints
- Payment Gateway Adapter: TypeScript component for external payment communication
- ILS Sync Worker: TypeScript component for legacy ILS data synchronization
- Webhook Handler: Express component for payment asynchronous callbacks
- Data Mapper & Transformer: TypeScript utility component for schema translations
- Circuit Breaker & Retry Manager: TypeScript component for downstream resilience
- Audit & Compliance Logger: TypeScript component for GDPR-compliant tracking
- External Payment Gateway & Legacy ILS: External systems
- Core Domain Service: Internal upstream container
- RabbitMQ: Message broker container
- PostgreSQL: Database container for local audit logs

## Relationships
- Core Domain Service -> Integration Router [REST / HTTPS]
- ILS Sync Worker -> RabbitMQ [AMQP]
- External Payment Gateway -> Webhook Handler [HTTPS / Webhook]
- Payment Gateway Adapter & ILS Sync Worker -> Data Mapper & Transformer [In-Memory Function Call]
- Payment Gateway Adapter & ILS Sync Worker -> Circuit Breaker & Retry Manager [In-Memory Function Call]
- Circuit Breaker & Retry Manager -> External Payment Gateway / Legacy ILS [HTTPS]
- Data Mapper & Transformer -> Audit & Compliance Logger [In-Memory Function Call]
- Audit & Compliance Logger -> PostgreSQL [SQL / TCP]

## Technology Stack
- Node.js & Express: Event-driven I/O model for network-bound integrations
- TypeScript: Strong typing and maintainability for external API contracts
- AMQP via RabbitMQ: Asynchronous event messaging for ILS synchronization
- HTTPS/REST/Webhooks: Secure protocols for external gateway and legacy integration
- SQL/TCP via PostgreSQL: Local persistence for EU-compliant audit logs

## Rationale
The component architecture ensures high availability and fault tolerance through dedicated circuit breakers when interacting with fragile external systems. It strictly enforces EU data residency and GDPR compliance via isolated auditing and secure local persistence.