## Overview
- An AWS-hosted online bookstore built for 1M MAU, delivering catalog browsing, secure checkout, reviews, and personalized recommendations.
- Implemented as a microservices-based container architecture across multiple global regions to ensure high availability, security, and low latency.

## Key Elements
- Customers [person]
- Authors/Publishers [person]
- Store Administrators [person]
- Web App Frontend [container, React, Next.js, TypeScript]
- API Gateway [container, Amazon API Gateway]
- Catalog & Search Service [container, Java, Spring Boot, Amazon OpenSearch]
- Checkout & Order Service [container, Go, gRPC/REST]
- Recommendation Service [container, Python, FastAPI]
- Admin Management Service [container, Java, Spring Boot]
- Database Storage [container/storage, Amazon Aurora PostgreSQL Global Database]
- Caching Layer [container/storage, Amazon ElastiCache (Redis)]
- Payment Gateway [externalSystem]
- Third-Party Shipping APIs [externalSystem]
- Identity Provider [externalSystem, AWS Cognito/Auth0]
- AWS CloudFront CDN/WAF [externalSystem]
- Route 53 [externalSystem]
- AWS Secrets Manager [externalSystem]
- AWS KMS [externalSystem]

## Relationships
- Customers -> Web App Frontend (HTTPS / TLS 1.3 / OAuth 2.0 / OIDC)
- Web App Frontend -> API Gateway (HTTPS / REST / gRPC)
- API Gateway -> Catalog & Search Service (HTTPS / gRPC)
- API Gateway -> Checkout & Order Service (HTTPS / gRPC)
- API Gateway -> Recommendation Service (HTTPS / gRPC)
- API Gateway -> Admin Management Service (HTTPS / gRPC)
- Checkout & Order Service -> Payment Gateway (HTTPS / REST APIs)
- Checkout & Order Service -> Third-Party Shipping APIs (HTTPS / REST APIs)
- API Gateway -> Identity Provider (OIDC / OAuth 2.0 / HTTPS)
- Recommendation Service -> Caching Layer (Redis Protocol)
- Services -> Database Storage (PostgreSQL Protocol over TLS)

## Technology Stack
- Frontend: React, Next.js, TypeScript with AWS CloudFront for SSR/SSG delivery (<2s page load).
- Backend Services: Java Spring Boot (Catalog, Admin), Go (Checkout for ACID performance), Python FastAPI (Recommendations).
- Infrastructure & Compute: AWS ECS on Fargate across us-east-1, eu-west-1, and ap-southeast-1 for container orchestration and 99.95% uptime.
- Data & Caching: Amazon Aurora PostgreSQL Global Database for multi-region transactional persistence; Amazon OpenSearch for search; Amazon ElastiCache (Redis) for sub-100ms recommendations.
- Security & Routing: Amazon API Gateway, AWS App Mesh for mTLS, AWS KMS (AES-256) for encryption, AWS Secrets Manager, and Route 53 for global traffic routing.

## Rationale
- Decouples user-facing and administrative containers to protect system reliability and prevent resource starvation during peak sales events.
- Utilizes global databases, multi-region container orchestration, and caching to satisfy strict scalability, low-latency, and GDPR/CCPA compliance requirements.