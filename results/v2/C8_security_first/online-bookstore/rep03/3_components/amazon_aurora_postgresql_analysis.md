## Overview
[The Online Bookstore system provides scalable catalogue browsing, secure multi-currency checkouts, reviews, and recommendations for 1M MAU. It utilizes AWS microservices backed by Amazon Aurora PostgreSQL to ensure high availability and GDPR/CCPA compliance.]

## Key Elements
*   [Shopper / Reviewer and Store Administrator]
*   [Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)]
*   [AWS API Gateway & AWS WAF]
*   [Catalogue, Cart & Checkout, Review, and Localization Services (AWS ECS Fargate)]
*   [Amazon Aurora PostgreSQL (Aurora Serverless v2, Multi-AZ, AWS RDS Proxy)]
*   [Amazon DynamoDB and Amazon ElastiCache (Redis)]
*   [External Payment Gateways and Third-Party Shipping APIs]

## Relationships
*   [Shopper -> Amazon CloudFront: HTTPS/TLS 1.3]
*   [SPA -> AWS API Gateway: REST/HTTPS]
*   [API Gateway -> AWS ECS Fargate Services: Internal VPC routing]
*   [ECS Fargate Services -> AWS RDS Proxy: SQL over TLS 1.3 (`sslmode=verify-full`)]
*   [AWS RDS Proxy -> Amazon Aurora PostgreSQL Engine: Internal VPC connection]
*   [Amazon Aurora PostgreSQL Engine -> Aurora Distributed Storage: 6-way replication across 3 AZs]

## Technology Stack
*   [AWS ECS Fargate: Container orchestration for microservices without server management]
*   [Amazon Aurora PostgreSQL: Transactional relational database with Serverless v2 for auto-scaling]
*   [AWS RDS Proxy: Connection pooling to prevent database exhaustion during checkout bursts]
*   [AWS KMS: Customer-managed keys (CMKs) for storage, backup, and PII encryption]
*   [Flyway / Liquibase: CI/CD schema migrations through RDS Proxy]

## Rationale
[Aurora Serverless v2 and Multi-AZ deployments guarantee 99.95% uptime and auto-scale compute for 1M MAU while controlling costs. Strict encryption, RDS Proxy connection pooling, and multi-region read replicas ensure GDPR/CCPA compliance and sub-2-second page loads globally.]