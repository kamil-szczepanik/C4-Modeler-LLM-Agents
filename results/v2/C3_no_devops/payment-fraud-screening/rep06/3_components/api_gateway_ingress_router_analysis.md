## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations to prevent fraud and provides a case management interface for fraud analysts. It operates on AWS within a strict PCI-DSS Level 1 compliance framework and a 25,000 EUR monthly budget.

## Key Elements
- Payment Ingress Router (AWS Application Load Balancer)
- Management API Gateway (Amazon API Gateway)
- Scoring Engine (AWS ECS Fargate)
- Case Management API (AWS ECS Fargate)
- Fraud Analyst SPA (Amazon S3 and Amazon CloudFront)
- Audit & Persistence Store (Amazon Aurora PostgreSQL)
- Feature Store (Amazon ElastiCache Redis)
- Asynchronous Event Bus (Amazon EventBridge and Amazon MSK Lite)

## Relationships
- Payment Gateway -> Payment Ingress Router: Processing authorization requests via HTTPS/gRPC over TLS 1.3 and mTLS
- Fraud Analyst -> Management API Gateway: Accessing analyst sessions via HTTPS over TLS 1.3 with JWT authentication
- Payment Ingress Router -> Scoring Engine: Forwarding payload requests via gRPC over mTLS within private subnets via VPC Endpoints
- Management API Gateway -> Case Management API: Routing case management operations via HTTPS over mTLS

## Technology Stack
- AWS Application Load Balancer: Chosen for the payment ingress to handle high-throughput B2B traffic cost-effectively under the 25,000 EUR/month budget.
- Amazon API Gateway: Selected for management traffic to provide built-in AWS Cognito JWT validation and AWS WAF integration.
- AWS ECS Fargate: Utilized for containerized microservices to minimize operational overhead for a three-engineer team.
- Amazon Aurora PostgreSQL: Deployed for the tamper-evident audit store to meet the 7-year retention and compliance requirements.
- Amazon ElastiCache Redis: Implemented as a feature store to guarantee sub-50ms P99 scoring latency.

## Rationale
The architecture separates high-frequency payment routing from human analyst traffic to isolate workloads and guarantee sub-50ms P99 latency. Leveraging managed AWS services maximizes reliability and security within the constraints of a three-engineer team and a fixed infrastructure budget.