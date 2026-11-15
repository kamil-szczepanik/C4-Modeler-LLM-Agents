## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, offering catalog browsing, secure checkout, reviews, and personalized recommendations. It is architected on AWS across multiple global regions to deliver high availability and performance.

## Key Elements
- Storefront Frontend (SPA): AWS S3, Amazon CloudFront
- Edge Security & WAF: AWS WAF
- API Gateway / BFF: AWS API Gateway
- Core Domain Services: AWS ECS / EKS (gRPC, REST)
- Caching Layer: Amazon ElastiCache (Redis)
- Asynchronous Message Broker: AWS SQS/SNS with Dead Letter Queue (DLQ)
- Background Workers: AWS ECS / Lambda
- Persistence Layer: Amazon RDS, Amazon OpenSearch
- Observability & Synthetic Monitoring: AWS CloudWatch, AWS X-Ray

## Relationships
- Storefront Frontend (SPA) -> Edge Security & WAF: Routes user traffic [HTTPS]
- Edge Security & WAF -> API Gateway / BFF: Forwards inspected traffic [HTTPS]
- API Gateway / BFF -> Core Domain Services: Invokes backend business logic and aggregates responses [gRPC / REST]
- Core Domain Services -> Caching Layer: Reads and writes session/catalog data [Redis Protocol]
- Core Domain Services -> Persistence Layer: Executes queries and indexes data [PostgreSQL Wire Protocol, OpenSearch API]
- Core Domain Services -> Asynchronous Message Broker: Publishes domain events [AWS SQS/SNS]

## Technology Stack
- AWS API Gateway: Selected for native routing, rate limiting, and supporting the 99.95% uptime SLA.
- AWS ECS / EKS: Chosen to run containerized core domain services with horizontal scalability.
- Amazon ElastiCache (Redis): Deployed for low-latency caching to meet performance requirements on 3G networks.
- Amazon RDS & OpenSearch: Utilized for relational transaction integrity and fast keyword catalog search.
- AWS SQS/SNS: Implemented for asynchronous decoupling and reliable background processing.

## Rationale
This microservices-based AWS architecture ensures horizontal scalability to handle 1 million MAU without performance degradation. Edge caching, API aggregation, and strict security controls collectively guarantee rapid page loads and robust data protection.