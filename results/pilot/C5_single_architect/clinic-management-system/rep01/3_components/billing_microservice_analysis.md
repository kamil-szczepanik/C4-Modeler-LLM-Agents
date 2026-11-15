## Overview
The Billing Microservice is a core container within the Clinic Management System that handles patient billing, invoice generation, and insurance claim processing. It ensures secure, resilient financial transactions while complying with strict healthcare regulations.

## Key Elements
- `BillingController`: Spring MVC component handling incoming gRPC/REST endpoints from the API Gateway.
- `ClaimProcessingService`: Core business logic component orchestrating invoice generation and state transitions.
- `InsuranceGatewayClient`: Resilience4j-wrapped WebClient managing external HTTPS/REST communication.
- `BillingRepository`: Spring Data JPA component managing secure database persistence.
- `TokenizationService`: Component isolating and handling patient financial instruments and credit card data via a token vault.
- `ClaimStatusListener`: Spring Kafka message listener component consuming asynchronous updates from the Messaging Backbone.
- `KafkaEventPublisher`: Component publishing financial domain events.

## Relationships
- API Gateway -> `BillingController`: Routes incoming requests [gRPC, mTLS]
- `BillingRepository` -> PostgreSQL Database: Persists financial data [PostgreSQL, AES-256]
- `KafkaEventPublisher` -> Messaging Backbone: Publishes domain events [Apache Kafka]
- `InsuranceGatewayClient` -> Insurance Gateways: Submits billing claims [HTTPS, REST]
- Messaging Backbone -> `ClaimStatusListener`: Consumes claim status updates [Apache Kafka]

## Technology Stack
- Spring MVC: Handles incoming gRPC and REST endpoints with robust routing.
- Spring Data JPA: Manages ACID-compliant relational persistence with Spring `@Transactional`.
- Resilience4j: Wraps external clients to ensure fault tolerance and circuit breaking for insurance APIs.
- Apache Kafka: Enables asynchronous, decoupled event-driven claim status reconciliation.
- PostgreSQL Database: Provides secure, encrypted relational storage.

## Rationale
This component-level architecture isolates sensitive financial data through a dedicated token vault to satisfy HIPAA and GDPR compliance constraints. Asynchronous event consumption via Apache Kafka and resilience patterns ensure high availability (99.99%) and thread safety under heavy workloads.