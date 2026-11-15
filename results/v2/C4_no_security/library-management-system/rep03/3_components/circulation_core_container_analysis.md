## Overview
- Solution: Circulation & Core Container within the Library Management System.
- Purpose: Enforce circulation business rules, automated fine calculations, policy validations, and secure data persistence.

## Key Elements
- Circulation & Core Container (Node.js/Express)
- Loan Management Component
- Fine & Fee Component
- Core Data Access Layer
- Policy Validation Engine
- Audit & Compliance Module
- PostgreSQL Database
- RabbitMQ Message Broker
- API Gateway (Nginx/Kong)

## Relationships
- API Gateway -> Circulation & Core Container: Routes internal traffic [gRPC]
- Circulation & Core Container -> RabbitMQ Message Broker: Publishes domain events [AMQP]
- Circulation & Core Container -> PostgreSQL Database: Persists transactional data and audit logs [TCP]
- Core Data Access Layer -> PostgreSQL Database: Interfaces via TypeORM with PgBouncer connection pooling

## Technology Stack
- Node.js/Express: Chosen for high throughput on circulation checkouts
- TypeScript/JavaScript: Standardized language for backend development
- TypeORM: Object-relational mapping for database interactions
- PostgreSQL: Relational database enforcing EU-only data residency and immutable audit logging
- RabbitMQ: Message broker utilizing transactional outbox pattern for asynchronous event publishing
- PgBouncer: Connection pooling to prevent database thread starvation

## Rationale
- The architecture ensures strict transactional integrity and EU-only data residency for patron history within PostgreSQL.
- Utilizing Node.js with gRPC and a component-driven internal design guarantees high-performance circulation checkouts and actionable policy validations.