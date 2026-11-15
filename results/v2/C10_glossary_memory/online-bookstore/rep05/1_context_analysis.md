## Overview
An AWS-hosted global online bookstore handling 1 million monthly active users with multi-currency support and secure e-commerce operations. It provides catalogue browsing, secure checkout, reviews, and personalized book recommendations.

## Key Elements
- **Customers / Shoppers**: End-users browsing catalogues and purchasing books.
- **Registered Users / Reviewers**: Authenticated customers writing reviews and ratings.
- **Store Administrators**: Internal staff managing content and catalogue accuracy.
- **Online Bookstore System**: Core React/Node.js/Java microservices platform on AWS.
- **Payment Gateway**: Stripe/PayPal handling secure tokenized transactions.
- **Third-Party Shipping APIs**: FedEx/UPS/DHL providing real-time rates.
- **Identity Provider**: AWS Cognito managing OAuth2/OIDC authentication.
- **Analytics & Monitoring Platform**: Datadog/Segment tracking checkout friction and telemetry.

## Relationships
- **Customer to Online Bookstore**: HTTPS (TLS 1.3) via global CDN/WAF and Route 53 latency-based routing.
- **Online Bookstore to Payment Gateway**: HTTPS/REST using tokenized iframe SDKs for PCI-DSS compliance.
- **Online Bookstore to Shipping Providers**: HTTPS/REST with circuit breakers and fallback caching.
- **Online Bookstore to Identity Provider**: OAuth2/OIDC with short-lived JWTs.
- **Online Bookstore to AWS Cognito / AWS CloudWatch**: Internal mTLS and AES-256 encryption-at-rest.

## Technology Stack
- **Cloud Infrastructure**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` regions for global resilience.
- **Frontend/Backend**: React SPA with Node.js and Java microservices.
- **Security & Compliance**: AWS WAF, TLS 1.3, AWS Cognito, and AES-256 KMS encryption for GDPR/CCPA and OWASP mitigation.
- **Observability**: AWS CloudWatch, OpenSearch, and synthetic monitoring for 99.95% uptime.

## Rationale
This architecture ensures high availability (99.95%) and low latency (<2s) for 1M MAU through multi-region AWS deployment and edge traffic routing. Security measures like tokenized payments and WAF protection satisfy stringent GDPR, CCPA, and PCI-DSS compliance constraints.