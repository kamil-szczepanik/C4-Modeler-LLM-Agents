## Overview
This architecture defines a real-time payment fraud screening system for processing card-not-present authorizations securely. It provides automated scoring, case management for analysts, and tamper-evident auditing within strict budget and compliance limits.

## Key Elements
- Fraud Analysts & Risk/Compliance Officers (Users)
- Payment Gateway / Merchants & Card Tokenization Vault (External Systems)
- Real-Time Scoring Engine & Case Management App (Containers on ECS Fargate)
- Feature Store & Cache (Amazon ElastiCache Redis) & Database (Amazon Aurora PostgreSQL)
- Network & Security (AWS WAF, Amazon API Gateway, AWS KMS, AWS Secrets Manager)

## Relationships
- Payment Gateways to API Gateway via HTTPS/TLS 1.3
- API Gateway to ECS Fargate tasks via VPC Links using internal HTTPS
- ECS Fargate to Amazon Aurora PostgreSQL and ElastiCache Redis via TCP/TLS
- Secrets Manager and KMS to ECS Fargate via AWS IAM

## Technology Stack
- Amazon API Gateway & AWS WAF: Edge routing and request filtering for high-throughput traffic
- AWS KMS & AWS Secrets Manager: Encryption, key segregation, and automated credential rotation for PCI-DSS compliance
- AWS VPC Security Groups: Micro-segmentation ensuring strict network isolation
- Amazon ECS Fargate: Serverless container orchestration aligned with a 3-engineer team constraint

## Rationale
Managed AWS services minimize operational toil for a small three-engineer team while keeping infrastructure costs well within the 25,000 EUR monthly budget. Enforcing strict network isolation, encryption in transit, and KMS key segregation satisfies PCI-DSS Level 1 compliance and 7-year audit requirements without exceeding the 50 ms P99 latency threshold.