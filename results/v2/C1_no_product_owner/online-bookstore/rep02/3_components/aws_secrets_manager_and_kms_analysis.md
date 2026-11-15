## Overview
The Online Bookstore system is a scalable e-commerce platform built on AWS, designed to support 1 million MAU with high availability and stringent GDPR/CCPA compliance. It utilizes a containerized microservices architecture to handle product catalogs, secure checkout, and personalized recommendations.

## Key Elements
- **Secrets Engine Component**: AWS Secrets Manager managing dynamic database credentials and third-party API keys.
- **Key Management Component**: AWS Key Management Service (KMS) with FIPS 140-2 Level 3 hardware security modules.
- **Secrets Caching Wrapper**: AWS Secrets Manager Caching Library embedded in ECS Fargate services.
- **KMS Crypto Client**: AWS Encryption SDK handling client-side envelope encryption and local data key caching.
- **Microservices**: Order & Checkout Service and Catalog Service running on Amazon ECS Fargate.

## Relationships
- *Order & Checkout Service* and *Catalog Service* invoke *Secrets Engine Component* via AWS SDK (HTTPS) through the *Secrets Caching Wrapper*.
- *All Microservices* invoke *Key Management Component* via AWS SDK (HTTPS) using the *KMS Crypto Client*.
- *Secrets Engine Component* performs automatic secret rotation via AWS Lambda over HTTPS/TLS 1.3.

## Technology Stack
- **AWS Secrets Manager**: Manages dynamic credentials and third-party API keys with automatic rotation.
- **AWS Key Management Service (KMS)**: Secures Customer Master Keys (CMKs) for data encryption.
- **AWS Secrets Manager Caching Library**: Provides local in-memory credential caching to prevent API throttling.
- **AWS Encryption SDK**: Enables client-side envelope encryption and local data key caching.
- **Terraform / AWS CDK**: Automates Infrastructure-as-Code provisioning.

## Rationale
This architecture ensures 99.95% availability by eliminating runtime throttling bottlenecks through aggressive local caching wrappers. It meets strict GDPR/CCPA and OWASP security constraints via least-privilege IAM boundaries, TLS 1.3 encryption, and customer-managed KMS key policies.