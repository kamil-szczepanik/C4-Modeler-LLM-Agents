## Overview
The Online Bookstore API Gateway container routes, secures, and optimizes client traffic for a globally distributed e-commerce platform. It provides high-performance routing, localized multi-currency context propagation, and stringent security controls to ensure high availability and compliance.

## Key Elements
- Routing & Edge Component (Amazon API Gateway, Amazon CloudFront, AWS WAF)
- Authentication & Authorization Filter (AWS Lambda Authorizer)
- Service Mesh Proxy (AWS App Mesh / Envoy sidecar)
- Client Context & Localization Component (Integrated within API Gateway)
- External Systems (Identity Provider, Single Page Application, Backend Microservices)

## Relationships
- Single Page Application -> Routing & Edge Component: Routes client traffic [HTTPS (TLS 1.3)]
- Routing & Edge Component -> Authentication & Authorization Filter: Validates tokens [HTTPS/JSON]
- Routing & Edge Component -> Service Mesh Proxy: Forwards internal requests [HTTP/2 or gRPC]
- Service Mesh Proxy -> Backend Microservices (Catalogue, Order, Recommendation, Review): Enforces east-west traffic [mTLS via gRPC]
- Authentication & Authorization Filter -> Identity Provider: Authenticates users [OAuth 2.0 / OIDC over HTTPS]

## Technology Stack
- Amazon API Gateway: Manages edge routing, rate limiting, and request validation for scalability.
- AWS App Mesh / Envoy: Manages service-to-service communication and mTLS to guarantee uptime.
- AWS Lambda: Executes token authorization and header enrichment without latency.
- Amazon CloudFront & AWS WAF: Provides global content delivery and OWASP Top-10 mitigations.

## Rationale
This architecture uses managed AWS edge and service mesh technologies to handle 1M MAU and maintain a 99.95% uptime SLA. It centralizes security, PII masking, and multi-currency context handling at the gateway to satisfy strict GDPR/CCPA compliance and performance constraints.