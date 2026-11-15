## Overview
The Online Bookstore is a globally scaled e-commerce platform designed to deliver secure, multi-currency book purchasing, recommendations, and reviews. It ensures high availability, strict GDPR/CCPA compliance, and resilience for 1 million monthly active users across multiple regions.

## Key Elements
* **Customer:** End-user shopping for physical and electronic books.
* **Store Administrator:** Back-office user managing inventory and support.
* **Online Bookstore System:** Core AWS-hosted multi-region retail platform.
* **Payment Gateway:** Stripe/PayPal handling secure PCI-DSS checkout.
* **Third-Party Shipping/Carrier APIs:** FedEx/UPS managing physical fulfillment.
* **Tax Calculation Service:** Avalara/TaxJar for multi-region tax compliance.
* **Recommendation Provider:** AWS Personalize generating "Customers also bought" data.
* **Identity Provider:** AWS SES/OAuth managing authentication and notifications.

## Relationships
* **Customer** interacts with **Online Bookstore System** via HTTPS (Web/Mobile) using TLS 1.3.
* **Store Administrator** accesses **Online Bookstore System** via HTTPS with OAuth 2.0 / OIDC and MFA.
* **Online Bookstore System** integrates with **Payment Gateway** and **Tax Calculation Service** via TLS 1.3 / REST for checkout (R-02).
* **Online Bookstore System** connects to **Third-Party Shipping APIs** via HTTPS/REST webhooks using HMAC-SHA256 signing.
* **Online Bookstore System** fetches ML recommendations from **Recommendation Provider** via asynchronous gRPC/REST APIs.

## Technology Stack
* **Cloud Infrastructure:** AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee 99.95% uptime and low latency.
* **Security & Auth:** OAuth 2.0 / OIDC with AWS Secrets Manager for secret rotation and AES-256 data encryption at rest.
* **Integration Protocols:** TLS 1.3, HTTPS, REST, and gRPC for secure external and internal service communication.
* **Compliance & Data:** Tokenization and pseudonymization engines to enforce GDPR/CCPA data privacy constraints.

## Rationale
This multi-region AWS architecture decouples heavy ML recommendations and tax calculations to maintain sub-2-second page loads and scale effortlessly to 1 million active users. Offloading PCI-DSS scope to external payment gateways combined with robust boundary security ensures strict regulatory compliance and high availability.