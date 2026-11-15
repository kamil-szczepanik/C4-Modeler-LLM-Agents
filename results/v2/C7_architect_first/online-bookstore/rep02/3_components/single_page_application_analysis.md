## Overview
- Single Page Application (SPA) container for the Online Bookstore e-commerce platform.
- Delivers a high-performance, secure, and accessible user interface for global customers and administrators.

## Key Elements
- Router Component (`React Router v6`)
- State Management Store (`Zustand`)
- API Client Layer (`Axios`)
- Feature Modules (Catalog Browser, Checkout Flow, Review Manager, Recommendation Widget)
- External Infrastructure (AWS S3, AWS CloudFront, AWS API Gateway)

## Relationships
- Router Component loads Feature Modules on-demand [In-Memory]
- Feature Modules and State Management Store read/write state [In-Memory]
- Feature Modules and State Management Store invoke API Client Layer [TypeScript / HTTPS]
- API Client Layer sends requests to AWS API Gateway [HTTPS]

## Technology Stack
- React.js: Frontend UI library chosen for component reusability and fast rendering.
- React Router v6: Handles client-side navigation with code-splitting for <2s page load times on 3G.
- Zustand: Lightweight state management ensuring tokens are kept strictly in-memory for security.
- Axios: HTTP client with interceptors for JWT injection and multi-currency headers.
- AWS S3 & CloudFront: Static asset storage and global edge distribution for high availability.

## Rationale
- This architecture guarantees sub-2-second page loads and 99.95% uptime globally across target AWS regions.
- Strict in-memory state handling and CSP headers ensure robust GDPR/CCPA compliance and OWASP Top-10 mitigations.