## Overview
Amazon-style e-commerce platform for physical and electronic books with recommendations, reviews, and multi-currency support. Engineered to handle 1M MAU on AWS with high availability and low latency.

## Key Elements
- **Users**: Customers, Content Moderators, Operations Personnel, Customer Support Agents
- **Frontend Containers**: Storefront Frontend (SPA) via AWS S3 and Amazon CloudFront; Edge Security & WAF via AWS WAF
- **Backend Containers**: API Gateway / BFF (AWS API Gateway); Core Domain Services (AWS ECS / EKS); Background Workers (AWS ECS / Lambda)
- **Data & Caching Containers**: Caching Layer (Amazon ElastiCache (Redis)); Persistence Layer (Amazon RDS, Amazon OpenSearch)
- **Integration & Monitoring**: Asynchronous Message Broker (AWS SQS/SNS with DLQ); Observability (AWS CloudWatch, X-Ray)

## Relationships
- Storefront Frontend (SPA) -> API Gateway / BFF: HTTPS / WSS
- API Gateway / BFF -> Core Domain Services: gRPC / REST over TCP
- Core Domain Services -> Caching Layer (Amazon ElastiCache (Redis)): TCP
- Core Domain Services -> Persistence Layer (Amazon RDS, OpenSearch): SQL / HTTPS over TCP
- Core Domain Services -> Asynchronous Message Broker (AWS SQS/SNS): HTTPS / AMQP

## Technology Stack
- **Caching Layer**: Amazon ElastiCache (Redis) with Cache-Aside pattern, `volatile-lru` eviction, and Redlock distributed locking.
- **Compute & Orchestration**: AWS ECS / EKS for Core Domain Services; AWS Lambda for background execution.
- **Storage & Search**: Amazon RDS for relational transactional data; Amazon OpenSearch for catalogue search.
- **Infrastructure & Delivery**: AWS S3 and Amazon CloudFront (CDN/Geo-DNS); AWS WAF for edge security.

## Rationale
AWS-native microservices ensure elasticity to handle 1M MAU while maintaining sub-2-second page loads. Redis caching with multi-AZ replication, circuit breakers, and Stale-While-Revalidate guarantees 99.95% availability.