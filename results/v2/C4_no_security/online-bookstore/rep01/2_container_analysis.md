## Overview
[An Amazon-style global online bookstore enabling customers to browse catalogues, securely purchase books, read reviews, and receive personalized recommendations. The system is designed to support 1 million monthly active users globally while ensuring strict GDPR/CCPA compliance and high availability.]

## Key Elements
- **Users**: Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent
- **Frontend Container**: React/TypeScript Single-Page Application (SPA)
- **API Management**: Amazon API Gateway
- **Backend Containers**: Catalog & Search (Spring Boot/Java), Checkout & Order (Node.js), Recommendation (Python/FastAPI), Analytics Ingestion (Go), Notification (Asynchronous)
- **Data & Messaging**: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon OpenSearch, AWS SQS, AWS EventBridge, Amazon Kinesis
- **External Systems**: Payment Gateway, Shipping Provider API, Tax/Compliance Service, AWS Route 53, AWS SQS/EventBridge, Amazon DynamoDB

## Relationships
- **SPA to API Gateway**: HTTPS / REST & GraphQL
- **API Gateway to Core Containers**: HTTPS / JSON routing, rate limiting, and JWT validation
- **Inter-Container Communication**: Asynchronous messaging via AWS SQS and AWS EventBridge
- **Core Services to Databases**: TLS-encrypted JDBC/TCP connectors
- **Analytics Ingestion**: Real-time clickstream streaming via Amazon Kinesis

## Technology Stack
- **Frontend Hosting**: Amazon CloudFront / S3 for fast global content delivery
- **Compute**: AWS ECS (Fargate) for standardized container deployment and minimal runtime drift
- **Languages/Runtimes**: TypeScript (React), Java (Spring Boot), Node.js, Python (FastAPI), Go
- **Databases & Search**: Amazon RDS (PostgreSQL) for transactional data, Amazon DynamoDB for session/cart state, Amazon OpenSearch for catalog search
- **Observability & Management**: OpenTelemetry (OTel) sidecars, AWS Secrets Manager, ArgoCD for GitOps, AWS Route 53 for latency-based routing

## Rationale
[Standardizing on AWS ECS (Fargate) with multi-region deployments in us-east-1, eu-west-1, and ap-southeast-1 guarantees 99.95% uptime and low latency for 1M MAU. Isolating critical domains like checkout and recommendations ensures PCI-DSS compliance, data residency requirements, and fault tolerance during traffic surges.]