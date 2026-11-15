## Overview
The Online Bookstore is a globally distributed e-commerce platform built to handle high-volume book browsing, secure checkout, and personalized recommendations. It leverages an AWS cloud-native microservices architecture to ensure high availability, low latency, and regulatory compliance.

## Key Elements
- **Users**: Customer, Bookstore Administrator
- **Frontend Container**: Single Page Application (React hosted on AWS S3 with CloudFront CDN)
- **API Gateway Container**: AWS API Gateway combined with Envoy proxy
- **Backend Containers**: Core Microservices (Node.js/Go/Python on AWS ECS/Fargate and AWS App Mesh)
- **Data & Storage**: AWS RDS PostgreSQL, DynamoDB, Elasticsearch, AWS ElastiCache (Redis)
- **External Systems**: Payment Gateway, Third-Party Fulfillment Partner, Shipping APIs, Identity Provider

## Relationships
- **Customer -> Single Page Application (SPA)**: Browses catalog and manages cart via [HTTPS]
- **Single Page Application (SPA) -> API Gateway / Envoy**: Sends API requests via [HTTPS/REST]
- **API Gateway / Envoy -> Core Microservices**: Routes authenticated requests via [gRPC over HTTP/2, mTLS (AWS App Mesh)]
- **API Gateway / Envoy -> AWS ElastiCache (Redis)**: Evaluates rate limits via [TCP]

## Technology Stack
- **AWS API Gateway & Envoy**: Edge routing, rate limiting, and OWASP defense
- **AWS WAF**: Edge-level blocking of web exploits and bot traffic
- **AWS App Mesh & mTLS**: Secure service-to-service communication and traffic encryption
- **AWS ECS/Fargate**: Container orchestration for scalable microservices execution
- **AWS ElastiCache (Redis)**: Distributed caching and rate-limit token bucket tracking
- **OpenTelemetry**: Distributed tracing and performance monitoring

## Rationale
This architecture uses Envoy and AWS Fargate to effortlessly scale past 1 million MAU while meeting the strict sub-2-second performance constraint. Decoupling edge security, rate limiting, and routing via managed AWS services guarantees the required 99.95% uptime and GDPR/CCPA compliance.