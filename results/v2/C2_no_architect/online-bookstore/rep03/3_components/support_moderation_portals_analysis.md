## Overview
[The Support/Moderation Portals container provides internal interfaces for customer support agents and content moderators to manage user disputes, reviews, and GDPR/CCPA data requests. It ensures secure, isolated operations while maintaining regulatory compliance across global AWS regions.]

## Key Elements
* Customer Support Agent
* Content Moderator
* Support/Moderation Portals Container (Amazon EKS)
* Internal Application Load Balancer (ALB)
* AWS IAM Identity Center (OIDC/SAML)
* AWS KMS
* AWS Systems Manager Session Manager
* Istio Service Mesh

## Relationships
* Customer Support Agent -> Internal ALB: Accesses portal via HTTPS with Zero-Trust VPN/MFA
* Content Moderator -> Internal ALB: Accesses portal via HTTPS with Zero-Trust VPN/MFA
* Internal ALB -> Support/Moderation Portals: Routes internal staff traffic
* Support/Moderation Portals -> Istio Service Mesh: Enforces mTLS and regional data isolation

## Technology Stack
* Amazon EKS: Provides isolated container deployment for portal services
* AWS IAM Identity Center: Delivers OIDC/SAML authentication and step-up MFA
* Istio: Enforces zero-trust microsegmentation and mTLS communication
* AWS KMS: Handles field-level encryption at rest for PII
* AWS Systems Manager Session Manager: Enables ephemeral, JIT break-glass access

## Rationale
[Strict network isolation and RBAC protect sensitive PII and ensure OWASP Top-10 mitigations. Region-locked data pipelines and immutable audit logging satisfy multi-region GDPR/CCPA constraints without degrading system performance.]