## Overview
[An Amazon-style e-commerce site providing physical and electronic book sales, personalized recommendations, and reviews. Built to handle 1M MAU across global regions with strict GDPR/CCPA compliance.]

## Key Elements
* **Users:** Customer (Shopper), Reviewer, Store Administrator
* **Frontend:** Single Page Application (React / TypeScript) via Amazon S3 and Amazon CloudFront
* **Edge/Routing:** Amazon API Gateway / Application Load Balancer
* **Core Services (AWS ECS / Fargate):** Catalogue & Search Service, Checkout & Cart Service, Recommendation Service, Review Service
* **Data & Caching:** Amazon RDS (PostgreSQL with read replicas), Amazon ElastiCache (Redis), Amazon OpenSearch
* **Messaging & Streaming:** Amazon SQS / SNS (with DLQ), Amazon Kinesis
* **External Systems:** Payment Gateway, Shipping Provider APIs, Identity & Notification Service

## Relationships
* **SPA to API Gateway:** HTTPS / JSON
* **API Gateway to Core Services:** HTTPS / REST
* **Service-to-Service:** gRPC with mTLS via AWS App Mesh / Envoy sidecars
* **Streaming:** Event capture via Amazon Kinesis, feeding the Recommendation Service
* **Asynchronous Messaging:** Transactional Outbox Pattern to Amazon SQS for shipping and payment APIs

## Technology Stack
* **Cloud Infrastructure:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region presence
* **Compute:** Amazon ECS with AWS Fargate for operational simplicity and container orchestration
* **Database & Search:** Amazon RDS PostgreSQL (with regional data residency) and Amazon OpenSearch for R-01 catalogue search
* **Caching:** Amazon ElastiCache (Redis) for sub-50ms recommendation lookups
* **Observability & Security:** OpenTelemetry, AWS CloudWatch, AWS Secrets Manager, and AWS KMS for encryption with CMKs

## Rationale
[AWS Fargate combined with Amazon CloudFront and ElastiCache ensures sub-2-second page loads globally while scaling dynamically to 1M MAU. Regional database endpoints, PII masking, and outbox patterns enforce GDPR/CCPA compliance and 99.95% availability.]