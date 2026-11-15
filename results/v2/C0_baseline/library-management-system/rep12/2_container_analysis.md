## Overview
The Library Management System provides a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and deliver self-service patron portals. It enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Library Patrons and Library Staff
- External Systems: Payment Gateway, Identity Provider / SSO, Notification Service, Logging & APM
- Containers: Patron Web Application, Staff Administration Portal, API Gateway, Core Domain Services, Search Engine, Relational Database, Async Event Bus, Notification Worker

## Relationships
- Patron Web Application to API Gateway via HTTPS/REST
- Staff Administration Portal to API Gateway via HTTPS
- API Gateway to Core Domain Services via mTLS
- Core Domain Services to PostgreSQL and Elasticsearch via mTLS
- Core Domain Services to Async Event Bus via mTLS
- Notification Worker to external Notification Service via HTTPS/API Keys

## Technology Stack
- React / TypeScript & Angular / TypeScript: Frontend web applications served via CDN and internal networks
- Nginx / Spring Cloud Gateway: Single reverse proxy enforcing TLS 1.3 and JWT authentication
- Node.js / NestJS: Modular monolith core domain services and background notification worker
- Elasticsearch: Dedicated search engine ensuring <800ms P99 response times
- PostgreSQL: Relational database for transactional consistency with AES-256 encryption
- RabbitMQ / Apache Kafka: Async event bus for decoupled event-driven architecture
- Kubernetes: EU-region-locked cluster infrastructure with mTLS zero-trust networking

## Rationale
This container architecture separates patron self-service from staff administration to ensure high performance and strict compliance. Utilizing an async event bus and dedicated search engine guarantees low-latency responses while maintaining EU data residency constraints.