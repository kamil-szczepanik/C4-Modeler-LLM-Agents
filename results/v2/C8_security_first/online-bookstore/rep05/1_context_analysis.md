## Overview
The Online Bookstore is a cloud-native e-commerce platform built to serve 1 million active users globally with high availability and regulatory compliance. It provides secure catalogue browsing, multi-currency checkout, AI-driven recommendations, and automated customer data management.

## Key Elements
* Customers (Shoppers/Readers)
* Store Administrators
* Online Bookstore System (AWS Microservices Platform)
* Stripe / PayPal (Payment Gateway)
* FedEx / UPS (Shipping Provider APIs)
* AWS Cognito / Auth0 (Identity Provider)
* AWS SES / SendGrid (Notification Service)

## Relationships
* Customers & Store Administrators -> Online Bookstore System via HTTPS (TLS 1.3, Web/Mobile, MFA for admins)
* Online Bookstore System -> Payment Gateway via HTTPS/REST (OAuth 2.0, Tokenization)
* Online Bookstore System -> Shipping Provider APIs via HTTPS/REST (API Key/HMAC)
* Online Bookstore System -> Identity Provider via HTTPS/REST (OIDC / OAuth 2.0)
* Online Bookstore System -> Notification Service via HTTPS/REST

## Technology Stack
* Cloud Platform: AWS (us-east-1, eu-west-1, ap-southeast-1 regions) for global scalability
* Routing & Security: AWS Route 53 (latency-based routing), AWS WAF (DDoS/OWASP mitigation)
* Database & Storage: AWS Aurora Global Databases (Active-Passive with read replicas) for consistency and GDPR compliance
* Secrets Management: AWS Secrets Manager with automated rotation for API credentials
* Observability: AWS OpenTelemetry / X-Ray for distributed tracing and performance monitoring

## Rationale
The AWS-based microservices architecture with regional read replicas ensures 99.95% uptime and sub-2-second page loads for 1M MAU while simplifying multi-region GDPR/CCPA data purges. Utilizing managed services like AWS Cognito and Stripe decouples authentication and payment complexities, ensuring PCI-DSS compliance and secure multi-currency transactions.