## Overview
A scaled-down Amazon-style e-commerce site for physical and electronic books with recommendations, reviews, and multi-currency support. It provides high availability and global scalability for 1 million monthly active users.

## Key Elements
* **Shopper / Reviewer (Person):** External users browsing catalogues, managing carts, submitting reviews, and purchasing books.
* **Store Administrator (Person):** Internal users managing inventory, order disputes, and sales metrics.
* **Online Bookstore System (Software System):** Core e-commerce platform hosted on AWS across us-east-1, eu-west-1, and ap-southeast-1.
* **Payment Gateway (External System):** Stripe or PayPal handling PCI-DSS compliant transactions.
* **Shipping Provider APIs (External System):** FedEx or UPS for order fulfillment.
* **Recommendation Engine (External System):** AWS Personalize providing machine-learning personalization.
* **Notification Service (External System):** SendGrid or Twilio managing transactional emails, SMS, and MFA codes.

## Relationships
* **Shopper / Reviewer -> Online Bookstore System:** HTTPS (TLS 1.3) for browsing, checkout, and reviews.
* **Store Administrator -> Online Bookstore System:** HTTPS (TLS 1.3) with OAuth 2.0/OIDC and MFA for backend management.
* **Online Bookstore System -> Payment Gateway:** Outbound HTTPS/REST with tokenization for secure payments.
* **Online Bookstore System -> Shipping Provider APIs:** Outbound HTTPS with mutual TLS (mTLS) for fulfillment data.
* **Online Bookstore System -> Recommendation Engine:** Outbound HTTPS/REST for personalization payloads.
* **Online Bookstore System -> Notification Service:** Outbound HTTPS/REST for customer alerts.

## Technology Stack
* **Cloud Infrastructure:** AWS deployed across us-east-1, eu-west-1, and ap-southeast-1 to ensure regional resilience.
* **Security & Compliance:** AWS KMS (AES-256) for data at rest, AWS WAF and CloudFront for edge security, TLS 1.3 for transit.
* **Traffic & Delivery:** AWS Route 53 for global traffic management and CloudFront CDN for edge caching and static asset delivery.
* **Observability:** AWS X-Ray and centralized log aggregation for distributed tracing across all regions.

## Rationale
* The multi-region AWS deployment with edge caching guarantees 99.95% uptime and sub-2-second page loads for global users.
* Strict external tokenization and encryption standards ensure full GDPR, CCPA, and OWASP Top-10 compliance.