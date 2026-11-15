## Overview
This system is an Amazon-style online bookstore designed to handle 1 million monthly active users with multi-region AWS deployment. Its core purpose is to provide catalogue browsing, secure checkout, personalized recommendations, reviews, and secure digital asset delivery.

## Key Elements
* Customers & Admin Staff (Users)
* Customer SPA & Admin SPA (React, Amazon S3, CloudFront)
* AWS API Gateway with AWS WAF & Amazon Cognito (Auth/BFF)
* Core Backend Containers: Catalog & Search (Spring Boot/OpenSearch), Order & Checkout (Node.js), Recommendation (Python/FastAPI), Async Worker, Digital Asset Delivery (Go)
* Async Event Bus: Amazon EventBridge & AWS SQS
* Data Layer: Amazon Aurora PostgreSQL (Global Tables), Amazon DynamoDB, Redis (ElastiCache)
* Observability: AWS Distro for OpenTelemetry (ADOT) sidecar

## Relationships
* Customers and Admin Staff connect to SPAs via HTTPS, and authenticate via HTTPS/OIDC using Amazon Cognito.
* SPAs communicate with the API Gateway via HTTPS/WSS, protected by AWS WAF edge filtering.
* API Gateway routes internal traffic to backend containers using gRPC over TLS and HTTPS.
* Order & Checkout publishes asynchronous events via Amazon EventBridge and SQS to the Async Worker and Digital Asset Delivery containers.
* Backend containers connect to Aurora PostgreSQL, DynamoDB, and Redis via native database protocols over isolated VPC private subnets.
* Customers download e-books securely via HTTPS using CloudFront Signed URLs backed by Amazon S3.

## Technology Stack
* Frontend: React, deployed on Amazon S3 and distributed via Amazon CloudFront for <2s global page loads.
* Edge Security: AWS API Gateway, AWS WAF, and Amazon Cognito for OWASP Top-10 mitigations and OAuth2/OIDC.
* Backend Services: Spring Boot (Java), Node.js (TypeScript), Python (FastAPI), and Go to optimize specific domain workloads.
* Messaging & Events: Amazon EventBridge and AWS SQS for asynchronous domain decoupling and third-party API resilience.
* Databases: Amazon Aurora PostgreSQL (Multi-Region Global Tables) for transactional integrity, Amazon DynamoDB for recommendations, and Redis (ElastiCache) for session management.
* Observability: AWS Distro for OpenTelemetry (ADOT) for distributed tracing and CloudWatch integration.

## Rationale
This architecture uses multi-region AWS services and asynchronous decoupling via EventBridge to guarantee 99.95% uptime and fault tolerance against third-party shipping API failures. The combination of CloudFront, Redis caching, and specialized microservices guarantees sub-second keyword search and sub-2-second page loads under a 1M MAU scale.