## Overview
The Online Bookstore is a scaled-down e-commerce platform built on AWS supporting 1M MAU across three global regions. It provides catalog browsing, secure checkout, reviews, and personalized recommendations.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: Payment Gateway, Shipping Providers, Tax Calculation Service, Notification Service, SIEM Provider, Compliance/Archival Store, Global CDN & WAF
- **Containers**: SPA/Mobile Client, API Gateway, Catalog Service, Order & Checkout Service, Recommendation Service, Review Service, Asynchronous Message Broker (AWS SQS/SNS), Amazon ElastiCache, Segregated Isolated Data Stores, AWS Secrets Manager / Parameter Store

## Relationships
- Customer/Admin -> SPA/Mobile Client: HTTPS over TLS 1.3
- SPA/Mobile Client -> API Gateway: REST / GraphQL via HTTPS
- API Gateway -> Microservices (Catalog, Order, Recommendation, Review): Internal REST / gRPC
- Microservices -> Asynchronous Message Broker (AWS SQS/SNS): Publishes/consumes asynchronous events
- Microservices -> Amazon ElastiCache / Data Stores: Redis protocol / JDBC over TLS

## Technology Stack
- **Compute/API**: AWS API Gateway, Microservices (Java/Spring Boot or Node.js, Python for Machine Learning)
- **Messaging**: AWS SQS/SNS, AWS Kinesis / SQS archive for event replay
- **Caching/Storage**: Amazon ElastiCache (Redis), segregated isolated relational/NoSQL stores
- **Security/Governance**: AWS WAF, AWS Secrets Manager, AWS Glue Schema Registry / JSON Schema, AsyncAPI
- **Testing/Ops**: LocalStack, Pact for contract testing, CloudWatch for metrics and tracing

## Rationale
This microservices architecture utilizing AWS managed services ensures high availability (99.95% uptime) and scalability to handle 1M MAU. Asynchronous messaging via SQS/SNS decouples services, while strict schema validation, idempotency, and multi-region deployment guarantee data integrity, disaster recovery, and compliance with GDPR and CCPA.