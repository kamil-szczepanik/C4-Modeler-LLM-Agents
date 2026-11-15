## Overview
The Online Bookstore is a multi-region e-commerce platform built to support scalable book discovery, secure multi-currency checkout, and strict regulatory compliance. It delivers resilient, low-latency performance for global users while isolating critical transactional workflows from high-traffic browsing.

## Key Elements
- Book Buyer & Site Administrator (Users)
- Global CDN & AWS WAF
- Application Load Balancer (ALB)
- Amazon ECS on AWS Fargate (Containers: Search, Recommendations, Checkout, Shopping Cart)
- Amazon Cognito (Authentication/OIDC)
- Amazon SQS/SNS with Dead-Letter Queues (DLQs)
- AWS Secrets Manager & AWS KMS
- External Payment Gateways, Shipping Providers, and Book Publishers

## Relationships
- Users to Global CDN/WAF via HTTPS
- ALB to ECS Fargate Containers via HTTP/REST and gRPC
- Inter-container communication (east-west) via mTLS
- Containers to AWS Secrets Manager via HTTPS for runtime credentials
- Checkout Container to External Payment/Shipping APIs via HTTPS with circuit breakers
- Event publishers to SQS/SNS via encrypted AWS KMS channels

## Technology Stack
- **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region availability
- **Compute:** Amazon ECS on AWS Fargate for isolated, scalable container workloads
- **Security & Compliance:** AWS WAF, AWS KMS, AWS Secrets Manager, and Amazon Inspector for OWASP Top-10 and GDPR/CCPA compliance
- **Identity:** Amazon Cognito (OAuth 2.0 / OIDC) for session management
- **Resilience:** Amazon SQS/SNS with Dead-Letter Queues (DLQs) for asynchronous event handling

## Rationale
This architecture isolates high-traffic discovery from the transactional core using the bulkhead pattern, ensuring payment availability during traffic spikes. Multi-region Fargate deployment with strict mTLS, KMS encryption, and circuit breakers guarantees 99.95% uptime, OWASP mitigation, and seamless global scalability.