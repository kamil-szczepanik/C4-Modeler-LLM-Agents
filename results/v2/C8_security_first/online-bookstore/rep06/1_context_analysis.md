## Overview
The Online Bookstore is a globally scaled e-commerce platform designed to support catalogue browsing, secure checkout, 5-star reviews, and personalized recommendations for 1 million monthly active users. It meets strict multi-region availability, compliance, and performance requirements via AWS cloud infrastructure.

## Key Elements
- **Shoppers**: End-users browsing catalogues, managing carts, and purchasing books.
- **Vendors & Admins**: Internal users managing inventory, catalogue listings, and order disputes.
- **Online Bookstore Software System**: Core AWS-hosted retail platform handling business logic.
- **Payment Gateway**: External PCI-compliant payment processor (Stripe/PayPal).
- **Third-Party Shipping APIs**: External fulfillment and tracking providers (FedEx/UPS).
- **Notification Service**: External transactional email SaaS provider (AWS SES/SendGrid).
- **Recommendation Engine**: Internal subsystem handling real-time "Customers also bought" suggestions.

## Relationships
- **Shopper** -> **Online Bookstore**: HTTPS via AWS CloudFront and WAF for catalogue browsing, search, and checkout.
- **Vendor & Admin** -> **Online Bookstore**: HTTPS with enforced MFA for management console access.
- **Online Bookstore** -> **Payment Gateway**: REST/HTTPS for secure tokenized checkout transactions.
- **Online Bookstore** -> **Third-Party Shipping APIs**: REST/HTTPS for fulfillment and tracking integration.
- **Online Bookstore** -> **Notification Service**: REST/HTTPS over TLS 1.3 for asynchronous transactional emails.

## Technology Stack
- **Cloud Infrastructure**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee high availability.
- **Global Routing & Edge**: AWS Route 53 with latency-based routing and AWS CloudFront with WAF for performance and security.
- **Security Protocols**: TLS 1.3 for data in transit; AES-256 for data at rest to satisfy GDPR and CCPA.
- **Resilience Patterns**: AWS SQS and circuit breakers to isolate third-party failures.

## Rationale
This multi-region AWS architecture ensures 99.95% uptime and sub-2-second page loads globally while isolating PCI-DSS and GDPR compliance scopes. Edge caching and decoupled third-party integrations successfully support the 1 million MAU scaling constraint.