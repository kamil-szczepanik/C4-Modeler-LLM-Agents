## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It adheres strictly to EU-only data residency requirements while ensuring high-performance search capabilities.

## Key Elements
- Library Patrons, Librarians/Circulation Staff, Library Administrators, Third-Party Vendors/Digital Content Providers
- Single Page Application (SPA)
- API Gateway
- Core Domain Container
- Search Container
- Integration Container
- Async Event Broker
- EU Payment Gateway, Notification Service
- EU-hosted PostgreSQL, Elasticsearch

## Relationships
- SPA to API Gateway: HTTPS/REST
- API Gateway to Core Domain/Search/Integration: gRPC or REST over TLS within EU-isolated VPC
- Core Domain to EU-hosted PostgreSQL: Database protocol over TLS
- Integration Container to EU Payment Gateway & Notification Service: HTTPS
- Core Domain to Async Event Broker: Domain events publishing (SASL/SCRAM, mTLS)
- Integration Container to Async Event Broker: Asynchronous consumption with DLQs

## Technology Stack
- React/TypeScript: SPA framework for intuitive user experience
- Nginx or Spring Cloud Gateway: API Gateway for request routing
- Java/Spring Boot: Core Domain Container for robust cataloguing and circulation (R-01)
- Elasticsearch: Dedicated Search Container for sub-800ms search performance (R-05)
- Node.js/TypeScript: Integration Container for external APIs and payment handling
- Apache Kafka or RabbitMQ: Async Event Broker for decoupled event-driven notifications
- Kubernetes (EKS/AKS) & ArgoCD: Container orchestration and declarative GitOps deployment
- PostgreSQL: EU-hosted transactional database with encryption-at-rest (CMK)

## Rationale
This architecture isolates user-facing workflows and decouples search and notification processing to consistently achieve the required 99th-percentile search response time under 800ms. Strict containerization, mTLS, and regional hosting enforce EU-only data residency compliance and enterprise security.