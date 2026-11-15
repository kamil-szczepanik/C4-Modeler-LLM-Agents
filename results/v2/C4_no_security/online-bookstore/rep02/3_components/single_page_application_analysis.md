## Overview
[The system is a scalable global e-commerce SPA built to provide lightning-fast book browsing, secure checkout, reviews, and personalized recommendations for 1M MAU. It ensures low latency, multi-currency support, and strict GDPR/CCPA compliance across three global AWS regions.]

## Key Elements
- Book Shopper, Book Author/Publisher, Store Administrator
- Single Page Application (React / TypeScript, hosted on AWS S3)
- Routing & Shell Component, Consent & Localization Provider, Catalog & Search Component, Checkout & Cart Component, Reviews & Recommendations Component, Admin & Author Dashboard Component, State & Telemetry Component
- AWS API Gateway (REST / GraphQL)
- AWS Cognito / Auth0
- AWS CloudFront and Route 53
- Datadog RUM / CloudWatch

## Relationships
- AWS CloudFront/Route 53 -> Single Page Application: Delivers static assets and frontend application [HTTPS]
- Single Page Application -> AWS API Gateway: Sends API requests for data and actions [HTTPS / REST / GraphQL]
- Single Page Application -> AWS Cognito/Auth0: Authenticates users and validates sessions [OAuth2/OIDC over HTTPS]
- Single Page Application -> Datadog / CloudWatch: Sends telemetry, logs, and RUM metrics [HTTPS]

## Technology Stack
- React / TypeScript: Chosen for component reusability, rich ecosystem, and rapid UI development.
- AWS S3 & CloudFront: Selected for global edge delivery, caching, and meeting sub-2-second 3G load-time NFRs.
- Zustand & React Query: Utilized for efficient global state management and server-state caching.
- Datadog RUM SDK: Integrated for tracking Core Web Vitals and performance across regions.

## Rationale
[The React SPA hosted on AWS S3 and distributed via CloudFront guarantees high availability (99.95%) and low latency for global users. Modularizing the frontend into dedicated components ensures clean separation of concerns, secure authentication, and seamless adherence to strict performance and compliance constraints.]