## Overview
The Online Bookstore is a globally scaled e-commerce system providing physical and electronic book sales, recommendations, and reviews. Its core purpose is delivering a reliable, secure, and performant shopping experience across multiple regions.

## Key Elements
- Customers and Bookstore Administrators
- Single Page Application (SPA) (React, AWS S3, CloudFront)
- API Gateway / Envoy (AWS API Gateway, AWS App Mesh)
- Core Microservices (AWS ECS/Fargate)
- Catalog Service, Checkout & Cart Service, Recommendation Service, Review & Rating Service, Moderation Worker
- Async Event Bus (Amazon EventBridge, SNS, SQS)
- Data Stores (AWS RDS PostgreSQL, DynamoDB, Elasticsearch)
- External Systems (Payment Gateway, Tax Service, Shipping APIs)

## Relationships
- SPA -> API Gateway / Envoy: Routes user traffic via HTTPS
- API Gateway -> Core Microservices: Forwards authenticated requests via mTLS (AWS App Mesh)
- Checkout Service -> Payment Gateway: Processes transactions via HTTPS/JSON
- Core Microservices -> Async Event Bus: Publishes and consumes domain events via JSON over SNS/SQS
- Internal Components -> Data Stores: Reads and writes data via PostgreSQL protocol, DynamoDB API, and Elasticsearch API

## Technology Stack
- Cloud Infrastructure: AWS across us-east-1, eu-west-1, ap-southeast-1 for global availability
- Containers & Orchestration: AWS ECS/Fargate with AWS App Mesh for service mesh routing
- Languages: Go (Catalog, Checkout), Python (Recommendations, Moderation), Node.js (Reviews)
- Datastores: PostgreSQL for transactional data, Elasticsearch for search, DynamoDB for operational data
- Security: AWS KMS for encryption-at-rest, AWS Secrets Manager for credentials, SPIFFE/SPIRE IDs for service authorization

## Rationale
This architecture isolates critical revenue-generating flows like checkout from non-critical paths like recommendations to prevent cascading failures under heavy load. The distributed AWS deployment combined with decoupled microservices ensures high availability (99.95%), low latency, and strict GDPR/CCPA compliance.