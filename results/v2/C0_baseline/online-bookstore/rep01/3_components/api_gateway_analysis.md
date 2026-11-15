## Overview
The Online Bookstore system is an Amazon-style e-commerce platform providing catalog browsing, secure checkout, reviews, and recommendations for 1 million monthly active users. It delivers high scalability, security, and global availability across AWS regions.

## Key Elements
- **Users**: Book Buyer, Site Administrator, Customer Support Representative, Third-Party Content Provider/Publisher
- **External Systems**: Payment Gateway, Third-Party Shipping API, Tax Calculation Service, Marketing/Email Service Provider
- **Containers**: Managed AWS API Gateway / Envoy Edge, Single Page Application (React on AWS S3/CloudFront), Catalog & Search Container, Order & Checkout Container, Recommendation Container, Localization Container, Analytics & Event Ingestion Container
- **API Gateway Components**: Edge Router & TLS Termination, Auth & Token Validator, Request Transformer, Traffic Policy & Throttling Component, Internal Routing & mTLS Dispatcher, Service Mesh Proxy

## Relationships
- **Book Buyer / Publisher -> AWS API Gateway**: Sends HTTPS traffic with JWT validation, OAuth 2.0 credentials, and rate-limiting [HTTPS, TLS 1.3]
- **AWS Route 53 -> AWS API Gateway**: Routes global latency-based traffic across us-east-1, eu-west-1, and ap-southeast-1 [DNS]
- **AWS API Gateway -> Backend Containers**: Dispatches internal requests securely [gRPC over mTLS via AWS App Mesh]
- **API Gateway -> Amazon CloudWatch & AWS X-Ray**: Centralizes access logs, telemetry, and tracing [AWS APIs]

## Technology Stack
- **Edge Routing & Ingress**: AWS API Gateway / Envoy-managed ingress, AWS Route 53, AWS WAF (Offloads TLS termination and OWASP Top-10 mitigations for R-07 and R-08)
- **Frontend**: React hosted on AWS S3 and distributed via CloudFront (Ensures <2s page load on 3G per R-06)
- **Backend & Services**: Node.js/Express, Spring Boot, Python/FastAPI, Go (Supports multi-domain retail business logic)
- **Data & Search**: Amazon OpenSearch, PostgreSQL (Provides high-performance catalog search and ACID transactions)
- **Messaging & Streaming**: Amazon Kinesis Firehose, Amazon SQS/SNS (Handles event ingestion and telemetry)
- **Security & Infrastructure**: AWS App Mesh, Amazon Cognito, AWS Secrets Manager, Terraform/CDK (Enforces mTLS, OAuth 2.0, and multi-region IaC consistency)

## Rationale
This architecture leverages managed AWS services like AWS API Gateway, WAF, and App Mesh to meet the 99.95% availability (R-07) and 1M MAU scalability (R-05) requirements without operational bloat. Edge-based security controls, JSON schema validation, and multi-region deployment ensure strict GDPR/CCPA compliance and OWASP mitigation (R-08).