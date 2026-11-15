## Overview
The Online Bookstore is a globally distributed, scalable e-commerce platform providing physical and electronic book sales, search, recommendations, and reviews. It ensures high availability, strict security compliance, and multi-region resilience for 1M MAU.

## Key Elements
- Book Buyer (Person)
- Site Administrator (Person)
- AWS WAF & Amazon CloudFront (Global CDN / WAF)
- AWS Application Load Balancer (ALB)
- Amazon ECS on AWS Fargate (Containers: Search, Recommendations, Checkout, Shopping Cart)
- Amazon Cognito (Identity Management / OIDC / OAuth 2.0)
- Amazon SQS / SNS (Asynchronous Messaging)
- AWS Secrets Manager & AWS KMS (Secrets & Encryption Management)

## Relationships
- Book Buyer -> Global CDN & AWS WAF: Browses catalogue and executes secure checkout [HTTPS]
- Global CDN & AWS WAF -> Application Load Balancer: Forwards routed traffic [HTTPS]
- Application Load Balancer -> Amazon ECS Fargate Containers: Distributes incoming requests [HTTP/HTTPS]
- Checkout Container -> Payment Gateway & Shipping Provider API: Processes transactions and logistics [HTTPS / REST]
- Search & Checkout Containers -> AWS Secrets Manager & AWS KMS: Retrieves runtime credentials and decryption keys [HTTPS via AWS PrivateLink]

## Technology Stack
- AWS Fargate & ECS: Container orchestration for microservices scalability without server management
- AWS Secrets Manager & KMS: Secure credential storage and envelope encryption with multi-region keys for GDPR/CCPA compliance
- Amazon Cognito: OIDC/OAuth 2.0 user authentication supporting 1M MAU
- AWS PrivateLink (VPC Endpoints): Secure internal service communication isolating traffic from the public internet

## Rationale
This multi-region AWS architecture ensures 99.95% uptime and sub-2-second page loads across three global regions while meeting GDPR and CCPA security constraints. Utilizing managed serverless containers and secure secrets management minimizes operational overhead while safeguarding sensitive customer data.