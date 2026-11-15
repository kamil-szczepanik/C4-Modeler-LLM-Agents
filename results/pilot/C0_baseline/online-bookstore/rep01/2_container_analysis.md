## Overview
[An Amazon-style online bookstore providing physical and electronic book sales, recommendations, reviews, and secure global checkout.]
[Engineered to scale for 1 million MAU with 99.95% uptime while ensuring GDPR, CCPA, and PCI-DSS compliance.]

## Key Elements
- Customers and Administrators (Users)
- React Single Page Application (Client Tier)
- Amazon CloudFront & AWS WAF (CDN & Edge Security)
- Amazon ECS Fargate Go Microservices (Backend Container Tier)
- Amazon Aurora PostgreSQL (Transactional Database)
- AWS DynamoDB (Catalogue & Recommendations Database)
- Amazon SQS & SNS (Event-Driven Messaging)
- Redis (Currency & Exchange Rate Caching)
- Third-Party Shipping Providers, Payment Gateway APIs, Global Tax and Currency Conversion Service, Transactional Email and SMS Service Provider (External Systems)

## Relationships
- Customers interact with the React SPA via HTTPS (TLS 1.3) through Amazon CloudFront and AWS WAF.
- React SPA communicates with ECS Fargate microservices using HTTPS and gRPC.
- Go microservices communicate internally using gRPC with mTLS and short-lived JWTs.
- Microservices persist transactional data to Amazon Aurora PostgreSQL and catalogue data to AWS DynamoDB using TLS 1.3 and AES-256.
- Order Fulfillment and Notification Dispatcher microservices consume messages from Amazon SQS.
- Currency Service reads exchange rates from Redis and external Global Tax and Currency Conversion Service.
- System integrates securely with Third-Party Shipping Providers and Payment Gateway APIs via restricted egress security groups.

## Technology Stack
- Frontend: React SPA served via Amazon CloudFront for optimized global delivery.
- Backend Compute: Go microservices running on Amazon ECS Fargate for high throughput and low-latency performance.
- Databases: Amazon Aurora PostgreSQL for ACID-compliant transactional data; AWS DynamoDB for high-velocity catalogue and recommendation reads.
- Caching & Messaging: Redis for multi-currency exchange rate caching; Amazon SQS and SNS for asynchronous event-driven workflows.
- Security & Infrastructure: AWS IAM, KMS (AES-256), AWS WAF, mTLS, JWTs, Terraform for Infrastructure-as-Code, and AWS CodeDeploy for blue/green deployments.
- Observability: AWS X-Ray for distributed tracing, Prometheus and Grafana for resource monitoring, and AWS CloudWatch.

## Rationale
[Go microservices on ECS Fargate paired with Aurora PostgreSQL and DynamoDB deliver the sub-second page load times and horizontal scalability required for 1M MAU.]
[Rigorous multi-region AWS deployment across us-east-1, eu-west-1, and ap-southeast-1 with SQS decoupling ensures 99.95% availability and robust fault tolerance.]