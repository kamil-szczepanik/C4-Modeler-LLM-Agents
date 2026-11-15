## Overview
An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations. The frontend is a scalable Single Page Application deployed globally on AWS.

## Key Elements
- Single Page Application (SPA) (React, TypeScript)
- Routing & Shell Component (React Router)
- Catalog & Search Module
- Cart & Checkout State Machine (Redux Toolkit)
- Recommendation & Review Widgets
- API Client & Interceptor Module (Axios)
- Amazon S3 & Amazon CloudFront
- API Gateway / Load Balancer

## Relationships
- Customer, Reviewer, Store Administrator -> Single Page Application (SPA) [HTTPS / JSON]
- Single Page Application (SPA) -> API Gateway / Load Balancer [HTTPS / JSON]
- Amazon CloudFront -> Amazon S3 [Internal AWS Protocol]

## Technology Stack
- React & TypeScript: Type-safe, component-driven UI development
- Redux Toolkit: Predictable state management for complex cart workflows
- Axios: Centralized HTTP client with interceptors for auth and tracing
- Amazon S3 & CloudFront: Static hosting and global edge delivery for <2s performance
- DOMPurify: Client-side sanitization against XSS in user reviews

## Rationale
This architecture ensures high performance, global availability, and strict security compliance while handling 1 million monthly active users. Decoupling the SPA components guarantees maintainability and seamless scalability across regions.