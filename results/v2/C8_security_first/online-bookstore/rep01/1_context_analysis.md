## Overview
The Online Bookstore is a globally scaled e-commerce platform built on AWS to provide book purchasing, recommendations, and reviews. Its core purpose is to deliver a secure, multi-currency retail experience supporting 1 million monthly active users across multiple regions.

## Key Elements
- **People:** Customer, Book Author / Publisher, Customer Support Agent, Shipping Partner, Site Administrator / Content Manager.
- **Systems:** Online Bookstore (System-of-Interest).
- **External Systems:** Payment Gateway, Shipping Provider APIs, Notification Service, Currency Exchange API.
- **Containers/Infrastructure:** AWS Route 53, AWS WAF, AWS API Gateway, AWS Secrets Manager, AWS KMS, AWS ElastiCache (Redis).

## Relationships
- **Customer -> Online Bookstore:** HTTPS (TLS 1.3) with OAuth 2.0/OIDC and MFA for browsing, search, and checkout.
- **Site Administrator -> Online Bookstore:** HTTPS (TLS 1.3) restricted via RBAC and AWS IAM.
- **Online Bookstore -> Payment Gateway:** HTTPS/REST for tokenized transactions.
- **Online Bookstore -> Shipping Provider APIs:** HTTPS/REST for automated fulfillment.
- **Online Bookstore -> Notification Service:** HTTPS/SMTP for transactional emails.
- **Online Bookstore -> Currency Exchange API:** HTTPS/REST for multi-currency conversion.

## Technology Stack
- **Cloud Provider:** AWS (us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability.
- **Security & Compliance:** AWS WAF, AWS API Gateway, AWS Secrets Manager, and AWS KMS (AES-256 encryption at rest, TLS 1.3 in transit) for GDPR/CCPA and OWASP Top-10 mitigation.
- **Networking & Resilience:** AWS Route 53 (latency-based routing, DNS failover), AWS ElastiCache (Redis) for local caching, and circuit breakers for high availability (99.95% uptime).

## Rationale
This architecture uses AWS multi-region active deployments with edge routing to achieve sub-2-second performance and 99.95% uptime for 1M MAU. Offloading PCI-DSS scope to tokenized payment gateways and enforcing regional data residency controls ensures strict GDPR/CCPA compliance.