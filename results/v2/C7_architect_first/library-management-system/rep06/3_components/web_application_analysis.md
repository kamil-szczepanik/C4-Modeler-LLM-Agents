## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Patrons
- Library Staff
- Web Application (React, TypeScript, Nginx reverse proxy)
- API Gateway (Kong or Spring Cloud Gateway)
- Core Domain Service (Java, Spring Boot)
- Search Service (Python, FastAPI, Elasticsearch)
- Notification Service (Node.js)
- PostgreSQL Database
- RabbitMQ Message Broker
- External Payment Gateway
- Digital Content Repositories

## Relationships
- Library Patrons -> Web Application: Accesses public catalogs and self-service portals [HTTPS]
- Library Staff -> Web Application: Manages cataloging and circulation [HTTPS]
- Web Application -> API Gateway: Routes API requests via Nginx reverse proxy [HTTPS/REST]
- API Gateway -> Core Domain Service, Search Service, Notification Service [gRPC/REST]
- Search Service -> Elasticsearch [TCP]
- Core Domain Service -> PostgreSQL Database [JDBC/TLS]
- Core Domain Service -> RabbitMQ Message Broker [AMQP]

## Technology Stack
- React/TypeScript with Nginx: Client-side rendering, static asset hosting, and secure reverse proxy/BFF pattern for session management.
- Java/Spring Boot: Powers the robust Core Domain Service for complex business logic.
- Python/FastAPI & Elasticsearch: Delivers high-performance search capabilities meeting sub-800ms latency requirements.
- PostgreSQL & RabbitMQ: Provides reliable relational data storage and asynchronous messaging.
- TLS 1.3 & HttpOnly Cookies: Secures data-in-transit and protects session tokens from XSS.

## Rationale
This architecture combines a high-performance frontend with a scalable microservices backend to meet stringent sub-800ms search SLAs. Furthermore, utilizing Nginx as a reverse proxy for secure cookie handling ensures strict compliance with EU-only data residency mandates.