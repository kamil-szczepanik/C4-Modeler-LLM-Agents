## Overview
An AWS-deployed e-commerce platform featuring microservices for catalogue, cart, reviews, and recommendations. It handles high-concurrency traffic with strict global compliance and multi-region resilience.

## Key Elements
- Customers
- API Gateway Container
- Frontend Container
- Core Domain Containers (Catalogue, Cart/Checkout, Recommendations, Reviews)
- Integration / Anti-Corruption Layer (ACL) Container
- Async Worker / Event Broker Container
- Caching/Session Container (Redis)
- Third-Party Services (Payment, Shipping, FX, Tax, Fraud)

## Relationships
- API Gateway Container -> Core Domain Containers: Routes client requests [Internal REST / gRPC]
- Core Domain Containers -> Caching/Session Container: Reads/writes session and frequent data [Redis Protocol]
- Core Domain Containers -> Async Worker / Event Broker Container: Publishes and consumes events [CloudEvents]
- Core Domain Containers -> Integration / Anti-Corruption Layer (ACL) Container: Requests external vendor APIs [Internal REST]

## Technology Stack
- AWS (us-east-1, eu-west-1, ap-southeast-1): Multi-region cloud infrastructure ensuring high availability.
- Redis: In-memory store for session caching and low-latency state access.
- OpenTelemetry & JSON Logging: Standardized distributed tracing and structured correlation for observability.
- OpenAPI & Protobuf: Contract definitions for microservice communication.
- Pact: Consumer-driven contract testing in CI/CD.

## Rationale
Microservice decomposition with strict database isolation guarantees independent scaling for 1M MAU while meeting 99.95% uptime targets. Region-localized state management and event-driven decoupling ensure GDPR compliance and resilient performance under regional network partitions.