## Overview
- Single Page Application (SPA) serving as the primary frontend interface for shoppers, vendors, and admins of the Online Bookstore.
- Built to deliver instant responsiveness, secure authentication, and offline resilience for 1M MAU globally.

## Key Elements
- **Routing & Shell Component**: React Router for client-side navigation and lazy-loading feature modules.
- **State Management Store**: Centralized reactive state for cart items and user session footprint via Zustand/React Context.
- **API Client Layer**: Encapsulates backend communication, error boundaries, and request interceptors.
- **Persistence & Sync Middleware**: Manages local caching and synchronizes offline cart/wishlist state via IndexedDB.
- **Telemetry & Analytics Wrapper**: Asynchronously captures user interaction events and metrics.
- **Feature Modules**: Decoupled domain views (Catalogue Browser, Cart & Checkout, Product Reviews, Vendor Portal).

## Relationships
- Shoppers & Vendors -> Single Page Application: Browses catalogue, manages cart, and accesses portals [HTTPS via AWS CloudFront]
- Single Page Application -> API Gateway & WAF: Sends API requests for data and transactions [HTTPS / REST]
- State Management Store <-> Persistence & Sync Middleware: Synchronizes in-memory state with IndexedDB [Local Browser APIs]

## Technology Stack
- **React & React Router**: Core SPA framework chosen for component-based modularity and fast client-side rendering.
- **AWS S3 & CloudFront**: Static asset hosting and global content delivery network for <2s 3G page load performance.
- **IndexedDB**: Local browser storage for offline cart persistence during network drops.
- **HttpOnly Cookies**: Secure session management to prevent XSS credential theft.

## Rationale
- Optimizes initial bundle size and edge caching via CloudFront to meet strict 3G performance and 99.95% availability targets.
- Implements robust client-side security controls and IndexedDB offline persistence to ensure a reliable user experience across global regions.