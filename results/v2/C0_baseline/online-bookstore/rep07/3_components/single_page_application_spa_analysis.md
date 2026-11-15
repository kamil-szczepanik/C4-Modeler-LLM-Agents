## Overview
The Single Page Application (SPA) container serves as the primary browser-based user interface for the Online Bookstore, delivering a global, sub-2-second catalog browsing and secure checkout experience. It leverages a modern frontend stack deployed via AWS to support 1 million monthly active users with high performance and security.

## Key Elements
- Single Page Application (SPA) container
- Routing & Shell Component (React Router, Zustand)
- Catalog & Search Component
- Checkout & Cart Component
- Recommendation & Reviews Component
- Admin & Analytics Dashboard Component
- API Client Layer (Axios/Fetch with OpenAPI SDK)

## Relationships
- Shopper / Registered Customer / Admin -> Single Page Application (SPA): Interacts with UI [HTTPS / JSON]
- Single Page Application (SPA) -> API Gateway: Sends client requests and API calls [HTTPS / JSON]
- Routing & Shell Component -> Functional Components: Renders views [In-memory]
- Functional Components -> API Client Layer: Executes remote operations [HTTPS / JSON]

## Technology Stack
- React & TypeScript: Core frontend framework for type-safe component development
- Amazon CloudFront & S3: Global static asset delivery for sub-2-second page loads (R-06)
- Zustand: Decoupled global state management, including local cart persistence for resilience
- AWS Lambda@Edge: Enforces Content Security Policy (CSP), HSTS, and CORS for OWASP Top-10 mitigation (R-08)

## Rationale
This component-level architecture ensures lightning-fast global performance and high availability while strictly separating untrusted client-side execution from secure backend services. The modular design protects conversion rates through resilient cart handling and robust client-side security controls.