## Overview
An AWS-hosted microservices architecture for the Online Bookstore, providing real-time book reviews, ratings, and personalized recommendations. Built for scalability, it handles 1 million MAU across three global regions with strict GDPR/CCPA compliance.

## Key Elements
- Book Buyer / Registered Reviewer & Store Administrator (Users)
- Amazon API Gateway (API Gateway)
- Recommendation & Review Service (Python FastAPI Container on Amazon ECS Fargate)
- Review API Controller & Recommendation API Controller (Components)
- Moderation Pipeline Component & Review Aggregator Component (Components)
- Notification Dispatcher Component (Component)
- Amazon SQS / SNS (Asynchronous Event Bus)
- Amazon ElastiCache Redis (Caching Datastore)
- Amazon Aurora PostgreSQL (Primary Database)
- External Notification Service & Catalogue Service

## Relationships
- Users -> Amazon API Gateway: Submits reviews and requests recommendations via mTLS and gRPC
- Amazon API Gateway -> Recommendation & Review Service: Routes requests using AWS Signature V4 and IAM
- Review API Controller -> Moderation Pipeline Component: Offloads moderation via Amazon SQS
- Review API Controller -> Review Aggregator Component: Updates rating cache via local method call
- Catalogue Service -> Review Aggregator Component: Fetches product ratings via mTLS and gRPC
- Notification Dispatcher Component -> External Notification Service: Triggers review emails via REST/HTTPS

## Technology Stack
- Python (FastAPI): Chosen for high-performance asynchronous API endpoints
- Amazon ECS (Fargate): Container orchestration ensuring zero-downtime blue/green deployments
- Amazon SQS/SNS: Asynchronous messaging to decouple review ingestion and moderation
- Amazon ElastiCache Redis: Sub-millisecond global rating cache using Global Datasets
- AWS KMS & Secrets Manager: Encrypts data at rest with customer-managed keys and manages credentials
- OpenTelemetry: Provides distributed tracing across regional services

## Rationale
The architecture uses asynchronous queuing and Redis caching to ensure page loads under 2 seconds while maintaining a 99.95% uptime SLA. ECS Fargate auto-scaling and multi-region deployments effortlessly support 1 million MAU globally.