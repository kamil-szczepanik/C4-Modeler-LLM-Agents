## Overview
The Online Bookstore is a cloud-native e-commerce system built to sell physical and electronic books with recommendations, reviews, and secure global checkout. It delivers high scalability, multi-currency support, and strict compliance with data privacy regulations.

## Key Elements
* **Customer**: End-user accessing the system via Web Browser or Mobile App.
* **Store Administrator**: Internal user managing inventory and pricing via Web Browser.
* **Online Bookstore System**: Core cloud-native retail platform hosted on AWS.
* **Payment Gateway**: External Stripe/PayPal system handling secure checkout and multi-currency transactions.
* **Third-Party Shipping Provider API**: External service calculating shipping rates and tracking.
* **Notification Service**: External AWS SES/Twilio system dispatching alerts.
* **Identity Provider / OAuth 2.0 Service**: External Auth0 or AWS Cognito service managing authentication.
* **Currency Exchange Rate Service**: External API fetching daily conversion rates.

## Relationships
* **Customer** interacts with **Online Bookstore System** via HTTPS/REST (Web/Mobile).
* **Store Administrator** interacts with **Online Bookstore System** via HTTPS/REST.
* **Online Bookstore System** calls **Payment Gateway** via HTTPS/REST for transactions.
* **Online Bookstore System** calls **Third-Party Shipping Provider API** via HTTPS/REST for logistics.
* **Online Bookstore System** integrates with **Notification Service** via SMTP/APIs.
* **Online Bookstore System** authenticates users via **Identity Provider / OAuth 2.0 Service** using OIDC/HTTPS.
* **Online Bookstore System** queries **Currency Exchange Rate Service** via HTTPS/REST for USD, EUR, and GBP rates.

## Technology Stack
* **AWS Cloud**: Multi-region hosting (us-east-1, eu-west-1, ap-southeast-1) ensuring 99.95% uptime and 1M MAU scalability.
* **Auth0 / AWS Cognito**: Provides secure OIDC authentication meeting GDPR/CCPA and OWASP requirements.
* **Stripe / PayPal**: Secures multi-currency transactions (USD, EUR, GBP).
* **AWS SES / Twilio**: Delivers reliable transactional notifications.
* **HTTPS / REST / SMTP**: Protocols ensuring secure communication and integration with external third-party services.

## Rationale
This architecture isolates third-party financial, logistical, and identity dependencies to maintain a secure, compliant, and highly available global retail platform. Distributing services across multiple AWS regions directly supports the 99.95% uptime and low-latency performance requirements.