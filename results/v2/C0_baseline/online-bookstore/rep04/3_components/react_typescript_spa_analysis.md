## Overview
The Online Bookstore SPA is a high-performance React/TypeScript application delivered globally via AWS S3 and CloudFront to serve 1M MAU. It provides a secure, multi-currency e-commerce shopping experience with sub-2-second load times on 3G networks.

## Key Elements
- Routing & Layout Component (React Router)
- Catalog & Search Feature Module (React, Zustand)
- Cart & Checkout Feature Module (React, React Hook Form)
- Social Proof & Recommendations Module (React Query)
- Admin Management Module (React, Lazy-Loaded)
- API Client Wrapper (Axios)
- AWS CloudFront & AWS S3
- AWS API Gateway

## Relationships
- Book Buyer, Registered Reviewer, Store Administrator -> React / TypeScript SPA via HTTPS
- React / TypeScript SPA -> AWS API Gateway via HTTPS / JSON
- React / TypeScript SPA -> AWS S3 / CloudFront via HTTPS
- Internal Modules -> API Client Wrapper via TypeScript / Function Calls

## Technology Stack
- React & TypeScript: Type-safe component architecture and core UI framework.
- AWS S3 & CloudFront: Global static asset hosting and CDN for low-latency delivery.
- Zustand: Global client-side state management for cart and currency preferences.
- React Query: Server-state caching, synchronization, and optimistic UI updates.
- Axios: HTTP client with interceptors for secure API communication.

## Rationale
Modular code-splitting and edge caching ensure sub-2-second performance on 3G networks while supporting 1M MAU. Strict token handling and CSP headers mitigate OWASP Top-10 risks and ensure GDPR and CCPA compliance.