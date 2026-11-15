## Overview
The Online Bookstore system is a multi-region retail e-commerce platform providing scalable book browsing, secure checkout, reviews, and personalized recommendations. The Catalog Service specifically manages public catalog browsing, keyword search, currency conversion, and event emission for recommendations.

## Key Elements
- **Catalog Controller (Express Router)**: Handles incoming HTTP/gRPC requests, input validation, and asynchronous event dispatch.
- **Search & Browse Engine**: Manages keyword search, input sanitization, SQL queries, and metadata faceting.
- **Currency Conversion Client**: Integrates with the external Currency Exchange API using a circuit breaker and Amazon ElastiCache (Redis) for cached rates.
- **Event Publisher**: Emits domain events using the AWS SDK.
- **External Dependencies**: Envoy Service Mesh, Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Currency Exchange API, and Amazon EventBridge.

## Relationships
- **Envoy Service Mesh -> Catalog Controller**: Routes incoming catalog requests [gRPC over mTLS / HTTPS over TLS]
- **Catalog Controller -> Search & Browse Engine**: Executes internal operations [TypeScript]
- **Catalog Controller -> Event Publisher**: Dispatches domain events [TypeScript]
- **Search & Browse Engine -> Amazon Aurora PostgreSQL**: Queries catalog and faceted data [PostgreSQL Wire Protocol over TLS 1.3]
- **Currency Conversion Client -> Currency Exchange API**: Fetches live exchange rates [REST/JSON over HTTPS]
- **Currency Conversion Client -> Amazon ElastiCache (Redis)**: Reads and writes cached rates [RESP over TLS]
- **Event Publisher -> Amazon EventBridge**: Emits book view events [HTTPS over TLS with AWS KMS]

## Technology Stack
- **Node.js & Express**: Core runtime and framework for lightweight, fast request handling.
- **TypeScript**: Ensures type safety across internal component communications.
- **AWS ECS on Fargate**: Container orchestration ensuring auto-scaling and high availability.
- **Amazon Aurora PostgreSQL**: Relational database with cross-region read replicas for low-latency queries.
- **Amazon ElastiCache (Redis)**: In-memory cache for fast currency rate lookups and offline fallbacks.
- **Opossum (Node.js Library)**: Circuit breaker implementation for resilience against third-party API failures.
- **AWS KMS & TLS 1.3**: Secures data in transit and at rest for compliance and OWASP mitigation.

## Rationale
This architecture uses containerized microservices deployed across multiple AWS regions to easily exceed the 1M MAU scalability requirement and maintain 99.95% uptime. Caching, circuit breaking, and cross-region database replicas guarantee sub-second performance on 3G connections while adhering to strict security and compliance mandates.