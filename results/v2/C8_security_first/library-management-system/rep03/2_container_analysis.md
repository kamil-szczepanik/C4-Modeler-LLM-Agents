## Overview
The Library Management System is a robust solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search response times.

## Key Elements
* Web Application Container (React/TypeScript SPA) - Patron Self-Service Portal
* Librarian Management Portal Container (React/TypeScript SPA)
* API Gateway Container (Kong / Envoy)
* Search Microservice Container (Java / Spring Boot)
* Circulation & Catalogue Microservice Container (Java / Spring Boot)
* Notification Dispatcher Container (Node.js / TypeScript)
* Message Broker (RabbitMQ / Kafka)
* Database Layer (PostgreSQL instances with EU-pinned TLS 1.3/JDBC)
* Orchestration (Kubernetes EKS/AKS in EU regions)

## Relationships
* Web and Librarian Portals communicate via HTTPS to API Gateway
* API Gateway routes ingress to microservices using OAuth 2.0 / OIDC and mTLS
* Microservices communicate via gRPC over mTLS
* Circulation publishes asynchronous events to RabbitMQ/Kafka
* Notification Dispatcher consumes events and calls EU Notification Gateway via HTTPS/REST
* Search queries Elasticsearch (EU-hosted)

## Technology Stack
* React/TypeScript: High-responsiveness for patron and librarian UIs
* Kong / Envoy: Secure ingress routing and rate limiting
* Java / Spring Boot: High-performance microservices for search and circulation
* Elasticsearch: Sub-800ms search performance (R-05)
* PostgreSQL: Relational persistence compliant with EU-only residency
* Kubernetes & Prometheus: Automated horizontal scaling and observability
* RabbitMQ/Kafka: Asynchronous decoupling for notifications

## Rationale
This architecture uses container decomposition and a database-per-service pattern to isolate heavy workloads, ensuring search latency remains under 800ms. Strict EU-region pinning, mTLS, and RBAC satisfy regional compliance and security constraints.