## Overview
[The Online Bookstore platform provides a globally accessible e-commerce system for browsing catalogues, secure multi-currency checkout, and personalized recommendations. The architecture leverages AWS cloud infrastructure across multiple regions to ensure high availability and scalability for 1M MAU.]

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: Payment Gateway, Shipping Providers, Tax Calculation Service, Notification Service, SIEM Provider, Compliance/Archival Store, Global Content Delivery Network (CDN) and WAF
- **Containers**: Single Page Application / Mobile Client (React/Angular/Native), API Gateway (AWS API Gateway), Microservices (Catalog, Order & Checkout, Recommendation, Review), Asynchronous Message Broker (AWS SQS/SNS), Distributed Caching Container (Amazon ElastiCache), Compliance/User Data Container, Configuration/Secrets Management (AWS Secrets Manager)
- **Order & Checkout Service Components**: API Layer, Application Layer (Saga Orchestrators), Domain Layer (Checkout State Machines), Infrastructure Layer (Persistence, External API Adapters), Idempotency Ledger (Redis/ElastiCache), Message Outbox, Health/Readiness Probes (`/health/readiness`, `/health/liveness`)

## Relationships
- **API Gateway -> Order & Checkout Service**: Routes order and checkout requests via REST/gRPC
- **Order & Checkout Service -> Payment Gateway**: Processes secure payments via TLS and AWS SQS/SNS
- **Order & Checkout Service -> Shipping Providers**: Arranges fulfillment via TLS and AWS SQS/SNS
- **Order & Checkout Service -> Asynchronous Message Broker**: Publishes/consumes events via AWS SQS/SNS
- **Order & Checkout Service -> Compliance/User Data Container**: Accesses order database via Database-per-Service (TCP)
- **Order & Checkout Service -> Tax Calculation Service**: Calculates taxes via gRPC/HTTPS
- **Order & Checkout Service -> Notification Service**: Triggers notifications via asynchronous messaging (AMQP/HTTPS)
- **Order & Checkout Service -> SIEM Provider**: Exports structured JSON logs via HTTPS

## Technology Stack
- **Backend Services**: Java/Spring Boot or Node.js for microservices; Python for Recommendation Service
- **Messaging & Caching**: AWS SQS/SNS for asynchronous messaging; Amazon ElastiCache (Redis) for distributed caching and idempotency ledgers
- **Resilience & Patterns**: Idempotency Pattern, Orchestration-based Saga Pattern, Outbox Pattern, Circuit Breakers, Bulkhead Isolation, Exponential Backoff with Jitter
- **Observability & Security**: OpenTelemetry for distributed tracing; AWS Secrets Manager for secrets; strict Data Masking and Logging Policies for GDPR/CCPA compliance

## Rationale
[This architecture fits requirements by employing patterns like Saga, Outbox, and Idempotency to guarantee distributed transaction integrity and eliminate double-charges across third-party APIs. Furthermore, Bulkhead Isolation, Circuit Breakers, and Database-per-Service ensure 99.95% availability, strict security compliance, and fault tolerance under high-load conditions.]