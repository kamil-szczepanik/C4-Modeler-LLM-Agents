## Overview
- An Amazon-style e-commerce Online Bookstore providing physical and electronic books, search, cart, secure checkout, reviews, and recommendations.
- Built to handle 1M MAU with 99.95% uptime while ensuring GDPR and CCPA compliance.

## Key Elements
- Customer SPA & Admin SPA (React, Amazon S3, CloudFront)
- AWS API Gateway & AWS WAF
- Catalog & Search Service (Spring Boot, OpenSearch)
- Order & Checkout Service (Node.js)
- Recommendation Service (Python, FastAPI)
- Digital Asset Delivery Service (Go)
- Databases & Caching: Amazon Aurora PostgreSQL, Amazon DynamoDB, Redis ElastiCache
- Infrastructure: Amazon EventBridge, AWS SQS, AWS Distro for OpenTelemetry (ADOT)

## Relationships
- Customer SPA / Admin SPA -> AWS API Gateway: Inbound client traffic [HTTPS/WSS]
- AWS API Gateway -> Catalog, Order, Recommendation, & Digital Asset Services: Internal routing [gRPC over TLS / HTTPS]
- Internal Services -> Amazon Aurora PostgreSQL & DynamoDB: Data persistence [TLS]
- Services -> Amazon EventBridge & SQS: Asynchronous event publishing and queuing [AMQP/HTTPS]

## Technology Stack
- AWS: Cloud provider across us-east-1, eu-west-1, ap-southeast-1 for global reach and high availability.
- React, Node.js, Spring Boot, Python FastAPI, Go: Polyglot microservices stack matched to workload performance needs.
- gRPC over TLS: Low-latency internal service-to-service communication.
- Amazon Aurora PostgreSQL & DynamoDB: Scalable relational and NoSQL storage with multi-currency support.
- Redis ElastiCache: In-memory caching for high-performance catalogue lookups.

## Rationale
- Microservices deployed across multiple AWS regions guarantee 99.95% availability and sub-2-second page loads on 3G networks.
- Edge security via AWS WAF and stateless JWT authorization fulfill OWASP Top-10 mitigation and GDPR/CCPA compliance requirements.