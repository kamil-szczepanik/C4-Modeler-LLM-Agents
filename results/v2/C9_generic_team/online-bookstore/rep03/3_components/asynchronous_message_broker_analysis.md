## Overview
The Online Bookstore is an Amazon-style e-commerce platform built on AWS to support secure book sales, user reviews, and personalized recommendations. It handles 1 million MAU across multiple regions while maintaining GDPR and CCPA compliance.

## Key Elements
- Customers, Content Moderators, Operations Personnel, Customer Support Agents
- Storefront Frontend (SPA) (AWS S3, Amazon CloudFront)
- Edge Security & WAF (AWS WAF)
- API Gateway / BFF (AWS API Gateway)
- Core Domain Services (AWS ECS / EKS)
- Asynchronous Message Broker (AWS SQS/SNS with DLQ)
- Background Workers (AWS ECS / Lambda)
- Persistence Layer (Amazon RDS, Amazon OpenSearch)
- External Systems (Payment Gateways, Shipping Providers, Tax Calculation Service)

## Relationships
- Storefront Frontend (SPA) -> Edge Security & WAF: Inspects traffic [HTTPS]
- Edge Security & WAF -> API Gateway / BFF: Routes validated requests [HTTPS]
- API Gateway / BFF -> Core Domain Services: Invokes business logic [gRPC/REST]
- Core Domain Services -> Asynchronous Message Broker: Publishes events [AMQP/HTTPS]
- Asynchronous Message Broker -> Background Workers: Triggers background tasks [AMQP/HTTPS]
- Background Workers -> External Systems: Integrates with third-party APIs [HTTPS]

## Technology Stack
- Cloud Infrastructure: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region high availability.
- Frontend: AWS S3 and Amazon CloudFront for static asset delivery and global caching.
- Compute & Orchestration: AWS ECS / EKS for containerized core services and background workers.
- Messaging: AWS SQS/SNS with Dead Letter Queue (DLQ) for fault-tolerant asynchronous event-driven processing.
- Caching & Search: Amazon ElastiCache (Redis) and Amazon OpenSearch for performant catalogue search.

## Rationale
This AWS-native, distributed architecture scales dynamically to handle 1 million MAU with sub-2-second page loads globally. Asynchronous decoupling via SQS/SNS ensures 99.95% uptime and resilient integrations with third-party shipping and payment providers.