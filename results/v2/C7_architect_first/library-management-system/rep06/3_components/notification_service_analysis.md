## Overview
- Solution: Notification Service component within the Library Management System for asynchronous messaging and zero-loss patron notifications.
- Purpose: Delivers localized alerts via email and SMS while enforcing EU data residency constraints.

## Key Elements
- AMQP Consumer Component (Node.js, amqplib)
- Notification Router Component (Node.js)
- Template Engine Component (Nunjucks)
- Provider Integration Adapters (Node.js, Axios, SendGrid, Twilio)
- Outbox Repository Component (Node.js, TypeORM, PostgreSQL)
- Preference Cache Component (Node.js, ioredis, Redis)

## Relationships
- AMQP Consumer -> RabbitMQ: Consumes event messages [AMQP 0-9-1 with TLS 1.3]
- Notification Router -> Preference Cache: Queries patron preferences [In-Memory/TCP]
- Notification Router -> Template Engine: Renders localized templates [Internal Call]
- Notification Router -> Provider Integration Adapters: Sends payload [HTTPS]
- Provider Integration Adapters -> Outbox Repository: Persists delivery status [SQL/TCP]

## Technology Stack
- Node.js: Lightweight runtime for asynchronous messaging and IO-bound tasks
- RabbitMQ: Message broker with manual acknowledgments and dead-letter exchanges for zero-loss guarantees
- Nunjucks: Template engine supporting secure, localized message rendering
- PostgreSQL: Central database ensuring strict EU-only data residency and outbox audit logs
- Redis: In-memory cache for low-latency patron preference lookups
- SendGrid & Twilio: External providers for email and SMS delivery

## Rationale
- The architecture guarantees zero message loss and sub-second routing via decoupled consumers, outbox patterns, and low-latency caching.
- Compliance with EU data residency and privacy mandates is strictly maintained through encrypted PostgreSQL storage and secure in-transit protocols.