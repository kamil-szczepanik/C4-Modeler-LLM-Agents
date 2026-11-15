## Overview
[The Online Bookstore is a globally scaled e-commerce platform built for 1M MAU, delivering catalog browsing, secure checkout, reviews, and personalized recommendations across three AWS regions.]

## Key Elements
- Web App Frontend (React, Next.js, TypeScript)
- SSR Page Router / Rendering Component (Next.js App Router, TypeScript)
- Catalog & Search UI Component (React, TypeScript)
- Shopping Cart & Checkout UI Component (React, TypeScript)
- Reviews & Recommendations Component (React, TypeScript)
- Localization & Currency Preference Component (React, TypeScript)
- API Client / BFF Proxy Component (Next.js API Routes / TypeScript)
- API Gateway (Amazon API Gateway)
- AWS CloudFront CDN/WAF

## Relationships
- Customers -> Web App Frontend: Interacts with the web application [HTTPS / TLS 1.3 / OAuth 2.0 / OIDC]
- Web App Frontend -> API Gateway: Sends API requests to backend services [HTTPS / REST / gRPC]
- SSR Page Router -> Identity Provider: Handles user authentication flow [OIDC / OAuth 2.0 / HTTPS]
- SSR Page Router -> API Client / BFF Proxy Component: Internal function calls [Internal function call / HTTP]
- API Client / BFF Proxy Component -> API Gateway: Proxies backend requests [HTTPS / REST]

## Technology Stack
- React / Next.js / TypeScript: Powers frontend server-side rendering and UI components to meet sub-2s performance goals on 3G.
- AWS ECS Fargate / AWS CloudFront CDN/WAF: Provides scalable container hosting and edge caching across multi-region deployments.
- AWS Secrets Manager: Manages dynamic credentials and environment variables securely during CI/CD.

## Rationale
[This architecture utilizes Next.js SSR and AWS edge distribution to satisfy strict global performance and 99.95% availability targets for 1M MAU. Centralizing traffic through a BFF proxy and CloudFront WAF ensures robust OWASP security and GDPR/CCPA compliance.]