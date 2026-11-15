## Overview
The Online Bookstore is a globally distributed, scalable e-commerce platform designed to facilitate physical and electronic book sales, personalized recommendations, and reviews. It ensures high availability, GDPR compliance, and sub-2-second page loads across multiple regions.

## Key Elements
- **Actors & External Systems**: Customer, Payment Gateway, Shipping Provider API, Identity Provider / OAuth, Notification Service, Tax Calculation Service
- **Containers**: Single Page Application (SPA), API Gateway, Catalog Service, Order & Checkout Service, Recommendation Service, Review Service, Background Worker, Cache (Redis)
- **API Gateway Components**: JWT Authorizer, Rate Limiter & WAF, HTTP Proxy Router, Request Transformation & Enrichment, Response Caching

## Relationships
- Single Page Application -> API Gateway: Makes API requests [HTTPS / WSS]
- JWT Authorizer -> HTTP Proxy Router: Forwards authenticated requests [Internal]
- HTTP Proxy Router -> Request Transformation: Enriches payloads [Internal]
- Request Transformation -> Response Caching: Checks and stores cache [Internal / Amazon ElastiCache]
- Response Caching -> Catalog & Recommendation Services: Fallback origin fetch [gRPC over AWS VPC Link]
- API Gateway -> Order & Checkout Service: Routes checkout requests [gRPC / HTTP]
- API Gateway -> Review Service: Routes review queries [gRPC / HTTP]

## Technology Stack
- **Cloud Infrastructure**: AWS across us-east-1, eu-west-1, ap-southeast-1 for global availability (R-07)
- **Frontend**: React and TypeScript served via AWS S3 and CloudFront for low-latency delivery (R-06)
- **API Gateway**: AWS API Gateway integrated with AWS WAF for OWASP Top-10 mitigations and rate limiting (R-08)
- **Backend Services**: Go (Catalog), Node.js (Order & Checkout), Python FastAPI (Recommendations), Java Spring Boot (Reviews) for polyglot performance
- **Databases & Caching**: PostgreSQL (RDS) for transactional data, MongoDB for reviews, Vector DB for recommendations, and Redis (Amazon ElastiCache) for edge caching (R-06)
- **Communication**: gRPC over AWS VPC Links for low-latency internal service-to-service calls

## Rationale
This architecture uses cloud-native managed services, regional distribution, and efficient edge caching to easily scale to 1 million MAU while maintaining sub-2-second performance. Decoupled microservices ensure strict compliance (GDPR/CCPA), robust security (OWASP Top-10 via AWS WAF), and 99.95% uptime.