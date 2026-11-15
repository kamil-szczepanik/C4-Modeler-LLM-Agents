## Overview
- An Amazon-style e-commerce Online Bookstore system for browsing, purchasing, and reviewing physical and electronic books.
- Built for global scale (1M MAU) with multi-region deployment, stringent compliance, and high availability.

## Key Elements
- Customers (End-users)
- Online Bookstore Software System
- AWS CloudFront + AWS WAF (CDN / Edge Security)
- AWS Route 53 (DNS & Latency-Based Routing)
- Identity Provider (AWS Cognito / Auth0 via OIDC)
- Payment Gateway (Stripe / PayPal via REST/TLS)
- Shipping Provider APIs (FedEx / UPS via REST/TLS)
- Email / Notification Service (AWS SES / SendGrid via SMTP/REST)

## Relationships
- Customer -> AWS CloudFront/WAF: Routes web requests via HTTPS
- AWS Route 53 -> Online Bookstore: Directs latency-based traffic across regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`)
- Online Bookstore -> Identity Provider: Authenticates users via OIDC/OAuth2/HTTPS
- Online Bookstore -> Payment Gateway: Processes secure tokenized transactions via REST/TLS 1.3
- Online Bookstore -> Shipping Provider APIs: Calculates rates and fulfillment via REST/TLS
- Online Bookstore -> Notification Service: Dispatches transactional emails via SMTP/REST

## Technology Stack
- AWS Global Infrastructure: Multi-region hosting (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for low latency and high availability
- AWS CloudFront & WAF: Edge caching and OWASP Top-10 security mitigations
- Route 53: Latency-based DNS routing with health checks for automatic failover
- AWS KMS & Secrets Manager: Region-isolated encryption keys and credential rotation
- OIDC / OAuth2: Centralized authentication supporting MFA

## Rationale
- Multi-region AWS architecture guarantees 99.95% uptime and sub-2-second global page loads for 1M MAU.
- Edge security controls, data residency enforcement, and tokenized payments ensure strict GDPR, CCPA, and PCI-DSS compliance.