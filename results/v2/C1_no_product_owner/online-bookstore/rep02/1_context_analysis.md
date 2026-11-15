## Overview
A scaled-down Amazon-style e-commerce platform for purchasing books, providing personalized recommendations, and managing customer reviews globally. Designed for high availability, security, and multi-region deployment.

## Key Elements
* **Customer (Person):** End-user browsing, purchasing, and reviewing books.
* **Administrator (Person):** Manages catalogue, orders, and content moderation.
* **Online Bookstore System (Software System):** Core e-commerce platform.
* **Payment Gateway (External System):** Stripe/PayPal for secure checkout and multi-currency support.
* **Shipping Provider (External System):** FedEx/UPS APIs for fulfillment and tracking.
* **Email/Notification Service (External System):** SendGrid/AWS SES for transactional emails.
* **Identity Provider (External System):** AWS Cognito for OIDC/OAuth 2.0 authentication.

## Relationships
* **Customer / Administrator -> Online Bookstore System:** Interacts via HTTPS (TLS 1.3) through AWS CloudFront/WAF edge.
* **Online Bookstore System -> Identity Provider:** Authenticates via OIDC/HTTPS.
* **Online Bookstore System -> Payment Gateway:** Executes tokenized payments via HTTPS/REST.
* **Online Bookstore System -> Shipping Provider:** Manages fulfillment via HTTPS/REST.

## Technology Stack
* **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region redundancy.
* **Edge Security:** AWS CloudFront and AWS WAF for OWASP Top-10 mitigation and TLS 1.3 enforcement.
* **Global Routing:** AWS Route 53 with latency-based DNS failover for 99.95% availability.
* **Authentication:** AWS Cognito (OIDC/OAuth 2.0) with MFA for administrative sessions.
* **Secret Management:** AWS Secrets Manager for dynamic credential and API key injection.
* **Infrastructure as Code:** Terraform with GitOps pipelines for configuration management.

## Rationale
The architecture ensures GDPR, CCPA, and PCI-DSS compliance through strict edge security, tokenization, and data residency controls. Multi-region AWS deployment with Route 53 and strict availability patterns achieve the 99.95% uptime and <2s page load NFRs.