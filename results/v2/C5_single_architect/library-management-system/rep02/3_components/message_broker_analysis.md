## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It utilizes an event-driven architecture to process circulation tasks and maintain EU-only data residency.

## Key Elements
- Library Patrons and Library Staff (Users)
- Web Application (React/TypeScript SPA)
- API Gateway (Nginx / Spring Cloud Gateway)
- Core Domain Service (Java/Spring Boot)
- Search Service (Java with Elasticsearch)
- Notification Worker (Node.js)
- Database (PostgreSQL)
- Message Broker (RabbitMQ) containing Exchange Component, notification-queue, audit-event-queue, and Data Policy Enforcement Component
- External Systems: Payment Gateway, Notification Service, National Library Registry, Identity Provider

## Relationships
- Library Patrons / Staff -> Web Application [HTTPS]
- Web Application -> API Gateway [HTTPS/JSON]
- API Gateway -> Core Domain Service & Search Service [gRPC/HTTP]
- Core Domain Service -> Message Broker (Exchange Component) [AMQP]
- Exchange Component -> notification-queue & audit-event-queue [AMQP]
- notification-queue -> Notification Worker [AMQP]
- Message Broker -> Local Storage Volume [File I/O]

## Technology Stack
- React/TypeScript: Powers the frontend SPA for high responsiveness.
- Java/Spring Boot: Implements the robust Core Domain Service.
- Elasticsearch: Delivers sub-800ms 99th-percentile search performance.
- RabbitMQ: Handles asynchronous event-driven messaging via AMQP.
- PostgreSQL: Provides reliable relational persistence.

## Rationale
This architecture meets performance requirements through dedicated Elasticsearch indexing while ensuring strict EU data residency compliance via local RabbitMQ storage policies.