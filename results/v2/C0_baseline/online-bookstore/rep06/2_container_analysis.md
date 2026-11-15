## Overview
[An Amazon-style online bookstore providing catalogue browsing, secure checkout, reviews, and recommendations for 1M MAU across three global AWS regions.]

## Key Elements
• Book Buyers, Registered Reviewers, Store Administrators
• React/Next.js SPA frontend in AWS S3 and CloudFront CDN
• AWS API Gateway for routing, rate-limiting, and JWT validation
• ECS Fargate containers: Catalog & Search, Order & Checkout, Recommendation, Pricing & Localization
• AWS RDS PostgreSQL, AWS OpenSearch, and AWS ElastiCache (Redis)
• AWS EventBridge/SNS-SQS for event-driven messaging
• External Systems: Payment Gateway, Shipping APIs, Tax & Compliance Service, Identity Provider

## Relationships
• Users to SPA via HTTPS/REST/GraphQL
• SPA to API Gateway via HTTPS/REST/GraphQL
• API Gateway to ECS Fargate containers via gRPC over HTTP/2 and mTLS
• Containers to RDS PostgreSQL and OpenSearch via TCP/TLS
• Containers to ElastiCache Redis via encrypted TCP
• Containers to AWS EventBridge/SNS-SQS via HTTPS

## Technology Stack
• React/Next.js: Chosen for high-performance SPA delivery via CDN
• Node.js/Go, Java/Spring Boot, Python/FastAPI: Polyglot backend optimized for search, ACID checkout, and recommendations
• AWS ECS Fargate: Standardized container orchestration ensuring zero-downtime deployments
• AWS RDS PostgreSQL: ACID-compliant relational storage with strict isolation for GDPR/CCPA
• AWS OpenSearch & ElastiCache: High-speed catalogue search and session/rate caching
• AWS Route 53 & CloudWatch: Global latency-based routing and centralized logging

## Rationale
[Standardized ECS Fargate containers combined with managed AWS services ensure 99.95% uptime, sub-second latency, and multi-region scalability for 1M MAU. Strict network isolation, encryption, and regional replication satisfy OWASP mitigations and GDPR/CCPA compliance.]