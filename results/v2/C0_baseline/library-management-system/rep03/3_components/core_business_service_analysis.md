## Overview
The Library Management System is a comprehensive digital solution designed for public and academic libraries to catalogue items, manage circulation, and provide robust self-service patron portals. It ensures strict EU-only data residency and high-performance transactional integrity.

## Key Elements
- **Users**: Library Patrons, Library Staff
- **Gateways & Infrastructure**: API Gateway (Nginx / Envoy), Secrets Manager (HashiCorp Vault)
- **Core Container**: Core Business Service (Java / Spring Boot)
- **Core Internal Components**: API Controller Layer, Cataloguing & Inventory Component, Circulation & Loan Engine Component, Event Publisher Component, Vault Integration Component
- **Data & Messaging**: Relational DB (PostgreSQL), Message Broker (Kafka / RabbitMQ), Search Service (Elasticsearch / OpenSearch)
- **External Systems**: Third-Party Identity Providers, Payment Gateway, Notification Service, SIEM Platform

## Relationships
- API Gateway -> Core Business Service: Routes traffic via service mesh [gRPC/REST over mTLS (Istio)]
- Core Business Service -> Relational DB: Reads and writes transactional data [SQL / JDBC with Spring Data JPA]
- Core Business Service -> Search Service: Syncs data asynchronously [AMQP / Kafka]
- Core Business Service -> Message Broker: Publishes domain events [Kafka / AMQP]
- Core Business Service -> Secrets Manager: Retrieves dynamic secrets [HashiCorp Vault API]

## Technology Stack
- **Language & Runtime**: Java 17+ with Spring Boot, tuned with G1GC (`-XX:+UseG1GC`) for predictable latency.
- **Security**: OAuth2/JWT validation, Spring Security, JSR-380 Bean Validation, Resilience4j circuit breakers, and Istio mTLS.
- **Persistence & Secrets**: PostgreSQL (AES-256 encryption at rest, TLS 1.3 in transit) paired with HashiCorp Vault for dynamic credential injection.
- **Observability**: OpenTelemetry for distributed tracing with strict PII data-masking routed to a Centralized SIEM Platform.

## Rationale
This architecture guarantees strict transactional integrity and real-time inventory validation to support the self-service portal while meeting the sub-800ms search performance SLA via asynchronous Kafka eventing. Furthermore, strict containerization, zero-trust mTLS networking, and localized PostgreSQL instances fully enforce the mandated EU-only data residency and security compliance constraints.