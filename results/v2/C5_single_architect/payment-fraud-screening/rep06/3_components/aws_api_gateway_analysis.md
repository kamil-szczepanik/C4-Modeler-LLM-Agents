## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real-time and provides case management for fraud analysts. It ensures PCI-DSS Level 1 compliance, tamper-evident 7-year auditability, and sub-50ms P99 latency.

## Key Elements
- Payment Gateway / Acquirer Systems (External)
- Fraud Analysts (User)
- AWS API Gateway (REST) with native Request Validator, Authorizer, and HTTP Proxy Integration
- Scoring Engine (Go on AWS ECS Fargate)
- Case Management Backend (Node.js/Go on AWS ECS Fargate)
- Amazon DynamoDB and Amazon Aurora PostgreSQL
- Amazon S3 Object Lock & Amazon Kinesis Data Firehose

## Relationships
- Payment Gateway -> AWS API Gateway: Submits auth requests [HTTPS/JSON, mTLS]
- AWS API Gateway -> Scoring Engine: Routes requests for real-time scoring [Internal HTTP/REST over VPC Link]
- Scoring Engine -> Amazon DynamoDB: Queries rules and stores operational state [Internal AWS SDK]
- Case Management Backend -> Amazon Aurora PostgreSQL: Stores case data and analyst reviews [Internal TLS]
- System -> Amazon S3 Object Lock: Archives tamper-evident decision logs for 7 years [AWS SDK]

## Technology Stack
- AWS API Gateway (REST): Edge routing, JSON schema validation, and mTLS authorization for low latency
- Go & Node.js: High-performance backend services on AWS ECS Fargate
- Amazon DynamoDB & Aurora PostgreSQL: Low-latency NoSQL and relational data storage
- Amazon S3 with Object Lock: Tamper-evident 7-year audit retention
- AWS (eu-west-1): Cloud infrastructure complying with PCI-DSS Level 1

## Rationale
This architecture uses serverless and managed AWS services to meet the strict 50ms P99 latency constraint while staying within a 25,000 EUR monthly budget for a 3-engineer team. Native edge validation and VPC routing ensure high security and PCI-DSS compliance without adding infrastructure overhead.