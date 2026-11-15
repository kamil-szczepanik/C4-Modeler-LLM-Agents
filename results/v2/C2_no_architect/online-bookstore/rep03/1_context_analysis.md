## Overview
[An Amazon-style global e-commerce platform for purchasing physical and electronic books, supporting multi-currency transactions, personalized recommendations, and reviews. Designed for high availability, strict data sovereignty compliance, and global performance.]

## Key Elements
* Customer (Shopper)
* Site Administrator
* Warehouse / Fulfillment Partner
* AWS CloudFront (CDN with Lambda@Edge)
* AWS ECS / EKS (Microservices container platform)
* AWS KMS (Key Management Service)
* Third-Party Shipping & Payment APIs

## Relationships
* Customer interacts via HTTPS (TLS 1.3) through AWS CloudFront and AWS WAF
* Microservices communicate via mTLS across `us-east-1`, `eu-west-1`, and `ap-southeast-1`
* Checkout service connects asynchronously via encrypted AWS queues to third-party shipping APIs
* Administrators access internal workflows via RBAC and MFA-secured endpoints

## Technology Stack
* AWS CloudFront & Lambda@Edge for global edge caching and performance (<2s load)
* Terraform for immutable infrastructure deployment across multi-region AWS ECS/EKS
* OAuth 2.0 / OIDC with centralized IAM for authentication and authorization
* AWS KMS with regional keys for data-at-rest encryption and GDPR/CCPA compliance

## Rationale
[This distributed AWS architecture guarantees 99.95% uptime and low latency for 1M MAU via edge caching and multi-region deployment. Asynchronous decoupling and strict security controls ensure regulatory compliance, data protection, and resilience against third-party API failures.]