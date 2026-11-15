## Overview
The Online Bookstore is a globally distributed e-commerce platform designed to support 1 million monthly active users with multi-currency checkout, secure payments, and strict regulatory compliance. It provides catalog browsing, search, recommendations, and reviews while maintaining high availability across three AWS regions.

## Key Elements
* **Customers & Admins:** End-users and internal support staff accessing the platform.
* **Online Bookstore System:** Core e-commerce platform deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
* **Global Edge Layer:** CDN and edge routing layer with AWS WAF and AWS Shield.
* **External Systems:** Stripe/PayPal (Payment Gateway), FedEx/UPS (Shipping APIs), SendGrid/AWS SES (Notification Service), and Fixer/Open Exchange Rates (Currency Exchange Rate Provider).

## Relationships
* **Customer/Admin to Global Edge Layer:** HTTPS / TLS 1.3 via Global Anycast DNS (AWS Route 53).
* **Online Bookstore System to Payment Gateway & Shipping APIs:** HTTPS / REST / mTLS 1.3 for secure checkout and fulfillment.
* **Online Bookstore System to Currency Exchange Rate Provider:** HTTPS / REST / mTLS 1.3 with local caching and circuit breakers.
* **Online Bookstore System to Notification Service:** HTTPS / SMTP / TLS 1.3 for transactional messaging.

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for global scalability and multi-region redundancy.
* **Edge & Security:** AWS Route 53 (Anycast DNS), AWS WAF, and AWS Shield for OWASP Top-10 protection and global traffic routing.
* **Data Security:** AWS KMS with customer-managed keys (CMKs) enforcing regional PII data residency for GDPR/CCPA compliance.
* **Protocols:** TLS 1.3 and mTLS for all inbound, outbound, and inter-region communications.

## Rationale
This architecture utilizes a global edge layer with regional deployments to guarantee low-latency page loads and high availability. Isolating external payment and shipping dependencies ensures PCI-DSS scope reduction while meeting strict regulatory and performance SLAs.