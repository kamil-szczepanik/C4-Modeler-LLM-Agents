## Overview
[System: Online Bookstore] Provides an e-commerce platform for purchasing books with secure checkout, recommendations, and reviews.

## Key Elements
* Secrets Engine Component (AWS Secrets Manager)
* Key Management Component (AWS Key Management Service / KMS)
* IAM Policy Enforcement Component (AWS IAM & Resource-Based Policies)
* VPC Endpoint Integration Component (AWS PrivateLink / Interface VPC Endpoints)
* Core E-Commerce Service (Node.js, TypeScript, AWS ECS Fargate)

## Relationships
* Core E-Commerce Service -> VPC Endpoint Integration Component: Routes API calls internally [AWS PrivateLink / TLS 1.3]
* VPC Endpoint Integration Component -> Secrets Engine Component & Key Management Component: Forwards requests securely [AWS internal network]
* Core E-Commerce Service -> Secrets Engine Component: Fetches runtime DB credentials [HTTPS/TLS via AWS SDK]
* Core E-Commerce Service -> Key Management Component: Encrypts/decrypts sensitive customer PII fields [AWS KMS API / TLS]

## Technology Stack
* AWS Secrets Manager: Manages automated database credential rotation and API keys.
* AWS Key Management Service (KMS): Provides Customer Managed Keys (CMKs) for envelope encryption of PII at rest.
* AWS PrivateLink: Secures internal communication without public internet exposure.
* AWS SDK Client-Side Caching: Mitigates KMS/Secrets Manager TPS throttling under peak load.

## Rationale
[Architecture fits the requirements by utilizing AWS PrivateLink and multi-region KMS replicas to guarantee 99.95% uptime and low-latency security operations. Strict IAM policies and CMK encryption ensure full GDPR and CCPA compliance for sensitive user data.]