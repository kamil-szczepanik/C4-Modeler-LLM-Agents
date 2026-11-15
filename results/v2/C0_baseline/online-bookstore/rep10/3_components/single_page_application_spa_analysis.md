## Overview
The Online Bookstore SPA is a high-performance React application hosted globally on Amazon S3 and Amazon CloudFront. It delivers a fast, secure, multi-currency e-commerce experience to shoppers, authors, and administrators while supporting 1M MAU.

## Key Elements
* Single Page Application (SPA): React / TypeScript frontend container
* Router & Auth Guard Component: React Router for role-based route protection
* Catalog & Search Component: Redux Toolkit for browsing and keyword search (R-01)
* Cart & Checkout Component: Manages shopping cart state and secure checkout (R-02)
* Recommendation & Review Component: Displays 5-star ratings and recommendations (R-03, R-04)
* Admin & Publisher Dashboard Component: Lazy-loaded back-office interface chunk
* Localization & Currency Provider Component: React Context API and `formatjs` for multi-currency handling (USD, EUR, GBP)
* AWS CloudFront & Amazon S3: Global static asset delivery and hosting
* AWS API Gateway: Secure entry point for all backend microservices

## Relationships
* Shopper / Author / Administrator -> Single Page Application (SPA): Accesses interfaces via HTTPS/REST
* SPA Components -> AWS API Gateway: Fetches data and mutates state via HTTPS/REST
* CloudFront -> Lambda@Edge / CloudFront Functions: Handles edge geo-routing and localization injection

## Technology Stack
* React 18 / TypeScript: Type-safe component architecture for maintainability
* Redux Toolkit: Predictable state management for catalog and cart
* formatjs: Robust multi-currency and internationalization formatting
* Amazon CloudFront & S3: Global CDN and object storage ensuring sub-2-second page loads on 3G (R-06)
* GitHub Actions: Automated CI/CD pipeline with cache invalidation

## Rationale
Decomposing the SPA with lazy-loading ensures administrative code never burdens shopper payloads, directly satisfying performance targets. Edge localization and secure token handling via HttpOnly cookies fulfill strict scalability, multi-currency, and OWASP security constraints.