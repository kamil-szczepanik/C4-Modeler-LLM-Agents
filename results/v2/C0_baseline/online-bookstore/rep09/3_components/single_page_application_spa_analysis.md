## Overview
The Online Bookstore SPA is a React/TypeScript frontend delivered via AWS S3 and CloudFront. It provides high-performance browsing, secure checkout, multi-currency support, and GDPR compliance for 1 million monthly active users.

## Key Elements
- React Router (Router & View Controller)
- Zustand + i18next (State & Localization Store)
- Axios/Fetch with Interceptors (API Client Layer)
- Consent & Compliance Manager
- Auth & Session Interceptor
- AWS S3 & CloudFront (Hosting & CDN)
- AWS WAF (Edge Security)

## Relationships
- Book Buyer / Store Administrator -> CloudFront/S3: Accesses SPA interface [HTTPS / TLS 1.3]
- SPA -> AWS API Gateway: Sends REST API requests for catalogue, orders, and recommendations [HTTPS / JSON]
- CloudFront -> AWS WAF: Inspects and filters edge traffic for OWASP Top-10 mitigation [HTTPS]

## Technology Stack
- React & TypeScript: Delivers scalable, component-based UI for high maintainability
- AWS CloudFront & S3: Ensures global CDN caching for sub-2-second page loads on 3G (R-06)
- Zustand & i18next: Manages lightweight client state, themes, and multi-currency (USD, EUR, GBP) preferences
- HttpOnly Cookies: Secures session management against XSS exfiltration
- AWS WAF: Provides edge-level DDoS protection and OWASP Top-10 filtering (R-08)

## Rationale
This architecture decouples the frontend to guarantee high scalability and performance under heavy load. Utilizing secure cookies, strict CSP headers, and edge caching satisfies both strict GDPR/CCPA privacy constraints and high availability targets (99.95%).