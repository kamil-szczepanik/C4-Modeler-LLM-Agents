## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It operates globally across AWS regions while maintaining strict GDPR/CCPA compliance and multi-currency support.

## Key Elements
* **Customer:** End-user accessing the platform via web or mobile.
* **Online Bookstore System:** Core e-commerce platform handling catalogue, cart, checkout, reviews, and recommendations.
* **Third-Party Payment Gateway:** External system (Stripe/PayPal) for secure checkout.
* **Third-Party Shipping Provider:** External system (FedEx/DHL) for order fulfillment and tracking.
* **Identity Provider / Auth Service:** External system (Auth0/AWS Cognito) for authentication and identity management.
* **Currency Exchange Rate Service:** External system providing multi-currency conversion (USD, EUR, GBP).

## Relationships
* **Customer -> Online Bookstore:** Browses, purchases, and leaves reviews via HTTPS.
* **Customer -> Online Bookstore:** Authenticates using OIDC over HTTPS.
* **Online Bookstore -> Third-Party Payment Gateway:** Processes transactions via HTTPS/REST.
* **Online Bookstore -> Third-Party Shipping Provider:** Requests fulfillment via HTTPS/REST.
* **Online Bookstore -> Currency Exchange Rate Service:** Fetches live rates via HTTPS/REST.

## Technology Stack
* **AWS:** Target cloud provider spanning us-east-1, eu-west-1, and ap-southeast-1 for global availability and scalability.
* **HTTPS/REST:** Primary protocol for secure integrations with external payment, shipping, and currency services.
* **OIDC / OAuth2:** Protocols used with Auth0 or AWS Cognito for secure customer authentication.

## Rationale
This architecture leverages multi-region AWS infrastructure to achieve 99.95% availability and sub-2-second page loads for 1 million monthly active users. Integrating specialized external SaaS for auth, payments, and shipping ensures compliance, multi-currency support, and robust OWASP-level security.