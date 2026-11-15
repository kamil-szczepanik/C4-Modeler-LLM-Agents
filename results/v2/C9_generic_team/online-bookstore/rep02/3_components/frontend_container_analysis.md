## Overview
The Online Bookstore system is a scalable, globally distributed e-commerce platform designed for browsing, purchasing physical and electronic books, and managing user reviews and recommendations. It delivers a high-performance, secure, and multi-region user experience compliant with GDPR and CCPA.

## Key Elements
- Customers (Users)
- Frontend Container (SPA/SSR backed by CDN)
- API Gateway Container (AWS API Gateway / Reverse Proxy)
- Core Domain Containers (Microservices)
- Third-Party Services (Payment Gateway, Shipping, FX, Tax, Fraud, Distributors)

## Relationships
- Customers -> Frontend Container: Browsing, purchasing, and reviewing books [HTTPS over TLS]
- Frontend Container -> API Gateway Container: API requests and routing [HTTPS / REST]
- API Gateway Container -> Core Domain Containers: Internal service routing [gRPC / REST]

## Technology Stack
- Frontend: Single Page Application / Server-Side Rendering with TypeScript for end-to-end type safety
- Delivery & Security: Content Delivery Network (CDN) with strict Content Security Policy (CSP) and subresource integrity (SRI) for OWASP Top-10 mitigation
- Observability: Real-User Monitoring (RUM) and synthetic monitoring for Core Web Vitals tracking
- Cloud Infrastructure: AWS global regions (us-east-1, eu-west-1, ap-southeast-1)

## Rationale
This architecture ensures 99.95% availability and sub-2-second 3G page loads via aggressive CDN edge caching and resilient client-side error boundaries. It safely satisfies global compliance mandates and multi-currency support through stateless session management and regional dynamic configuration.