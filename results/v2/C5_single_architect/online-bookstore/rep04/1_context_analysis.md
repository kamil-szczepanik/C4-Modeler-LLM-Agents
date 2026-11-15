## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books. It provides catalogue browsing, secure checkout, reviews, and personalized recommendations.

## Key Elements
*   **Customer (Person)**: End-user browsing books, managing cart, and purchasing via web/mobile browsers.
*   **Online Bookstore System**: Core software boundary encompassing catalog, checkout, recommendations, and reviews.
*   **Payment Gateway (External System)**: Handles secure checkout and multi-currency transactions (USD, EUR, GBP).
*   **Shipping Provider API (External System)**: Manages logistics, shipping labels, and tracking.
*   **Identity Provider / OAuth (External System)**: Manages secure customer authentication.
*   **Notification Service (External System)**: Sends transactional emails and SMS for order confirmations and resets.
*   **Tax Calculation Service (External System)**: Calculates regional taxes for compliance during checkout.

## Relationships
*   **Customer -> Online Bookstore**: Browses catalogue, manages cart, and completes checkout via HTTPS.
*   **Online Bookstore -> Payment Gateway**: Processes secure multi-currency payments via HTTPS/REST.
*   **Online Bookstore -> Shipping Provider API**: Requests fulfillment and tracks shipments via HTTPS/REST.
*   **Online Bookstore -> Identity Provider / OAuth**: Authenticates users securely via OIDC/OAuth2 over HTTPS.
*   **Online Bookstore -> Notification Service**: Dispatches transactional alerts via HTTPS/REST.
*   **Online Bookstore -> Tax Calculation Service**: Queries regional tax rates during checkout via HTTPS/REST.

## Technology Stack
*   **AWS (Cloud Provider)**: Deployed across us-east-1, eu-west-1, and ap-southeast-1 for global scalability and 99.95% availability.
*   **HTTPS / REST**: Used for all external integrations to ensure secure communication and OWASP Top-10 mitigation.
*   **OAuth2 / OIDC**: Used for secure customer authentication.

## Rationale
This multi-region AWS architecture ensures 99.95% availability and sub-2-second performance for 1M MAU globally. Externalizing payments, taxes, and shipping reduces compliance scope while satisfying GDPR, CCPA, and multi-currency constraints.