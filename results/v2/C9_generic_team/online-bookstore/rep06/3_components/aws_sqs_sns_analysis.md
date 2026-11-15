## Overview
The Online Bookstore is a resilient, AWS-hosted e-commerce platform designed to process book sales, recommendations, and reviews at a scale of 1 million Monthly Active Users. It utilizes a decoupled, event-driven microservices architecture to ensure high availability, low latency, and compliance with GDPR and CCPA.

## Key Elements
- **Users**: Customers browsing and purchasing books.
- **Client Tier**: AWS CloudFront (CDN), Amazon S3 (Static Assets).
- **Edge Tier**: AWS API Gateway (BFF and Routing).
- **Core Containers**: ECS/EKS Docker Containers for Catalog, Checkout, Recommendations, Reviews, and Compliance Workers.
- **Data & Caching Tier**: Amazon Aurora/RDS (Relational DB), Amazon ElastiCache (Redis).
- **Messaging Infrastructure**: AWS SNS, AWS SQS, and Dead Letter Queues (DLQ).
- **External Systems**: Payment Gateways, Third-Party Shipping APIs, Forex/Currency Rate API, Notification Service.

## Relationships
- **Customers -> AWS CloudFront**: HTTPS / TLS 1.3 for browsing and checkout.
- **AWS CloudFront -> Amazon S3**: Static content retrieval [HTTPS].
- **Client Tier -> AWS API Gateway**: REST/GraphQL over [HTTPS].
- **AWS API Gateway -> ECS/EKS Core Containers**: Internal routing and service invocation [gRPC/JSON].
- **Core Containers -> Amazon Aurora/RDS & Amazon ElastiCache**: Data persistence and caching [SQL/Redis Protocol].
- **Core Containers -> AWS SNS / SQS**: Asynchronous event publishing and subscription [AMQP/JSON].
- **Core Containers -> External Systems**: Third-party API integrations for shipping and payments [HTTPS].

## Technology Stack
- **Cloud Provider**: AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
- **Compute**: Amazon ECS/EKS with Docker for microservices containerization.
- **Messaging**: AWS SNS/SQS with JSON schemas, DLQs, and wrapper envelopes for event-driven decoupling.
- **Database & Cache**: Amazon Aurora/RDS for ACID-compliant transactions and Amazon ElastiCache (Redis) for fast caching.
- **Security & Observability**: AWS IAM (least privilege), AWS CloudWatch (metrics/alarms), and AWS KMS (encryption at rest).

## Rationale
This event-driven microservices architecture guarantees high availability (99.95% uptime) and low latency under peak loads by decoupling heavy transactional workflows via SQS/SNS. Furthermore, multi-region AWS deployment combined with strict security baselines ensures robust global performance and regulatory compliance (GDPR/CCPA).