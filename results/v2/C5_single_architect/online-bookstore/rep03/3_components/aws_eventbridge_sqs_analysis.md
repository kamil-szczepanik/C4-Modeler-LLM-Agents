## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It is designed to scale to 1 million monthly active users while maintaining high availability across global AWS regions.

## Key Elements
* **Customer & Administrator:** End-users interacting with the platform.
* **Single-Page App (SPA):** React frontend hosted via AWS S3 and distributed through Amazon CloudFront.
* **API Gateway:** AWS API Gateway managing incoming client requests.
* **Microservices:** Node.js NestJS containers running on Amazon ECS/Fargate (Catalog, Order & Checkout, Recommendation, Email Services).
* **Databases & Storage:** Amazon RDS PostgreSQL, Amazon OpenSearch, Amazon DynamoDB, and Amazon ElastiCache Redis.
* **Messaging Layer:** AWS EventBridge event bus, Amazon SQS queues, and SQS Dead Letter Queues (DLQs).
* **External Systems:** Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, and Tax Calculation Service.

## Relationships
* **SPA -> API Gateway:** Routes client requests [HTTPS / JSON].
* **API Gateway -> ECS Containers:** Forwards traffic to microservices [gRPC / REST].
* **Order & Checkout Service -> AWS EventBridge:** Publishes domain events [AWS SDK (PutEvents) / HTTPS / JSON].
* **AWS EventBridge -> SQS Queues:** Routes messages based on pattern rules [SQS Queue Policy / AWS internal API].
* **SQS Queues -> Recommendation & Email Services:** Polled by ECS tasks [AWS SDK (ReceiveMessage) / HTTPS].

## Technology Stack
* **Frontend:** React, AWS S3, Amazon CloudFront for low-latency global delivery.
* **Backend:** Node.js with NestJS running on Amazon ECS/Fargate for modular microservices.
* **Databases:** Amazon RDS PostgreSQL for relational data, DynamoDB for fast lookups, OpenSearch for catalogue search, and Redis for caching.
* **Messaging:** AWS EventBridge and Amazon SQS with DLQs for reliable, asynchronous event-driven decoupling.
* **Cloud Infrastructure:** Multi-region AWS (us-east-1, eu-west-1, ap-southeast-1).

## Rationale
This architecture uses serverless containers and managed AWS messaging primitives to meet the 99.95% uptime and 1M MAU scalability targets without operational overhead. Asynchronous event-driven decoupling via EventBridge and SQS prevents cascading failures during high-traffic checkout events.