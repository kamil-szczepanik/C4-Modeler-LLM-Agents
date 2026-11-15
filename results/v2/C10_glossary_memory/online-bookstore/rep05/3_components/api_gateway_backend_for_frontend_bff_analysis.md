## Overview
[The Online Bookstore System is a scalable AWS-hosted e-commerce platform that provides global customers with catalogue browsing, secure checkout, reviews, and personalized recommendations.]

## Key Elements
• API Router & Rate Limiter Component (AWS API Gateway)
• GraphQL / REST Resolver Component (NestJS on AWS ECS Fargate)
• Session & Auth Middleware Component (NestJS)
• Telemetry & Logging Interceptor Component (NestJS)
• Regional Distributed Caching (AWS ElastiCache / Redis)

## Relationships
• Single-Page Application (SPA) -> API Gateway / Backend-for-Frontend (BFF) via HTTPS/REST and GraphQL
• API Router & Rate Limiter Component -> Session & Auth Middleware Component via Internal HTTP
• Session & Auth Middleware Component -> GraphQL / REST Resolver Component via In-process calls
• GraphQL / REST Resolver Component -> Catalog, Order, Recommendation Services via gRPC over mTLS
• API Gateway / Backend-for-Frontend (BFF) -> Identity Provider via OAuth2/OIDC with short-lived JWTs
• API Gateway / Backend-for-Frontend (BFF) -> Analytics & Monitoring Platform via HTTPS

## Technology Stack
• AWS API Gateway: Provides edge routing, WAF evaluation, and token bucket rate limiting for security.
• NestJS on AWS ECS Fargate: Powers the backend-for-frontend containers with horizontal autoscaling.
• AWS ElastiCache (Redis): Implements regional distributed caching for currency rates and catalogue metadata to reduce latency.
• OpenTelemetry: Standardizes distributed tracing across BFF and backend gRPC services.

## Rationale
[This architecture decouples heavy backend operations from the client while aggregating payloads to achieve sub-2s page loads on 3G networks. Multi-region ECS Fargate deployment and robust edge caching ensure 99.95% availability for 1 million monthly active users.]