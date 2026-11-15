## Overview
The Online Bookstore is a cloud-native, multi-region e-commerce platform designed to provide a secure, high-performance shopping experience for physical and electronic books. It supports global customers and administrators while meeting strict scalability, availability, and data privacy requirements.

## Key Elements
* **Online Bookstore:** The core e-commerce software system hosted on AWS.
* **Customer:** End-user shopping, browsing, reviewing, and checking out.
* **Store Administrator:** Internal user managing inventory, catalogue, and fulfillment.
* **Payment Gateway:** External financial transaction processor (e.g., Stripe/PayPal).
* **Shipping Provider:** External physical logistics partner (e.g., FedEx/UPS).
* **Identity Provider (IdP):** External authentication service (e.g., Auth0/AWS Cognito).

## Relationships
* **Customer & Store Administrator to Online Bookstore:** HTTPS via AWS CloudFront CDN, enforcing TLS 1.3 and OAuth 2.0 / OIDC.
* **Online Bookstore to Payment Gateway:** HTTPS / REST API via TLS 1.3 with mTLS and HMAC webhook verification.
* **Online Bookstore to Shipping Provider:** HTTPS / REST API via TLS 1.3 with circuit breakers.
* **Online Bookstore to Identity Provider:** OIDC / OAuth 2.0 over HTTPS.

## Technology Stack
* **Cloud Infrastructure:** AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to ensure global reach and 99.95% availability.
* **Routing & Performance:** AWS Route 53 latency-based routing and AWS CloudFront CDN to maintain <2s page load times on 3G connections.
* **Security & Compliance:** AWS KMS with customer-managed keys and AWS Secrets Manager for dynamic credential rotation, satisfying GDPR/CCPA and OWASP Top-10 mandates.

## Rationale
This multi-region, cloud-native architecture ensures low-latency performance and high availability required for 1 million Monthly Active Users (MAU). Decoupling external dependencies via secure REST APIs, circuit breakers, and centralized identity management minimizes operational risk and ensures strict compliance with regulatory standards.