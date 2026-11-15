## Overview
The Library Management System provides item cataloging, circulation, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Catalogue Management Component (Spring Boot `@Service`, Java)
- Circulation Component (Spring Boot `@Service`, Java)
- Notification & Payment Facade (Spring Boot `@Component`, Java)
- Search Synchronization Component (Spring Boot `@Service`, Java)
- PostgreSQL (AWS RDS EU)
- Search Container (Elasticsearch / OpenSearch)
- Message Broker (Apache Kafka / RabbitMQ)
- External Services: Stripe EU, SendGrid EU, Keycloak/Auth0 EU tenant

## Relationships
- API Gateway -> Core Services Container: Routes traffic via [gRPC/HTTPS using mTLS]
- Catalogue Management & Circulation -> PostgreSQL: Reads/writes relational data via [JDBC, mTLS]
- Catalogue Management -> Message Broker: Publishes item state changes via [Kafka, AMQP]
- Search Synchronization Component -> Search Container: Indexes item data via [TCP/gRPC with mTLS]
- Notification & Payment Facade -> Stripe EU & SendGrid EU: Processes payments and notifications via [HTTPS (REST)]

## Technology Stack
- Java & Spring Boot: Framework for modular monolith internal components and business logic
- Spring Security: Enforces method-level Role-Based Access Control (RBAC)
- Resilience4j: Implements circuit breakers for outbound HTTP calls
- JPA / Hibernate: Manages relational data persistence in PostgreSQL
- HashiCorp Vault / AWS Secrets Manager: Securely injects API credentials

## Rationale
This modular monolith architecture inside the Core Services Container separates domain concerns cleanly while maintaining minimal latency. Asynchronous event propagation guarantees rapid catalogue indexing to meet sub-800ms search performance requirements.