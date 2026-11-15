## Overview
The Single-Page Application (SPA) serves as the primary frontend interface for the Online Bookstore, enabling users to browse, purchase, and review books. It is built to deliver high-performance, secure e-commerce experiences while supporting 1 million monthly active users globally.

## Key Elements
* Router & State Management Module (Redux Toolkit / Zustand)
* Catalog & Search View
* Checkout & Cart Workflow (supporting guest and authenticated flows)
* Review & Rating Component (DOMPurify for sanitization)
* API Client (Axios / GraphQL client with interceptors)

## Relationships
* Book Buyer & Reviewer -> Single-Page Application (SPA): Browses catalog, manages cart, and submits reviews [HTTPS]
* Single-Page Application (SPA) -> Amazon API Gateway: Communicates API requests and authentication flows [HTTPS (REST/GraphQL)]

## Technology Stack
* React / TypeScript: Chosen for component reusability and fast UI rendering.
* AWS S3 & CloudFront: Selected for static asset hosting and low-latency global edge caching.
* DOMPurify: Utilized for client-side input sanitization against XSS.

## Rationale
This architecture ensures sub-2-second page loads on 3G networks and meets strict OWASP Top-10 security standards. Decoupling the frontend presentation layer from backend pricing and calculations safeguards multi-currency transactions and prevents client-side tampering.