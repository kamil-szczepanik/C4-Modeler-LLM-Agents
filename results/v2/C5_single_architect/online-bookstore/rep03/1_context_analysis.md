## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed for purchasing physical and electronic books with recommendations and reviews. It provides global retail capabilities while maintaining multi-currency support, stringent security, and GDPR/CCPA compliance across multiple AWS regions.

## Key Elements
* **Customer (Person):** End-user browsing catalogues, purchasing items, and leaving reviews.
* **Administrator (Person):** Manages inventory, pricing, and content moderation.
* **Online Bookstore System (Software System):** Core e-commerce platform hosted on AWS.
* **Payment Gateway (External System):** Stripe or PayPal for secure checkout and multi-currency transactions.
* **Shipping Provider APIs (External System):** Third-party logistics for fulfillment tracking.
* **Email Service (External System):** Sendgrid or AWS SES for transactional notifications.
* **Identity Provider (External System):** Auth0 or AWS Cognito for authentication and compliance.
* **Tax Calculation Service (External System):** Avalara or TaxJar for regional tax calculations.

## Relationships
* **Customer** uses **Online Bookstore System** via HTTPS for browsing, purchasing, and reviews (R-01 to R-04).
* **Online Bookstore System** calls **Payment Gateway** via REST/TLS for secure checkout.
* **Online Bookstore System** calls **Shipping Provider APIs** via REST/JSON for fulfillment tracking.
* **Online Bookstore System** calls **Identity Provider** via OIDC/OAuth2/HTTPS for user authentication.
* **Online Bookstore System** calls **Tax Calculation Service** via REST/TLS for dynamic regional tax computation.

## Technology Stack
* **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region availability and scalability.
* **Protocols:** HTTPS, REST, TLS, OIDC, OAuth2 for secure transport and authentication.
* **Auth & Compliance:** Auth0/AWS Cognito for identity management supporting GDPR/CCPA.
* **Payments & Logistics:** Stripe/PayPal and third-party shipping APIs for financial and fulfillment integration.

## Rationale
This architecture leverages multi-region AWS cloud infrastructure to guarantee 99.95% availability, sub-2-second performance, and scalability for 1 million MAU. Externalized specialized services ensure strict compliance with PCI-DSS, GDPR, CCPA, and global tax regulations.