## Overview
An Amazon-style e-commerce platform enables users to browse, search, and purchase physical and electronic books with integrated reviews and recommendations. The cloud-native system ensures high availability, strict regulatory compliance, and seamless multi-currency support across global regions.

## Key Elements
* **Customer / Reviewer:** End-users browsing catalogues, purchasing items, managing carts, and submitting 5-star ratings.
* **Store Administrator:** Internal personnel managing catalogue integrity, fulfillment, and GDPR/CCPA compliance.
* **Online Bookstore System:** Core platform encompassing microservices behind an API Gateway with an anti-corruption layer.
* **Payment Gateway:** External service processing secure multi-currency checkouts (USD, EUR, GBP).
* **Shipping / Fulfillment Provider:** External API handling physical book logistics.
* **Identity Provider:** AWS Cognito / Auth0 managing customer authentication and OIDC/OAuth 2.0 flows.
* **Notification Service:** AWS SES / SendGrid delivering order confirmations and review prompts.

## Relationships
* **Customer -> Online Bookstore:** Browses, searches, and checks out via HTTPS (Web/Mobile).
* **Customer / Reviewer -> Identity Provider:** Authenticates and authorizes via HTTPS / OpenID Connect.
* **Online Bookstore -> Identity Provider:** Validates tokens via JWT / JWKS.
* **Online Bookstore -> Payment Gateway:** Authorizes transactions via HTTPS / REST (TLS 1.3, PCI-DSS).
* **Online Bookstore -> Shipping Provider:** Dispatches fulfillment orders via HTTPS / REST Webhooks.
* **Online Bookstore -> Notification Service:** Triggers transactional emails via SMTP / API.

## Technology Stack
* **Cloud Infrastructure:** AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee 99.95% uptime and low latency.
* **Edge & Security:** AWS CloudFront with Edge WAF for OWASP Top-10 mitigation, DDoS protection, and sub-2s global page loads.
* **Data Protection & Encryption:** TLS 1.3 for transit, AES-256 for databases/caches, and AWS KMS for PII payload encryption in messaging queues.
* **Identity & Access:** AWS Cognito / Auth0 for OIDC/OAuth 2.0, paired with AWS Secrets Manager for rotating API keys.
* **Resilience & Observability:** OpenTelemetry for distributed tracing, with circuit breakers and asynchronous queues for third-party API fault isolation.

## Rationale
This multi-region AWS architecture achieves sub-2-second performance and 99.95% availability to support 1 million MAU without degradation. Strict cryptographic boundaries and edge security controls ensure full compliance with GDPR, CCPA, and PCI-DSS standards.