## Overview
The Online Bookstore system is an AWS-hosted e-commerce platform built for 1 million MAU, delivering catalog browsing, secure checkout, reviews, and personalized recommendations. It ensures high scalability, GDPR/CCPA compliance, and multi-currency support across global regions.

## Key Elements
- Customers [person]
- Store Administrators [person]
- Web App Frontend (React, Next.js, TypeScript) [container]
- API Gateway (Amazon API Gateway) [container]
- Catalog & Search Service (Java, Spring Boot, Amazon OpenSearch) [container]
- Checkout & Order Service (Go, gRPC/REST) [container]
- Recommendation Service (Python, FastAPI) [container]
- Admin Management Service (Java, Spring Boot) [container]
- Database Storage (Amazon Aurora PostgreSQL Global Database) [container]
- Caching Layer (Amazon ElastiCache (Redis)) [container]
- Identity Provider (AWS Cognito/Auth0) [externalSystem]
- Payment Gateway [externalSystem]

## Relationships
- Customers -> Web App Frontend: Browses catalog and manages cart [HTTPS / TLS 1.3 / OAuth 2.0]
- Web App Frontend -> API Gateway: Forwards user requests [HTTPS / REST / gRPC]
- API Gateway -> Catalog & Search Service: Routes catalog and search queries [gRPC over TLS]
- Catalog & Search Service -> Caching Layer: Reads/writes cached search hits and metadata [Redis Protocol over TLS]
- Catalog & Search Service -> Database Storage: Syncs catalog source-of-truth [PostgreSQL Protocol over TLS]
- Catalog & Search Service -> Amazon OpenSearch: Executes faceted search queries [TLS]
- Checkout & Order Service -> Payment Gateway: Processes financial transactions [HTTPS / REST APIs]

## Technology Stack
- Java & Spring Boot: Powers high-performance backend microservices including the Catalog & Search Service.
- Amazon OpenSearch: Provides high-speed keyword and faceted search capabilities.
- Amazon Aurora PostgreSQL Global Database: Ensures multi-region transactional persistence and ACID compliance.
- Amazon ElastiCache (Redis): Delivers sub-100ms caching for search results and metadata.
- AWS ECS with Fargate: Runs containerized microservices with auto-scaling based on CPU and concurrency.

## Rationale
This architecture uses decoupled microservices and multi-region AWS services to easily handle 1M MAU with 99.95% uptime. Caching layers, asynchronous CDC pipelines, and managed search engines guarantee sub-2-second page loads even under heavy traffic.