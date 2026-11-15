## Overview
The Library Management System is a comprehensive platform for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It ensures strict EU data residency while delivering high-performance catalog searches under 800 milliseconds.

## Key Elements
- Library Patron and Library Staff (Users)
- External Payment Gateway, Digital Content Provider, and Notification Service (External Systems)
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway / Envoy)
- Catalogue Service, Circulation Service, and Digital Content Proxy Service (Java, Spring Boot)
- Notification Worker (Node.js)
- PostgreSQL (Primary Database) and Redis (Cache)
- Elasticsearch (Search Engine)
- RabbitMQ (Message Broker)

## Relationships
- Web Application to API Gateway via HTTPS/JSON
- API Gateway to internal services via gRPC over TLS
- Circulation Service to External Payment Gateway via REST/HTTPS
- Digital Content Proxy Service to Digital Content Provider via HTTPS
- Notification Worker to Notification Service via AMQP/RabbitMQ

## Technology Stack
- React and TypeScript: Powers the frontend Single-Page Application for responsive user interactions.
- Java and Spring Boot: Implements scalable backend domain services.
- Elasticsearch: Delivers high-speed search capabilities meeting the <800ms P99 performance requirement.
- PostgreSQL: Provides relational data persistence restricted to an EU region for compliance.
- Redis: Caches frequent reads and user sessions to optimize performance.
- RabbitMQ: Manages asynchronous message queuing for notifications.

## Rationale
This architecture cleanly separates concerns through dedicated microservices while utilizing specialized data stores like Elasticsearch and Redis to meet stringent performance goals. Furthermore, localizing PostgreSQL within the EU guarantees full compliance with data residency constraints.