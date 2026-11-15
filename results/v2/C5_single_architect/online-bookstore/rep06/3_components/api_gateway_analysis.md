## Overview
The Online Bookstore API Gateway manages client traffic routing, security, and telemetry for the e-commerce platform. It provides high-performance ingress, authentication, and traffic management to meet global scalability and security requirements.

## Key Elements
- Customers and Admin/Support Staff
- Amazon API Gateway (HTTP APIs v2)
- Internal Components: Routing & Dispatcher, JWT Auth Filter, Rate Limiting & Throttling, Request/Response Transformation, API Analytics & Logging
- Downstream Containers: Catalog Service, Order & Checkout Service, Recommendation Service, Customer & Review Service
- External Systems: Amazon CloudWatch, Identity Provider / SSO Service

## Relationships
- Customer/Admin -> Amazon API Gateway: Sends API requests [HTTPS / JSON (JWT authenticated)]
- Amazon API Gateway -> Catalog Service / Order Service / Recommendation Service / Customer Service: Routes proxied requests [gRPC / HTTPS via AWS VPC Links]
- Amazon API Gateway -> Identity Provider: Validates user tokens [HTTPS / OIDC]
- Amazon API Gateway -> Amazon CloudWatch: Publishes access logs and metrics [AWS SDK / HTTPS]

## Technology Stack
- Amazon API Gateway HTTP APIs (v2): Selected for lower latency (<2s page load goal) and cost-efficiency.
- AWS Lambda Authorizers: Used for custom security validation logic and JWT verification at the edge.
- AWS VPC Links: Provides secure, low-latency connectivity to backend microservices.
- Amazon CloudWatch: Captures real-time request metrics, latency percentiles, and access logs for monitoring and audits.

## Rationale
This component architecture optimizes edge performance and security by offloading JWT validation, rate limiting, and request sanitization from backend microservices. Utilizing API Gateway HTTP APIs and VPC Links ensures minimal latency to support high-throughput, globally distributed users while meeting availability and audit constraints.