## Overview
[The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for 1 million monthly active users. Its core purpose is delivering a high-performance e-commerce experience with sub-2-second page loads and strict GDPR/CCPA compliance.]

## Key Elements
- Session Store Component (Redis Engine for active user carts and sessions)
- Product Catalog Cache Component (Redis Engine for book details and search aggregations)
- Recommendation Cache Component (Redis Engine for pre-computed recommendation vectors)
- Calling Services: Catalog & Search, Order & Checkout, Recommendation, and Localization Services (AWS ECS on AWS Fargate)
- Infrastructure & Management: AWS Secrets Manager, Amazon CloudWatch, and AWS KMS customer-managed keys

## Relationships
- Catalog & Search Service, Order & Checkout Service, Recommendation Service, and Localization Service -> Amazon ElastiCache via TCP (RESP protocol)
- Amazon ElastiCache -> AWS Secrets Manager via HTTPS for automated auth token rotation
- Amazon ElastiCache -> Amazon CloudWatch via AWS internal APIs for metric telemetry and alarm monitoring

## Technology Stack
- Redis Engine (v6/v7 on Amazon ElastiCache): Provides in-memory data structures for sub-millisecond retrieval and high throughput.
- Redis Cluster Mode with Global Datasets: Enables multi-AZ deployment and low-latency cross-region replication across us-east-1, eu-west-1, and ap-southeast-1.
- cache.r6g.xlarge Node Types: Delivers high memory performance optimized for caching workloads under heavy traffic.
- TLS In-Transit Encryption & AWS KMS At-Rest Encryption: Secures sensitive user cart data and satisfies GDPR/CCPA compliance mandates.

## Rationale
[This architecture guarantees the 99.95% uptime and sub-2-second page load requirements by utilizing an isolated, highly scalable, and encrypted multi-region caching layer. It protects user cart and session states while preventing cache degradation during peak load spikes for 1M MAU.]