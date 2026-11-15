## Overview
An AWS-hosted online bookstore delivering high-performance catalog browsing and secure checkout for 1M MAU. It features asynchronous microservices, strict security boundaries, and multi-region scalability.

## Key Elements
- Customers and Store Administrators
- React SPA (Frontend & Admin Back-Office)
- AWS API Gateway & AWS CloudFront (WAF protected)
- Catalog & Search Container (Spring Boot / Amazon OpenSearch)
- Order & Checkout Container (Node.js/TypeScript)
- Recommendation & Review Container (Python FastAPI)
- Customer Engagement & Notification Container (Node.js worker)
- Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache (Redis)
- External Systems: Payment Gateway, Third-Party Shipping APIs, AWS Cognito, AWS SQS/SNS

## Relationships
- Customers interact with the React SPA via HTTPS/TLS 1.3 through CloudFront and AWS API Gateway.
- API Gateway routes synchronous traffic to backend containers using REST/JSON over HTTP via VPC links and mTLS.
- Backend containers communicate asynchronously via AWS SQS/SNS for decoupled domain events (Order Placed, Notifications).
- Order & Checkout container integrates securely with external Payment Gateways and Third-Party Shipping APIs.

## Technology Stack
- **Frontend:** React/TypeScript hosted in AWS S3, distributed via CloudFront with WAF.
- **Backend Services:** Spring Boot (Catalog), Node.js/TypeScript (Checkout & Notifications), Python FastAPI (Recommendations).
- **Databases & Caching:** Amazon Aurora PostgreSQL (transactional), Amazon DynamoDB (session/cart), Amazon ElastiCache Redis (catalog caching).
- **Messaging & Integration:** AWS SQS and AWS SNS for asynchronous event-driven decoupling.
- **Security & Infrastructure:** AWS Cognito (OAuth2/OIDC), AWS Secrets Manager, AWS KMS, and AWS App Mesh.

## Rationale
This microservices-based, event-driven architecture on AWS isolates heavy administrative and checkout workloads from customer-facing services to guarantee sub-2-second page loads and 99.95% uptime. Strict network segmentation, IAM roles, and tokenization satisfy GDPR/CCPA compliance and OWASP Top-10 security requirements.