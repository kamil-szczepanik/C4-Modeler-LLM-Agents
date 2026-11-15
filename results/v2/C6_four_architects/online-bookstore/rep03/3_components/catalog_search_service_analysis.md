## Overview
The Online Bookstore system is a scalable e-commerce platform designed for purchasing physical and electronic books with integrated recommendations and reviews. It utilizes a microservices architecture hosted on AWS to deliver high performance and reliability.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: AWS CloudFront/Route 53, Stripe/PayPal, UPS/FedEx, Avalara, AWS SES/SNS, AWS Personalize, AWS Fraud Detector
- **Containers**: React Single Page Application, Amazon API Gateway, Catalog & Search Service (Spring Boot), Order & Checkout Service (Node.js), Payment & Currency Service (.NET Core), Recommendation & Review Service (Python), Data Privacy & User Service (Python), Admin & Content Management Service (.NET Core), Async Worker Service (Python)
- **Data & Caching Stores**: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch
- **Integration**: Amazon EventBridge, Amazon SQS
- **Catalog Components**: Search Controller, Catalog Controller, Search Service, Catalog Manager, Catalog Cache Manager, Event Consumer, Search Indexer, Catalog Domain Model, Catalog Security/Validation Interceptor, Catalog Circuit Breaker, Catalog Metrics & Telemetry Interceptor

## Relationships
- Amazon API Gateway -> Catalog & Search Service: Routes catalog and search requests [gRPC / HTTPS over TLS]
- Catalog & Search Service -> Amazon RDS (PostgreSQL): Reads and writes relational catalogue data [JDBC / SQL over TCP]
- Catalog & Search Service -> Amazon OpenSearch: Queries catalogue search indices [TCP / REST over HTTP]
- Catalog & Search Service -> Amazon ElastiCache (Redis): Caches search and catalogue data [Redis Protocol over TCP]
- Catalog & Search Service -> Amazon SQS / EventBridge: Handles asynchronous event ingestion and synchronization [AMQP / HTTPS]
- Catalog & Search Service -> Amazon CloudWatch: Exposes operational telemetry and metrics [HTTP / Prometheus format]

## Technology Stack
- **Frontend**: React, Amazon S3, Amazon CloudFront for high-speed content delivery
- **Backend Services**: Spring Boot (Java), Node.js, .NET Core, and Python for domain containers
- **Search & Caching**: Amazon OpenSearch for keyword indexing; Amazon ElastiCache (Redis) for sub-second data caching
- **Databases**: Amazon RDS (PostgreSQL) for transactional relational data; Amazon DynamoDB for NoSQL storage
- **Resilience & Observability**: Resilience4j for circuit breaking; Micrometer for metrics collection; Spring AOP for interception

## Rationale
This architecture uses a CQRS-lite pattern with separate search and relational data stores to ensure sub-2-second page loads under heavy traffic. The inclusion of caching, circuit breakers, and comprehensive telemetry guarantees 99.95% uptime and OWASP compliance while supporting global scalability.