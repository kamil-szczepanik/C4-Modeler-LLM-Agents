## Overview
An AWS-hosted online bookstore built for 1M MAU, delivering catalog browsing, secure checkout, reviews, and personalized recommendations. The architecture prioritizes global performance, strict compliance, and 99.95% uptime.

## Key Elements
*   **Customers, Authors/Publishers, Store Administrators:** Primary system users interacting via web and mobile interfaces.
*   **Online Bookstore System:** Core e-commerce platform processing catalogs, carts, orders, and reviews.
*   **External Systems:** Payment Gateway, Third-Party Shipping APIs, Notification Service (SES/SendGrid), Customer Support CRM, and Identity Provider (AWS Cognito/Auth0).
*   **Infrastructure & Security Components:** AWS CloudFront CDN/WAF, Route 53, AWS Secrets Manager, and AWS KMS.

## Relationships
*   **Users to Bookstore:** Connect via HTTPS (TLS 1.3) through CDN/WAF with OAuth 2.0 / OIDC authentication.
*   **Bookstore to Payment Gateway:** Integrates via HTTPS / REST APIs with client-side tokenization and webhook callbacks.
*   **Bookstore to Shipping Providers & CRM:** Integrates via HTTPS / REST APIs for fulfillment and support synchronization.
*   **Bookstore to IdP:** Authenticates users via OIDC/OAuth 2.0 over HTTPS.

## Technology Stack
*   **Cloud Provider:** AWS across regions `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global availability.
*   **Edge & Security:** AWS WAF and CloudFront for DDoS protection, TLS 1.3 termination, and sub-2s latency.
*   **Data & Secrets:** AWS KMS (AES-256) for encryption at rest and AWS Secrets Manager for dynamic credential rotation.
*   **Authentication:** AWS Cognito or Auth0 via OIDC/OAuth 2.0 supporting MFA.

## Rationale
Multi-region AWS deployment with edge caching ensures sub-2-second page loads globally while meeting the 99.95% uptime SLA. Zero-trust boundaries, tokenization, and strict data management natively fulfill GDPR, CCPA, and PCI-DSS compliance requirements.