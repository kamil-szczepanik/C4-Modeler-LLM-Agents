## Overview
An AWS-hosted, global Single Page Application serves as the high-performance customer interface for the Online Bookstore. It is optimized for rapid catalog browsing and secure e-commerce transactions across multiple international regions.

## Key Elements
- **Actors**: Customer (primary retail user)
- **Frontend Container**: Single Page Application (SPA) (React, TypeScript, AWS S3, AWS CloudFront)
- **SPA Components**: Routing & View Manager (React Router), State Management Store (Redux Toolkit/Zustand), API Client (Axios/Fetch with Performance Monitoring Interceptor), UI Component Library (Tailwind CSS/Shadcn UI)
- **External Systems**: API Gateway (AWS API Gateway with WAF), Catalog Service, Order Management & Payment Integration, Recommendation Service

## Relationships
- Customer -> Single Page Application (SPA): Accesses retail storefront [HTTPS]
- Single Page Application (SPA) -> API Gateway: Sends REST API requests [HTTPS / REST / JSON]
- Routing & View Manager -> UI Component Library: Dynamically loads views via lazy loading
- API Client -> API Gateway: Transmits telemetry and fetches catalog/checkout data [HTTPS]

## Technology Stack
- **Frontend Framework**: React with TypeScript for type-safe, maintainable component development.
- **Global Hosting & CDN**: AWS S3 and AWS CloudFront with geo-proximity routing across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to ensure sub-2-second page loads.
- **Security**: AWS WAF and HSTS/CSP response headers to mitigate OWASP Top-10 risks and protect authentication tokens.
- **State & Routing**: React Router and Redux Toolkit/Zustand for responsive navigation and resilient client-side state handling.

## Rationale
Restricting the SPA to the customer persona prevents bundle bloat and ensures high availability (99.95%) and performance for 1M MAU. Edge distribution via AWS CloudFront and robust client-side security measures directly satisfy global scalability, speed, and GDPR/CCPA-aligned data protection constraints.