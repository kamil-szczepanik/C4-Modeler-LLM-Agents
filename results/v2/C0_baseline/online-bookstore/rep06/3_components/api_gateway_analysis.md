## Overview
The Online Bookstore API Gateway routes and secures all client interactions for catalogue browsing, secure checkout, and recommendations. It provides scalable, low-latency traffic management across three global AWS regions.

## Key Elements
- Edge Router & WAF Integration
- Authentication & Authorization Filter
- Rate Limiting & Throttling Engine
- Service-Discovery & Routing Proxy
- AWS API Gateway
- AWS WAF & CloudFront
- AWS ElastiCache (Redis)
- AWS ECS Fargate Microservices

## Relationships
- Frontend SPA -> Edge Router: Sends API requests for catalogue, checkout, and user actions [HTTPS, REST, GraphQL]
- Edge Router -> Auth Filter -> Throttling Engine -> Routing Proxy: Processes requests through an in-memory pipeline
- Routing Proxy -> ECS Fargate Microservices: Routes internal traffic [gRPC over HTTP/2, mTLS]
- Auth Filter & Throttling Engine -> AWS ElastiCache (Redis): Validates token blacklists and synchronizes distributed rate limits [TCP]

## Technology Stack
- AWS API Gateway: Manages unified routing, rate-limiting, and canary deployments
- AWS WAF & CloudFront: Enforces OWASP Top-10 mitigations, SSL termination, and schema validation
- AWS ElastiCache (Redis): Powers distributed rate limiting and JWT revocation lookups
- gRPC over HTTP/2 with mTLS: Ensures secure, low-latency internal service communication

## Rationale
This architecture decouples edge security, routing, and rate-limiting from backend microservices to handle 1 million MAU reliably. It guarantees high availability and meets strict security, privacy, and performance requirements.