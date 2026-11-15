## Overview
The Localization Service manages multi-region localization, currency conversion, and geo-resolution for the Online Bookstore across three AWS regions. It ensures high availability and fast performance for 1 million monthly active users (MAU).

## Key Elements
- Localization Service Container (Node.js/Express, Amazon ECS on AWS Fargate)
- Translation Controller
- Translation Engine Component (i18next)
- Currency Conversion Component (with background sync worker)
- Geo-Resolution Component
- Localization Data Access Layer
- Amazon ElastiCache (Redis)
- Amazon Aurora PostgreSQL
- AWS Secrets Manager
- AWS CloudWatch and CloudWatch Logs

## Relationships
- API Gateway invokes Localization Service via gRPC over HTTP/2 with mTLS
- Localization Data Access Layer reads/writes translation bundles and currency rates from Amazon ElastiCache (Redis) [TCP/6379 with TLS]
- Localization Data Access Layer connects to Amazon Aurora PostgreSQL for persistent locale metadata [TCP/5432 with TLS]
- Currency Conversion Component fetches rates via TLS 1.3 from external financial APIs using credentials from AWS Secrets Manager
- Localization Service emits Prometheus metrics and audit logs to AWS CloudWatch

## Technology Stack
- Node.js & Express: Chosen for high throughput and low-latency gRPC request handling.
- `@grpc/grpc-js`: Enables secure gRPC over HTTP/2 communication with mTLS.
- Amazon ECS on AWS Fargate: Provides container orchestration with auto-scaling across AWS regions.
- Amazon ElastiCache (Redis): Delivers low-latency caching for translation bundles and currency exchange rates.
- Amazon Aurora PostgreSQL: Stores persistent locale metadata with encryption.
- AWS Secrets Manager: Secures external financial API keys.

## Rationale
This architecture uses containerized microservices on AWS Fargate combined with Redis caching to meet sub-2-second page load and 99.95% uptime requirements. Strict security controls, mTLS, and fallback mechanisms ensure global scalability, regional compliance, and resilience against external API failures.