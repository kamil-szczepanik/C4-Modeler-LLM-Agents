## Overview
The Online Bookstore Storefront provides a high-performance, secure e-commerce user interface for global customers and administrators. It delivers scalable multi-currency browsing, cart management, and secure checkout while ensuring compliance with GDPR, CCPA, and OWASP standards.

## Key Elements
- **Users**: Registered Customer, Guest Shopper, Store Administrator
- **External Systems**: External Identity Provider, External Payment Gateway, External Shipping Provider, External Notification Service
- **Containers**: Storefront SPA, API Gateway, Catalog & Search Service, Order & Checkout Service, Recommendation Service, Customer Privacy Service, Pricing & Currency Service
- **Storefront Components**: Catalog UI Module, Checkout & Cart Module, Authentication & Session Manager, Promotional Banner & Campaign Module, Abandoned Cart Recovery Trigger, Localization & Currency Module, Review & Rating UI Module

## Relationships
- Customer / Store Administrator -> Storefront: Accesses SPA via HTTPS/TLS 1.3 [HTTPS]
- Storefront -> API Gateway: Communicates UI actions and data requests via HTTPS/REST [HTTPS/REST]
- Authentication & Session Manager -> External Identity Provider: Authenticates users via OAuth 2.0 with PKCE [HTTPS]
- Localization & Currency Module -> Pricing & Currency Service: Fetches multi-currency rates via API Gateway [HTTPS/REST]

## Technology Stack
- **Frontend Framework**: React 18 with TypeScript and Tailwind CSS for robust, type-safe UI development
- **State Management**: Redux/Context for centralized client-side state and multi-currency cart handling
- **Delivery & CDN**: Amazon S3 and Amazon CloudFront CDN with AWS WAF for global static asset distribution and edge security
- **Security & Monitoring**: OAuth 2.0/PKCE, CSP headers, Subresource Integrity (SRI), and CloudWatch RUM/Synthetics for performance tracking

## Rationale
This architecture uses a React SPA delivered via CloudFront to achieve sub-2-second page loads on 3G connections for 1M MAU. Edge security, strict token isolation, and modular lazy-loading protect the system against OWASP Top-10 threats while preserving global performance and uptime SLAs.