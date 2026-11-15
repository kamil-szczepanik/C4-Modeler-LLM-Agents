## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud under strict latency and compliance constraints. It evaluates transactions in real-time and provides a case management interface for fraud analysts.

## Key Elements
- External Payment Gateway and Fraud Analysts (Users/Systems)
- AWS API Gateway with ingress schema validation (Container)
- AWS ECS on Fargate stateless scoring engine (Container)
- Amazon Aurora Serverless case management database (Container)
- Amazon S3 with Object Lock and Glacier Vault Lock audit store (Container)
- AWS SNS and PagerDuty alerting (Container)

## Relationships
- Payment Gateway to AWS API Gateway via HTTPS/HTTP/2 using gRPC/JSON payloads
- ECS Fargate to Amazon Aurora Serverless via TLS for case management data
- Scoring Engine to Amazon S3 via HTTPS for local model artifact loading
- System to Amazon S3 via AWS SDK for tamper-evident cryptographic audit logs
- System to PagerDuty via AWS SNS for operational alerts

## Technology Stack
- AWS ECS on Fargate: chosen for stateless scaling and low operational overhead
- Amazon Aurora Serverless: selected for elastic relational case management storage
- Amazon S3 with Object Lock and Glacier: provides cost-effective, tamper-evident 7-year audit retention
- AWS API Gateway: handles ingress validation, rate limiting, and circuit breaking
- Terraform and AWS Config: automates Infrastructure as Code and policy-as-code compliance

## Rationale
This architecture uses vertically scalable managed services to easily achieve sub-50ms P99 latency at 3,000 TPS within a €25k monthly budget. It minimizes operational toil for a three-engineer team while satisfying rigorous PCI-DSS Level 1 and 7-year auditability constraints.