## Overview
The Online Bookstore is a scaled-down e-commerce system for purchasing physical and electronic books with integrated recommendations and reviews. It utilizes a cloud-native microservices architecture hosted on AWS to support global scalability and compliance requirements.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: Payment Gateway, Third-Party Shipping Provider API, Notification Service, Identity Provider / OAuth 2.0 Service, Currency Exchange Rate Service
- **Containers**: Single Page Application (SPA), API Gateway, Catalog Service, Order & Checkout Service, Recommendation Service, Customer Review Service, Message Broker
- **API Gateway Components**: SSL Terminator & WAF, Authentication & Authorization Filter, Rate Limiter & Throttler, Request Router

## Relationships
- Single Page Application (SPA) -> API Gateway: Sends client requests [HTTPS / JSON]
- Authentication & Authorization Filter -> Identity Provider / OAuth 2.0 Service: Validates JWT signatures and scopes [HTTPS / REST]
- Rate Limiter & Throttler -> Amazon ElastiCache (Redis): Maintains token buckets and counters [RESP / TCP]
- Request Router -> Catalog Service, Order & Checkout Service, Recommendation Service, Customer Review Service: Forwards traffic [HTTP/2 / gRPC]

## Technology Stack
- Cloud Provider: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region redundancy and 99.95% uptime
- Frontend: React, TypeScript, Amazon S3, Amazon CloudFront for performance (page load < 2s on 3G)
- API Gateway & Security: Amazon API Gateway with AWS WAF for OWASP Top-10 mitigations and SSL termination
- Caching & Rate Limiting: Amazon ElastiCache (Redis) for distributed rate-limiting counters
- Backend Services: Go, Node.js, and Python (FastAPI) selected for domain-specific performance and scalability
- Datastores: Amazon Aurora, Amazon OpenSearch, and Amazon DocumentDB for data persistence and search

## Rationale
This decoupled microservices architecture scales horizontally to support 1 million Monthly Active Users without performance degradation. Leveraging managed AWS services minimizes operational overhead while ensuring high availability, global reach, and compliance with GDPR and CCPA.