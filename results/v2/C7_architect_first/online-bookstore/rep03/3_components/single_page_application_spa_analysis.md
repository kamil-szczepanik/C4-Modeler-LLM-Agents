## Overview
The Online Bookstore SPA is a React-based e-commerce storefront delivering high-performance catalog browsing, secure checkout, and personalized recommendations for 1M MAU. It prioritizes sub-2-second 3G page loads, multi-currency support, and strict GDPR/CCPA and OWASP compliance.

## Key Elements
- Routing & View Manager (React Router)
- Catalog & Search Module
- Cart & Checkout Module
- Auth & Session Context
- State Management Layer (Zustand / React Context)
- Analytics & Tracking Wrapper
- Amazon S3 & Amazon CloudFront (CDN) with Lambda@Edge
- Amazon API Gateway

## Relationships
- Routing & View Manager -> Catalog & Search Module & Cart & Checkout Module [In-memory routing]
- Cart & Checkout Module -> State Management Layer [In-memory state sync]
- All Modules -> Analytics & Tracking Wrapper [Async event dispatch]
- All Modules -> Amazon API Gateway [HTTPS/JSON via Axios]
- Customer -> Amazon CloudFront [HTTPS]

## Technology Stack
- React: Component-based UI rendering
- React Router: Client-side routing and lazy-loading for performance
- Zustand / React Context: Lightweight state management for optimistic UI updates
- Amazon S3 & Amazon CloudFront: Global static asset hosting and CDN delivery
- Lambda@Edge: Geo-based currency routing and security headers
- Zod: Client-side input validation and sanitization

## Rationale
This architecture leverages a decoupled SPA hosted on a global CDN to achieve sub-2-second load times on 3G and 99.95% uptime. In-memory token handling, strict CSP headers, and edge security controls ensure robust GDPR/CCPA and OWASP Top-10 compliance.