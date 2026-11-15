## Overview
The Online Bookstore is a multi-region e-commerce platform built on AWS to support global book sales with recommendations and reviews. Its core purpose is to provide a scalable, secure, and compliant shopping experience handling 1M MAU across three regions.

## Key Elements
* Customers and Client Applications (Web browser, native mobile apps)
* CDN (Content Delivery Network)
* Online Bookstore Core System (Containers: API Gateway, Web App, Recommendation Engine, Search Service)
* External Systems: Payment Gateway, Tax Calculation Service, Third-Party Shipping Provider, Notification Services (Email/SMS)
* External Infrastructure/SaaS: Identity Provider (IdP), Monitoring and Observability (APM), Secret Management Service (AWS Secrets Manager), Feature Flag Service, Currency Exchange Rate Service

## Relationships
* Customers interact with Client Applications via HTTPS.
* Client Applications fetch static assets and catalogue data (R-01) from the CDN via HTTPS.
* Client Applications communicate with the Online Bookstore Core System using REST/GraphQL over HTTPS.
* Online Bookstore integrates synchronously via HTTPS with Payment Gateway, Tax Calculation Service, and Currency Exchange Rate Service during checkout (R-02).
* Online Bookstore integrates asynchronously via event buses with Third-Party Shipping Provider and Notification Services.
* Core System utilizes AWS Secrets Manager and IdP securely via internal AWS VPC peering/IAM.

## Technology Stack
* AWS Cloud Infrastructure (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global scalability.
* CDN (Amazon CloudFront) for sub-2-second page loads on 3G networks.
* AWS Secrets Manager for credential security meeting OWASP Top-10 requirements.
* Asynchronous message queues for decoupled, resilient third-party integrations (shipping, notifications).

## Rationale
This multi-region, decoupled architecture guarantees high availability (99.95% uptime) and performance under heavy load while isolating PII to satisfy GDPR and CCPA compliance. Asynchronous boundaries and externalized SaaS dependencies ensure the critical checkout path remains resilient against third-party latency.