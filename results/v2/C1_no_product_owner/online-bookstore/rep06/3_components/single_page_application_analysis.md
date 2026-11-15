## Overview
An online bookstore Single Page Application (SPA) providing catalogue browsing, secure checkout, reviews, and recommendations. Built for global scale across three AWS regions supporting 1M MAU.

## Key Elements
- Single Page Application: React / TypeScript frontend container hosted on AWS S3 and distributed via CloudFront
- Router / Shell: Component managing client-side routing, layout, and lazy loading
- Catalogue & Search View: Components for browsing, filtering, and keyword search
- Cart & Checkout Flow: Components managing shopping cart state and secure checkout
- Reviews & Ratings Widget: Components for displaying and submitting customer reviews
- Recommendation Widget: Components displaying 'Customers also bought' items
- API Client: Centralized HTTP/REST communication layer injecting correlation IDs and managing in-memory tokens

## Relationships
- Customer -> Single Page Application: Browses catalogue and interacts with UI [HTTPS / TLS 1.3]
- Single Page Application -> API Gateway / ALB: Sends API requests via API Client [HTTPS / TLS 1.3]
- Single Page Application -> AWS S3 / CloudFront: Serves static assets globally [HTTPS / TLS 1.3]

## Technology Stack
- React / TypeScript: Core framework for component-based UI development and type safety
- AWS S3 & CloudFront: Static asset hosting and global CDN with Edge functions for low-latency delivery (<2s 3G requirement)
- In-Memory State & HttpOnly Cookies: Secure token management avoiding localStorage to mitigate XSS risks

## Rationale
Client-side rendering with S3 and CloudFront guarantees sub-second global performance and high availability under 1M MAU. In-memory token storage and strict CSP headers enforce OWASP Top-10 security without introducing an extra BFF container.