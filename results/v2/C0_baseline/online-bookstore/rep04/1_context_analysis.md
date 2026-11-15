## Overview
An Amazon-style global online bookstore system providing catalog browsing, secure checkout, reviews, and personalized recommendations. The architecture ensures GDPR/CCPA compliance, multi-currency support, and high availability across three AWS regions.

## Key Elements
- **Book Buyer / Customer:** End-user interacting via Web/Mobile clients over HTTPS.
- **Registered Reviewer:** User contributing reviews and 5-star ratings.
- **Store Administrator / Content Manager:** Manages catalog integrity, pricing, and content moderation.
- **Online Bookstore System:** Core AWS-hosted system containing e-commerce, catalog, review, and recommendation containers.
- **Stripe / PayPal:** External payment gateway for secure checkout and PCI-DSS offloading.
- **FedEx / UPS:** External shipping APIs for rate calculation and fulfillment.
- **Auth0 / AWS Cognito:** External Identity Provider handling authentication, MFA, and GDPR consent.
- **AWS SES:** External notification service for transactional emails.
- **Currency Exchange Rate Service:** External provider for daily multi-currency conversion rates.

## Relationships
- **Clients to Online Bookstore:** HTTPS via TLS 1.3, routed via AWS Route 53 Geo-DNS/Latency-based routing.
- **Online Bookstore to Stripe/PayPal:** REST/HTTPS for secure payment processing.
- **Online Bookstore to FedEx/UPS:** REST/HTTPS with circuit breakers and fallback queues for shipping.
- **Online Bookstore to Auth0/AWS Cognito:** Scoped OAuth2/JWT tokens and mTLS for identity management.
- **Online Bookstore to AWS SES:** HTTPS/SMTP with DMARC, DKIM, and SPF enforcement for notifications.
- **Online Bookstore to Currency Exchange Service:** REST/HTTPS with aggressive Redis caching.

## Technology Stack
- **Cloud Infrastructure:** AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to support global reach and 99.95% uptime.
- **Caching & State:** Amazon ElastiCache (Redis) for catalog browsing and currency rate lookups to handle traffic spikes.
- **Messaging & Resilience:** AWS SQS with Dead Letter Queues (DLQ) and circuit breakers for asynchronous external service integration.
- **Security & Compliance:** AWS Secrets Manager for credential rotation, AWS KMS with CMKs for data-at-rest encryption, and AWS CloudWatch Synthetics for monitoring.

## Rationale
This architecture guarantees 99.95% availability and sub-2-second performance for 1M MAU through multi-region AWS deployment, global caching, and resilient asynchronous integration patterns. Security and regulatory constraints are satisfied by offloading PCI-DSS to payment gateways, centralizing identity management, and enforcing strict data-in-transit and encryption controls for GDPR/CCPA compliance.