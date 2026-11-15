## Overview
[The system is an Amazon-style online bookstore platform designed to process book purchases, reviews, and recommendations for 1 million monthly active users globally. Its core purpose is to provide a highly available, secure, and compliant e-commerce experience across multiple regions and currencies.]

## Key Elements
- Book Buyer, Book Reviewer, Store Administrator, Support Agent
- AWS API Gateway (with TLS 1.3 edge termination, AWS WAF, and AWS Route 53)
- Cart & Checkout Container, Catalog & Search Container, Personalization Engine Container, Localization & Compliance Container, Admin & Support Container (Amazon ECS/EKS)
- AWS Aurora Database, Amazon ElastiCache, Amazon SQS
- Third-Party Payment Gateway, Third-Party Shipping APIs

## Relationships
- Book Buyer -> AWS API Gateway: Browses catalog, manages cart, and completes checkout [HTTPS (TLS 1.3)]
- Book Reviewer -> AWS API Gateway: Submits and manages reviews [HTTPS (TLS 1.3)]
- Store Administrator -> AWS API Gateway: Manages store operations [HTTPS (TLS 1.3)]
- Support Agent -> AWS API Gateway: Handles customer support inquiries [HTTPS (TLS 1.3)]
- AWS API Gateway -> ECS/EKS Containers: Routes validated traffic [mTLS inside AWS VPC]

## Technology Stack
- AWS API Gateway: Manages secure edge routing, rate limiting, and JWT/OAuth2 validation
- AWS WAF & Route 53: Provides OWASP Top-10 mitigation, edge security, and latency-based multi-region routing
- Amazon ECS/EKS: Hosts microservice containers across `us-east-1`, `eu-west-1`, and `ap-southeast-1`
- AWS Aurora & ElastiCache: Handles transactional persistence and caching for sub-2-second performance
- Amazon CloudWatch & AWS X-Ray: Delivers centralized access logging and distributed tracing for GDPR/CCPA compliance

## Rationale
[This architecture utilizes globally distributed AWS infrastructure and a managed API Gateway to guarantee 99.95% uptime and sub-2-second latency for 1M MAU. Built-in WAF, JWT authorization, and PII masking ensure strict GDPR/CCPA compliance and OWASP mitigation.]