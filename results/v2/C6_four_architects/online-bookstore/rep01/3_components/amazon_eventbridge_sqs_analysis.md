## Overview
The Online Bookstore system is a scalable Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews. It utilizes a resilient event-driven architecture hosted on AWS to support global users with high availability.

## Key Elements
- **Users:** Customer, Admin/Support Staff
- **External Systems:** Payment Gateway, Shipping Provider APIs, Identity Provider, Notification Service, Recommendation Service, Tax Calculation Service
- **Frontends:** Customer SPA, Admin SPA (React, Amazon S3, CloudFront)
- **API Layer:** AWS API Gateway, AWS WAF
- **Core Services:** Catalog & Search Service (Spring Boot, OpenSearch), Order & Checkout Service (Node.js), Recommendation Service (Python, FastAPI), Async Worker, Digital Asset Delivery Service (Go)
- **Messaging & Eventing:** Amazon EventBridge & SQS (Event Bus, Checkout Queue, Digital Asset Queue, Notification Queue, General DLQ, Event Archive, Cross-Region Event Rule, CloudWatch Alarms, SQS KMS Encryption)
- **Data & Caches:** Amazon Aurora PostgreSQL (Global Tables), Amazon DynamoDB, Redis ElastiCache, Amazon S3 (Digital Assets with CloudFront Signed URLs)
- **Observability:** AWS Distro for OpenTelemetry (ADOT Sidecar)

## Relationships
- **Customer SPA / Admin SPA -> AWS API Gateway:** Routes frontend traffic [HTTPS / REST & GraphQL]
- **AWS API Gateway -> Core Services:** Forwards authenticated requests [HTTP / gRPC]
- **Order & Checkout Service -> Event Bus (Amazon EventBridge):** Publishes domain events [HTTPS / AWS SDK]
- **Event Bus -> Checkout Queue / Digital Asset Queue / Notification Queue (AWS SQS):** Forwards filtered domain events [AWS SNS/SQS integration]
- **Checkout Queue -> Async Worker:** Pulls messages for background execution [SQS Long Polling]
- **Digital Asset Queue -> Digital Asset Delivery Service:** Pulls messages to provision downloads [SQS Long Polling]
- **Event Bus -> Cross-Region Event Rule:** Replicates critical domain events across regions [Cross-Region AWS API / HTTPS]
- **Queues -> General DLQ (AWS SQS):** Forwards failed messages after max retries [AWS Redrive Policy]
- **General DLQ -> DLQ CloudWatch Alarms:** Emits depth metrics for operational monitoring [CloudWatch Metric Integration]

## Technology Stack
- **Cloud Provider:** AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
- **Frontend:** React hosted on Amazon S3 and distributed via Amazon CloudFront for low-latency global delivery.
- **Backend Services:** Node.js, Spring Boot, Python FastAPI, and Go for microservice efficiency.
- **Messaging:** Amazon EventBridge and AWS SQS with AWS KMS encryption for decoupled, secure asynchronous communication.
- **Databases:** Amazon Aurora PostgreSQL with Global Tables and Amazon DynamoDB for scalable, multi-region persistence.
- **Caching & Search:** Redis ElastiCache and Amazon OpenSearch for high-performance catalogue search and caching.

## Rationale
This event-driven, microservices-based AWS architecture ensures horizontal scalability to handle 1M MAU while meeting strict 99.95% availability targets. Utilizing asynchronous message queues and multi-region replication decouples critical checkouts from background fulfillment, guaranteeing sub-2-second page loads and compliance with GDPR/CCPA.