## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search responses.

## Key Elements
- Library Patrons, Librarians/Circulation Staff, Library Administrators
- API Gateway (Nginx / Kong)
- Core Services Container (Java / Spring Boot)
- Search Container (Elasticsearch)
- Database Container (PostgreSQL)
- Async Worker Container (Python / Celery or Java)
- EU Identity Provider (IdP), EU Payment Gateway, EU Notification Service, EU Cloud Infrastructure
- Centralized Log & Metrics Aggregator

## Relationships
- API Gateway -> Core Services Container: Routes traffic [mTLS via gRPC/HTTPS]
- Core Services Container -> Database Container: Queries relational data [JDBC]
- Core Services Container -> Search Container: Queries catalog search index [HTTP/REST]
- Core Services Container -> Async Worker Container: Publishes events [Message Broker / Queue]
- Core Services Container -> EU Identity Provider: Authenticates users and validates tokens [OIDC/OAuth2 over HTTPS]
- Core Services Container -> EU Payment Gateway: Processes financial transactions [REST/HTTPS via Spring Cloud OpenFeign]
- Core Services Container -> Centralized Log & Metrics Aggregator: Sends logs and metrics [HTTPS]

## Technology Stack
- Java / Spring Boot: Core business logic framework providing robust enterprise capabilities and modular architecture.
- Spring Security & OAuth2: Validates JWTs and enforces Role-Based Access Control.
- PostgreSQL & JPA/Hibernate: Relational data persistence with parameterized queries for injection prevention.
- Elasticsearch: Delivers fast catalog search indexing to meet sub-800ms performance requirements.
- Resilience4j: Implements circuit breakers to prevent cascading failures from external payment services.
- Kubernetes: Orchestrates stateless container scaling with fine-grained probes and CSI-mounted secrets.

## Rationale
Modular Spring Boot components inside a stateless container enable horizontal scalability and fault isolation under peak academic workloads. Strict component decomposition, mTLS, and dedicated governance controls satisfy EU data residency and PII compliance mandates.