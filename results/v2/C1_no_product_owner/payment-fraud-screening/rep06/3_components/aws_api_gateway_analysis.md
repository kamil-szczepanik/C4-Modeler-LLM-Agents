## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at scale while enabling case management for risk analysts. It ensures PCI-DSS Level 1 compliance and sub-50ms P99 latency within a strict budget and lean engineering team.

## Key Elements
- Payment Gateway / Acquirer
- AWS API Gateway (with mTLS Endpoint Configuration, AWS WAF, Request Validator)
- Go Fraud Scoring Engine (AWS ECS Fargate, gRPC)
- Case Management Backend (AWS ECS Fargate, AWS Cognito)
- Amazon ElastiCache (Redis)
- Amazon Aurora Serverless v2
- AWS Secrets Manager and AWS Certificate Manager (ACM)
- Amazon S3 (with Object Lock)

## Relationships
- Payment Gateway / Acquirer -> AWS API Gateway: Sends payment authorization requests [HTTPS / mTLS]
- AWS API Gateway -> Go Fraud Scoring Engine: Forwards authorization requests for scoring [gRPC over mTLS via AWS VPC Lattice]
- AWS API Gateway -> Amazon S3: Streams access logs for tamper-evident auditing [AWS Internal]
- AWS API Gateway -> AWS WAF: Inspects ingress traffic for rate-limiting and security [AWS Internal]

## Technology Stack
- AWS API Gateway: Ingress layer providing native mTLS authentication, request validation, and WAF protection.
- Go on AWS ECS Fargate: High-performance scoring engine meeting the <50ms latency requirement.
- Amazon Aurora Serverless v2 & ElastiCache (Redis): Scalable persistence and caching for low-latency rule evaluation.
- Terraform: Infrastructure as Code for automated, zero-downtime deployments managed by a 3-engineer team.
- Amazon S3 with Object Lock: Immutably stores access logs to satisfy the 7-year audit retention constraint.

## Rationale
This architecture uses fully managed AWS services to minimize operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 security. Edge mTLS termination, payload sanitization, and high-performance containerized microservices guarantee sub-50ms decision latency within the 25,000 EUR monthly budget.