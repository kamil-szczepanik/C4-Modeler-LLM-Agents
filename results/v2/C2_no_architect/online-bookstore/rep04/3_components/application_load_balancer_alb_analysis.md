## Overview
The Online Bookstore system provides global e-commerce capabilities for physical and electronic books, supporting catalog browsing, secure checkout, and personalized recommendations for 1M MAU. It utilizes a scalable, multi-region AWS cloud architecture with strict security, GDPR/CCPA compliance, and multi-currency support.

## Key Elements
- **Book Buyer & Site Administrator**: End-users interacting with the platform.
- **Global CDN & AWS WAF**: Entry point utilizing CloudFront and WAF for traffic verification, rate limiting, and DDoS protection.
- **Application Load Balancer (ALB)**: AWS ALB handling TLS termination, header-based routing, and authentication offloading.
- **Backend Containers**: Amazon ECS on AWS Fargate running Search, Recommendations, Checkout, and Shopping Cart services.
- **Supporting Infrastructure**: Amazon Cognito, Amazon SQS/SNS, AWS Secrets Manager, and AWS KMS.

## Relationships
- Global CDN & AWS WAF -> Application Load Balancer (ALB): Forwards verified traffic [HTTPS]
- Application Load Balancer (ALB) -> Search & Recommendations Containers: Routes requests [HTTP/REST]
- Application Load Balancer (ALB) -> Checkout & Shopping Cart Containers: Routes requests [gRPC]
- Application Load Balancer (ALB) -> Amazon Cognito: Offloads JWT validation [OIDC/OAuth 2.0]
- Application Load Balancer (ALB) -> Backend Containers: Forwards validated claims via injected headers [`X-User-ID`, `X-User-Roles`]

## Technology Stack
- **Cloud Provider**: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region high availability.
- **Compute**: Amazon ECS on AWS Fargate for serverless, scalable container execution.
- **Load Balancing & Security**: AWS ALB with AWS ACM (TLS 1.3), AWS WAF, and AWS Shield Advanced for traffic management and OWASP mitigation.
- **Authentication**: Amazon Cognito for OIDC/OAuth 2.0 identity management.
- **Observability**: Amazon CloudWatch and Amazon S3 for centralized logging, metric alarms, and anomaly detection.

## Rationale
This architecture ensures 99.95% uptime and sub-2-second page loads globally by leveraging edge distribution and auto-scaling Fargate containers. The security and routing configurations at the ALB layer protect revenue-generating checkout flows and enforce strict data protection mandates.