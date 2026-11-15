## Overview
The Admin Dashboard Container is an internal React Single Page Application that enables Store Administrators to manage catalog integrity, order fulfillment, and GDPR/CCPA compliance. It provides secure administrative tooling with strict access controls and telemetry to support high operational availability.

## Key Elements
* Store Administrator [person, context]: Internal user managing catalogue integrity, fulfillment, and GDPR/CCPA compliance.
* Admin Dashboard Container [container, container] (React): Internal management interface hosted on AWS S3 + CloudFront.
* Catalog Management Component [component] (React): UI views for bulk inventory updates and review moderation.
* Order Fulfillment Component [component] (React): Dashboard views displaying shipping exceptions and order statuses.
* Compliance & Audit Component [component] (React): Interface handling GDPR/CCPA data export and deletion workflows.
* Admin State Management & Telemetry Component [component] (React Context / Redux Toolkit): Manages token expiration, idle timeouts, and error boundaries.
* API Gateway / BFF Container [container, container] (AWS API Gateway / Envoy): Secure routing layer for downstream microservices.
* Identity Provider [externalSystem, container] (AWS Cognito / Auth0): Manages OIDC/OAuth 2.0 authentication and JWT issuance.

## Relationships
* Store Administrator -> Admin Dashboard Container (HTTPS)
* Admin Dashboard Container -> Identity Provider (HTTPS / OpenID Connect via JWT / JWKS)
* Admin Dashboard Container -> API Gateway / BFF Container (Internal mTLS / REST with JWT claims)
* Admin Dashboard Container -> AWS S3 + CloudFront (HTTPS / CloudFront Functions / AWS WAF)

## Technology Stack
* React & Redux Toolkit: Powers modular UI components and centralized state management.
* AWS S3 & CloudFront: Delivers fast global static hosting with Lambda@Edge/CloudFront Functions.
* AWS WAF & IAM: Enforces IP allowlisting, rate-limiting, and Role-Based Access Control.
* Amazon CloudWatch & Sentry: Provides real-user monitoring, error tracking, and immutable audit logging.

## Rationale
This architecture ensures secure, isolated administrative access adhering to stringent compliance mandates while maintaining 99.95% uptime. Decoupling the UI via AWS S3 and CloudFront guarantees fast global performance and low operational overhead.