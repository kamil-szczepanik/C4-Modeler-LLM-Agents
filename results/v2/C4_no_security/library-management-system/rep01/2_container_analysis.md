## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU data residency and high-performance search capabilities.

## Key Elements
- Library Patrons and Librarians/Administrators
- Web Application (SPA)
- API Gateway
- Core Services API (Modular Monolith)
- Search Engine
- Database
- Async Message Broker
- External Systems: EU Identity Provider, EU Object Storage, SEPA/Stripe EU API Payment Gateway, External Notification Service, SIEM

## Relationships
- Library Patrons/Librarians -> HTTPS -> Web Application (SPA)
- Web Application (SPA) -> HTTPS -> API Gateway
- API Gateway -> REST/gRPC -> Core Services API
- Core Services API -> TCP -> PostgreSQL & Search Engine
- Core Services API -> AMQP -> Async Message Broker

## Technology Stack
- React/TypeScript for Web Application (SPA)
- Node.js/NestJS for Core Services API
- Elasticsearch/OpenSearch for Search Engine
- PostgreSQL for transactional database
- RabbitMQ/Apache Kafka for Async Message Broker
- Nginx/Envoy for API Gateway
- Kubernetes (EKS/AKS) and Docker for orchestration

## Rationale
This architecture uses an isolated Search Engine and asynchronous messaging to guarantee sub-800ms search performance under load. Deploying all containers exclusively within managed EU cloud regions satisfies strict data residency mandates.