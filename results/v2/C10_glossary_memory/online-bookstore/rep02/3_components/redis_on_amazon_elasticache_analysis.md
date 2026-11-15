## Overview
The Online Bookstore is a scalable cloud-native e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations. It utilizes Redis on Amazon ElastiCache as an in-memory caching and session store to ensure high-performance browsing and protect checkout availability.

## Key Elements
- Redis on Amazon ElastiCache (Redis, Amazon ElastiCache)
- Catalog Cache Store (In-Memory Key-Value Store)
- Session & Cart Store (In-Memory Hash/String Store)
- Catalog & Search Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Order & Checkout Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- AWS Secrets Manager (AWS Secrets Manager, AWS KMS)

## Relationships
- Catalog & Search Service -> Catalog Cache Store (RESP over TLS)
- Order & Checkout Service -> Session & Cart Store (RESP over TLS)
- Redis on Amazon ElastiCache -> AWS Secrets Manager (AWS SDK for AUTH token management)

## Technology Stack
- Redis on Amazon ElastiCache (Serverless/Multi-AZ): Delivers sub-millisecond latency for high-frequency catalog searches and active shopping carts.
- Redis ACLs & RBAC: Enforces least-privilege key-space access between microservices.
- AWS KMS & AWS Secrets Manager: Secures data at rest and manages dynamic Redis AUTH tokens.
- TLS 1.3: Secures all in-transit RESP protocol traffic between ECS tasks and ElastiCache.

## Rationale
This architecture meets 99.95% uptime and scalability requirements by isolating high-volume catalog reads from transactional cart mutations using dedicated Redis key-spaces. Security controls, including private VPC placement and automated TTL policies, ensure strict GDPR/CCPA compliance and robust protection against OWASP Top-10 vulnerabilities.