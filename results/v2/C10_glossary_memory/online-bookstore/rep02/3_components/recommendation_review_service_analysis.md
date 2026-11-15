## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations for physical and electronic books. It ensures high performance, security, and scalability for 1 million monthly active users globally.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA
- AWS API Gateway
- Recommendation & Review Service (Python/FastAPI on AWS ECS on Fargate)
- Recommendation Engine (AWS Personalize)
- Amazon RDS
- Redis on Amazon ElastiCache
- Amazon SQS
- AWS Secrets Manager
- Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA [HTTPS (TLS 1.3)]
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway [HTTPS]
- AWS API Gateway -> Recommendation & Review Service [gRPC over TLS with mutual TLS via AWS App Mesh]
- Recommendation & Review Service -> Recommendation Engine [REST over HTTPS with circuit breakers]
- Recommendation & Review Service -> Redis on Amazon ElastiCache [RESP with TLS]
- Recommendation & Review Service -> Amazon RDS [AWS SDK]
- Recommendation & Review Service -> Amazon SQS [AWS SDK]
- Recommendation & Review Service -> AWS Secrets Manager [AWS SDK]
- Recommendation & Review Service -> Centralized Logging & SIEM [HTTPS / AWS Infrastructure]

## Technology Stack
- **Python / FastAPI**: Chosen for efficient async I/O handling, non-blocking background tasks, and low latency on AWS ECS on Fargate.
- **AWS Personalize**: Provides machine learning-driven book recommendations via REST over HTTPS.
- **Redis on Amazon ElastiCache**: Serves high-frequency read requests with cache-aside pattern to protect database availability.
- **Amazon SQS**: Decouples asynchronous telemetry and analytics event processing.
- **AWS App Mesh & IAM**: Enforces mutual TLS, zero-trust service communication, and least-privilege security controls.

## Rationale
This architecture uses containerized microservices on AWS ECS with caching and asynchronous queues to absorb traffic spikes for 1M MAU while keeping page loads under 2 seconds. Layered security, circuit breakers, and automated data masking ensure GDPR compliance and 99.95% uptime availability.