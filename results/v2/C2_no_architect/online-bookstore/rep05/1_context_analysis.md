## Overview
The Online Bookstore is a globally distributed, Amazon-style e-commerce platform designed to support physical and electronic book sales, personalized recommendations, and reviews. Its core purpose is to deliver secure, multi-currency shopping and fulfillment while handling 1M MAU globally.

## Key Elements
- **Customers (Shoppers):** End-users browsing catalogues, managing carts, and purchasing books.
- **Authors/Publishers:** Secondary users accessing sales analytics and review feedback.
- **Store Administrators:** Back-office staff managing catalogues, moderation, and fulfillment.
- **Online Bookstore System:** Core platform handling catalog search, cart, reviews, and recommendations.
- **External Systems:** Payment Gateway (Stripe/PayPal) and Third-Party Shipping Provider APIs.
- **Infrastructure:** AWS Global DNS (Route 53), CDN/Edge Services, and Multi-Region AWS infrastructure (`us-east-1`, `eu-west-1`, `ap-southeast-1`).

## Relationships
- Customers interact with Edge/CDN and Online Bookstore via HTTPS/TLS 1.3.
- Online Bookstore integrates with Payment Gateways via Tokenized Client-Side SDKs and TLS 1.3.
- Online Bookstore integrates with Third-Party Shipping APIs via HTTPS.
- Internal service-to-service communication uses mTLS service mesh policies.

## Technology Stack
- **Cloud Provider:** AWS across three regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for low latency and high availability.
- **Global Delivery & DNS:** Amazon Route 53 with latency-based routing and Edge/CDN services for <2s page loads on 3G.
- **Security & Identity:** OAuth 2.0 / OIDC with MFA, AWS KMS for encryption at rest, and AWS Secrets Manager for secret rotation.
- **Observability:** AWS CloudWatch and OpenTelemetry for distributed tracing and centralized immutable audit logging.

## Rationale
This architecture uses a multi-region AWS deployment with edge caching to meet the 99.95% uptime SLA and strict <2s global performance constraints. Strict data residency boundaries and tokenized payments ensure full GDPR, CCPA, and PCI-DSS compliance without compromising user experience.