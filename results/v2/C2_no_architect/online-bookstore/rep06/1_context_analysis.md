## Overview
An Amazon-style global e-commerce platform designed to sell physical and electronic books with integrated reviews, recommendations, and multi-currency support. It provides high availability and low latency for millions of users across multiple AWS regions.

## Key Elements
* **Book Buyer:** Primary customer interacting via web/mobile frontends.
* **Store Administrator & Author/Publisher Partner:** Administrative users managing catalogues, permissions, and analytics.
* **AWS CloudFront & WAF:** Edge caching and security boundary.
* **API Gateway & Microservices:** Core containers handling catalogue, cart, checkout, reviews, and recommendations.
* **External Systems:** Third-Party Payment Gateways and Shipping APIs.

## Relationships
* **Book Buyer to CloudFront/WAF:** HTTPS (TLS 1.3) for catalogue browsing, checkout, and reviews.
* **Microservices to Payment Gateway:** HTTPS (TLS 1.2+) with client-side tokenization.
* **Microservices to Shipping APIs:** Asynchronous messaging via Amazon SQS and HTTPS.
* **Services to Databases:** Encrypted TCP connections to regional read replicas and KMS.

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) utilizing Route 53 latency-based routing for multi-region scale.
* **Security & Auth:** AWS WAF, KMS, OAuth 2.0 / OIDC, and TLS 1.3 for OWASP Top-10 and GDPR/CCPA compliance.
* **Resilience & Messaging:** Amazon SQS and circuit breakers for decoupling third-party shipping APIs.
* **Performance:** Amazon CloudFront for edge caching static assets to achieve sub-2s load times.

## Rationale
The distributed AWS multi-region architecture guarantees 99.95% uptime and sub-second performance for 1M MAU. Asynchronous queuing and strict data encryption ensure regulatory compliance and operational resilience during third-party outages.