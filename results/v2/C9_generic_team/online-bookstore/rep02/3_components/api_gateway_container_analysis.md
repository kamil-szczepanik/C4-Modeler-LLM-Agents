## Overview
The Online Bookstore is a scaled-down e-commerce platform built on AWS to support physical and electronic book sales, recommendations, and reviews. Its core purpose is to provide a highly available, scalable retail experience meeting GDPR/CCPA standards globally.

## Key Elements
- **Customers**: End-users browsing, reviewing, and purchasing books.
- **Frontend Container**: SPA/SSR application backed by a CDN.
- **API Gateway Container**: AWS API Gateway / Reverse Proxy handling perimeter security, routing, and rate limiting.
- **Core Domain Containers**: Microservices handling business logic via REST and gRPC.
- **Caching/Session Container**: Redis cluster for session data, rate limiting, and idempotency tracking.
- **External Systems**: Third-party Payment Gateway, Shipping Providers, Tax Calculation, and Notification Services.

## Relationships
- **Frontend Container -> API Gateway Container**: Client requests and routing via HTTPS / REST.
- **API Gateway Container -> Core Domain Containers**: Internal routing and service communication via Internal REST / gRPC.
- **API Gateway Container -> Caching/Session Container**: Distributed rate limiting and idempotency validation via Redis protocol.
- **Core Domain Containers -> External Systems**: Secure integrations for payment processing and shipping via HTTPS / REST.

## Technology Stack
- **Cloud Provider**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global reach.
- **API Management**: AWS API Gateway for TLS termination, rate limiting, and JWT validation.
- **Caching & State**: Redis for distributed caching, session storage, and idempotency keys.
- **Infrastructure as Code**: Terraform for declarative multi-region configuration management.
- **Protocols**: HTTPS, REST, and gRPC for client-server and inter-service communication.

## Rationale
This architecture ensures 99.95% uptime and scales to support 1M MAU by offloading cross-cutting concerns to a centralized API Gateway. Multi-region AWS deployment combined with Redis caching guarantees low-latency performance (< 2 s on 3G) while adhering to strict security and compliance requirements.