## Overview
[An Amazon-style global e-commerce platform built to support 1M MAU for purchasing physical and electronic books, reviews, and recommendations.]
[Engineered for high availability, sub-second latency, and strict multi-region compliance across US, EU, and APAC.]

## Key Elements
* Users: Customers, Admin/Operations
* Frontend: React Single-Page Application (SPA)
* API Layer: Amazon API Gateway
* Core Services (Containers): Catalog Service (Node.js/Express), Order & Checkout Service (Spring Boot), Recommendation Service (Python FastAPI)
* Data & Cache Stores: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch Service
* Messaging & Integration: Amazon EventBridge, Amazon SQS, Amazon SNS
* Infrastructure & Security: AWS ECS (Fargate), AWS App Mesh (mTLS), AWS Secrets Manager, AWS KMS

## Relationships
* Client to Frontend: HTTPS via Amazon CloudFront and Amazon S3
* Frontend to API Gateway: HTTPS/REST and GraphQL
* API Gateway to Services: gRPC over TLS via AWS App Mesh
* Inter-service Messaging: JSON over HTTPS via Amazon EventBridge, SQS, and SNS
* Services to Data Stores: TLS, IAM roles, and regional KMS CMKs

## Technology Stack
* Frontend: React hosted on AWS S3, distributed via Amazon CloudFront
* Compute & Orchestration: AWS ECS (Fargate) with Terraform/Helm for multi-region container deployments
* Runtimes: Node.js/Express (Catalog), Java Spring Boot (Checkout/Transactions), Python FastAPI (Recommendations)
* Databases & Search: Amazon RDS (PostgreSQL) for transactions, DynamoDB and OpenSearch for catalogue and search, ElastiCache (Redis) for sessions/carts
* Security & Observability: AWS App Mesh (mTLS), AWS KMS (CMKs), AWS Secrets Manager, OpenTelemetry sidecars with Datadog/CloudWatch

## Rationale
[A polyglot microservices architecture running on AWS ECS Fargate provides the horizontal scalability required to handle 1M MAU without degradation.]
[Managed AWS data stores, multi-region routing via Route 53, and zero-trust mTLS encryption ensure 99.95% uptime, sub-2s page loads, and GDPR/CCPA compliance.]