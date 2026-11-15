## Overview
The Online Bookstore is a globally distributed e-commerce platform built to handle physical and electronic book sales, recommendations, and reviews. It delivers high scalability, strict security compliance, and multi-currency support across multiple geographic regions.

## Key Elements
- **Users:** Customer (Shopper), Registered Customer/Reviewer, Site Administrator/Content Moderator.
- **External Systems:** Payment Gateway (Stripe/PayPal), Third-Party Shipping APIs (FedEx/UPS), Identity Provider (Auth0/AWS Cognito), Notification Service, and Supplier Feeds/ERP.
- **Containers:** AWS CloudFront / Global Accelerator (CDN/Edge), API Gateway with AWS WAF, AWS ECS/EKS Containerized Microservices (Catalog, Cart/Checkout, Recommendations), and Regional Databases.

## Relationships
- **Customer to CDN:** HTTPS / TLS 1.3
- **CDN to API Gateway:** HTTPS
- **Microservices to Identity Provider:** OAuth2 / OIDC over HTTPS
- **API Gateway to Payment Gateway & Shipping APIs:** HTTPS / REST
- **Online Bookstore to Notification Service:** HTTPS / REST Webhooks
- **Supplier Feeds to Online Bookstore:** Secure SFTP / S3 Batch Drops
- **Internal Microservices:** Mutual TLS (mTLS) via Service Mesh (Istio / AWS App Mesh)

## Technology Stack
- **Cloud Infrastructure:** AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region redundancy and low global latency.
- **Edge Delivery:** AWS CloudFront and Global Accelerator to satisfy the sub-2-second 3G page load requirement.
- **Compute:** AWS ECS/EKS for containerized microservices deployment with multi-AZ resilience.
- **Security & Compliance:** AWS WAF, AWS KMS (Customer Managed Keys), AWS Secrets Manager, and client-side tokenization (Stripe Elements) for PCI-DSS scope reduction.
- **Observability:** OpenTelemetry for centralized distributed tracing and multi-region log aggregation.

## Rationale
This architecture leverages a globally distributed, containerized microservices pattern on AWS to guarantee 99.95% availability and sub-2-second performance for 1 million MAU. Security controls, multi-region data residency strategies, and decoupled third-party integrations ensure full GDPR, CCPA, and PCI-DSS compliance.