## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Patron and Library Staff (Users)
- External Payment Gateway, Digital Content Provider, Notification Service
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway / Envoy)
- Catalogue Service, Circulation Service, Digital Content Proxy Service (Java, Spring Boot)
- Notification Worker (Node.js)
- PostgreSQL (PostgreSQL), Redis (Redis), Elasticsearch (Elasticsearch)
- RabbitMQ (RabbitMQ): Exchange Router, Notification Queue, Dead Letter Exchange & Queue (DLX/DLQ)

## Relationships
- Web Application -> API Gateway: Routes client requests [HTTPS]
- Catalogue Service -> Exchange Router: Publishes catalog events [AMQP]
- Circulation Service -> Exchange Router: Publishes loan/circulation events [AMQP]
- Exchange Router -> Notification Queue: Enqueues notification tasks [AMQP]
- Notification Queue -> Notification Worker: Dispatches pending notification tasks [AMQP]
- Notification Worker -> Exchange Router: Routes poisoned messages to DLX on failure [AMQP]
- Core Services -> PostgreSQL: Data persistence [JDBC]
- Core Services -> Elasticsearch: Item search indexing [HTTP/REST]

## Technology Stack
- React with TypeScript: Powers the self-service web application interface
- Spring Boot (Java): Implements core domain microservices
- Spring Cloud Gateway / Envoy: Manages secure API routing
- Elasticsearch: Delivers sub-800ms 99th-percentile search responses
- PostgreSQL: Provides durable relational storage with EU-only residency
- RabbitMQ: Handles asynchronous event messaging via AMQP and Erlang/Mnesia storage

## Rationale
This decoupled microservices architecture scales independently to meet demanding search performance SLAs while leveraging message queuing for reliable asynchronous processing. Strict database localization ensures compliance with EU-only data residency constraints.