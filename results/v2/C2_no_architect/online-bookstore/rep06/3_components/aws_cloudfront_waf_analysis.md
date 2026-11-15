## Overview
Global e-commerce platform for purchasing physical and electronic books with recommendations and reviews. Serves 1 million monthly active users globally with multi-currency support and strict regulatory compliance.

## Key Elements
- Book Buyer, Store Administrator, Author/Publisher Partner (Users)
- AWS CloudFront & WAF (Edge Caching, CDN, and Security)
- Catalog & Search, Personalization Engine, Checkout/Payment, Localization/Currency, Notification Containers (Amazon ECS/EKS)
- Third-Party Payment Gateways and Shipping APIs (External Systems)

## Relationships
- Book Buyer & Partners -> AWS CloudFront & WAF: Accesses platform securely [HTTPS (TLS 1.3)]
- AWS CloudFront & WAF -> Catalog & Search, Personalization, Checkout, Localization: Routes requests [HTTPS / mTLS over AWS App Mesh]
- AWS CloudFront & WAF -> Amazon S3: Origin failover and static asset retrieval [AWS IAM Origin Access Control]

## Technology Stack
- AWS CloudFront & WAF: Global CDN and edge security with AWS WAF Bot Control and Shield Advanced for DDoS mitigation.
- Amazon ECS/EKS: Container orchestration for core microservices across multi-regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
- Terraform/CDK: Infrastructure-as-Code for consistent multi-region deployments and automated provisioning.
- AWS Certificate Manager (ACM): TLS 1.3 termination at edge with strict mTLS for backend communication.

## Rationale
Multi-region AWS deployment with edge caching guarantees sub-2-second page loads on 3G networks globally. Comprehensive edge security controls and strict IAM policies fulfill GDPR/CCPA compliance and OWASP Top-10 requirements while maintaining 99.95% uptime.