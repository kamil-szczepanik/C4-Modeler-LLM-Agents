## Overview
The AWS API Gateway serves as the secure, high-performance managed entry point for the Online Bookstore, handling client routing, authentication, and traffic management. It bridges client-facing HTTP/REST/GraphQL traffic with backend microservices using gRPC over mTLS.

## Key Elements
- AWS API Gateway (Managed Service)
- AWS WAF
- JWT Authorizer Component
- Rate Limiter & Throttling Module
- API Router & Transform Engine
- Edge Observability & Tracing Agent (AWS X-Ray/OpenTelemetry)

## Relationships
- Single Page Application -> AWS API Gateway: Sends HTTPS/JSON REST and GraphQL requests [HTTPS/JSON REST/GraphQL]
- AWS API Gateway -> AWS WAF: Inspects incoming requests for OWASP Top-10 mitigations [In-line Shield]
- AWS API Gateway -> Catalog, Order & Checkout, Recommendation Services: Dispatches transformed payloads [gRPC over mTLS via AWS ECS Service Connect]

## Technology Stack
- AWS API Gateway: Managed entry point and API management for scale and regional routing.
- AWS WAF: Provides edge security and OWASP Top-10 mitigation.
- AWS ECS Service Connect: Secures internal service-to-service communication via mTLS.
- Amazon Route 53: Enables multi-region latency-based routing across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Rationale
This architecture ensures 99.95% availability, handles 1M MAU scalability, and meets rigorous GDPR/CCPA security standards. Edge offloading of authentication, throttling, and WAF inspection optimizes performance for page loads under 2 seconds.