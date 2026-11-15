## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It provides global catalogue browsing, secure multi-currency checkout, and fulfillment tracking for 1M MAU across AWS regions.

## Key Elements
* Customer (Person): End-user browsing books, managing cart, and submitting reviews.
* Admin / Support Staff (Person): Back-office users managing catalogue and fulfillment.
* Online Bookstore Software System (Container/Core System): The e-commerce platform handling core retail workflows.
* Payment Gateway (External System): Stripe/PayPal processing secure checkouts via REST/TLS.
* Shipping Provider APIs (External System): FedEx/UPS managing order fulfillment tracking via REST/JSON.
* Tax Calculation Service (External System): Avalara handling multi-region tax compliance (USD, EUR, GBP).
* Identity Provider / SSO Service (External System): Auth0 or AWS Cognito managing customer identity and sessions via OAuth2/OIDC.

## Relationships
* Customer interacts with Online Bookstore Software System via HTTPS (Web/Mobile App) for R-01 to R-04.
* Admin / Support Staff interacts with Online Bookstore Software System via HTTPS for back-office management.
* Online Bookstore Software System connects to Payment Gateway via REST/TLS for secure checkout (R-02).
* Online Bookstore Software System connects to Shipping Provider APIs via REST/JSON for fulfillment tracking.
* Online Bookstore Software System connects to Tax Calculation Service via REST/TLS for multi-region tax compliance.
* Online Bookstore Software System integrates with Identity Provider / SSO Service via OAuth2/OIDC over TLS for authentication.

## Technology Stack
* AWS (Cloud Provider): Deployed across us-east-1, eu-west-1, and ap-southeast-1 to meet scalability and availability targets.
* HTTPS / TLS: Secures all client-to-system and system-to-system transport layers for OWASP Top-10 mitigation (R-08).
* REST / JSON: Standardizes communication with third-party shipping APIs and tax services.
* OAuth2 / OIDC: Protocol used for federated identity management via Auth0 or AWS Cognito.

## Rationale
Isolating externalized payment, shipping, and tax systems ensures GDPR and CCPA compliance while limiting PCI-DSS data liability. Deploying across targeted AWS regions with decoupled identity and fulfillment dependencies guarantees 99.95% uptime and sub-2-second page loads for 1M MAU.