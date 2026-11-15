## Overview
- An Amazon-style e-commerce Single Page Application (SPA) providing browsing, search, reviews, recommendations, and checkout for physical and electronic books.
- Built using React and delivered globally via AWS S3 and CloudFront to support 1 million monthly active users (MAU) with sub-2-second 3G load times.

## Key Elements
- Book Buyer, Site Administrator, Customer Support Representative (Users)
- Single Page Application (SPA) (React, AWS S3, CloudFront)
- Catalog & Search Module, Checkout & Cart Module, Localization Context Provider, Compliance & Consent Banner, Analytics & Event Ingestion Client (React Components)
- API Gateway (Node.js)
- Localization Container, Analytics & Event Ingestion Container

## Relationships
- Users -> Single Page Application (SPA): Access application features [HTTPS via AWS CloudFront and Route 53]
- SPA (Catalog Module) -> API Gateway: Fetches book data [HTTPS / REST]
- Localization Context Provider -> Localization Container: Fetches currency rates and dictionaries [HTTPS / REST]
- Analytics Client -> Analytics & Event Ingestion Container: Dispatches telemetry and funnel events asynchronously [HTTPS / REST]

## Technology Stack
- React: Powers the component-based UI for high performance and modularity.
- AWS S3 & CloudFront: Ensures global content delivery and sub-2-second 3G load times.
- HttpOnly, Secure, SameSite=Strict Cookies: Manages secure token handling to prevent XSS.
- Content Security Policy (CSP): Mitigates OWASP Top-10 injection and XSS vectors.

## Rationale
- The React SPA architecture directly fulfills high-performance constraints and multi-currency needs across global regions.
- Edge delivery via CloudFront combined with strict security policies ensures GDPR/CCPA compliance and 99.95% availability.