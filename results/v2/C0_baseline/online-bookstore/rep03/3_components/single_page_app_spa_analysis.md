## Overview
The Single Page App (SPA) container delivers a high-performance, secure e-commerce frontend for the Online Bookstore. It enables global customers to browse catalogs, manage multi-currency carts, and complete secure checkouts.

## Key Elements
- **Customers (Shoppers) & Guest Shoppers**: End users browsing catalogs, managing carts, and purchasing books.
- **Catalog & Search Module**: React and Redux Toolkit component handling keyword searches and local caching.
- **Cart & Multi-Currency State Manager**: React Context/Zustand component managing local cart state and currency display (USD, EUR, GBP).
- **Checkout & Auth Client**: React Router and Auth0 SDK component handling authentication and checkout handoffs.
- **Recommendation & Review Widget**: React component rendering asynchronous product recommendations and 5-star ratings.
- **Promotions & Discount Client**: Zustand component managing coupon codes and promotional banners.
- **Consent & Privacy Module**: React component gating tracking initialization for GDPR and CCPA compliance.

## Relationships
- Customers (Shoppers) -> Single Page App (SPA): Browses store, manages cart, and views recommendations via [HTTPS]
- Single Page App (SPA) -> Amazon API Gateway: Client-to-backend communication via [HTTPS / REST]
- Checkout & Auth Client -> Auth0: User authentication via [OAuth 2.0 / OIDC]

## Technology Stack
- **React**: Frontend UI library for component-based rendering.
- **Redux Toolkit & Zustand**: State management for caching, carts, and promotions.
- **Amazon CloudFront & S3**: Global content delivery network and static asset storage for low-latency rendering.
- **Auth0 SDK**: Secure user authentication and session management.

## Rationale
This architecture ensures sub-2-second page loads on 3G networks globally across multi-region AWS deployments. Decoupled React components maximize maintainability, scalability for 1 million monthly active users, and strict GDPR/CCPA compliance.