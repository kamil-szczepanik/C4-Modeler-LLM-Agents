## Overview
Real-Time Payment Fraud Screening protects card-not-present authorizations from fraud for a mid-size payment processor. It provides sub-50ms scoring decisions, manual case management, and strict PCI-DSS compliance within a fixed AWS budget.

## Key Elements
- Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
- Case Management System API (Node.js / Express API on ECS)
- Case Management System Frontend (React SPA on S3 + CloudFront)
- Amazon API Gateway
- Amazon DynamoDB
- Amazon SQS / Amazon Kinesis
- Compliance Reporting Worker (AWS Lambda)
- Amazon CloudWatch (Log Groups, Metric Filters, Alarms, Logs Insights, Synthetics)
- AWS KMS and Amazon S3 with Object Lock

## Relationships
- Amazon API Gateway -> Real-Time Scoring Engine: Forwards payment authorization requests [HTTPS]
- Real-Time Scoring Engine -> Amazon DynamoDB: Persists transaction state and audit records [AWS SDK over TLS]
- Real-Time Scoring Engine -> Amazon SQS / Amazon Kinesis: Queues asynchronous review and audit events [AWS SDK over TLS]
- Real-Time Scoring Engine / Case Management API -> Amazon CloudWatch: Emits EMF metrics and redacted logs [AWS SDK over HTTPS]
- CloudWatch Alarm Evaluator -> Amazon SNS: Dispatches operational and business alerts [HTTPS]
- Amazon Kinesis Firehose -> Amazon S3 with Object Lock: Streams logs for 7-year immutable retention [HTTPS]

## Technology Stack
- AWS (eu-west-1): Target cloud provider ensuring managed scalability and compliance features
- Go: Chosen for the scoring engine to meet sub-50ms P99 latency at 3,000 TPS
- React SPA & Node.js/Express: Powers the case management UI and API
- Amazon DynamoDB: Provides low-latency NoSQL data persistence
- Amazon S3 with Object Lock: Enforces tamper-evident 7-year audit retention (R-06)
- Amazon CloudWatch & AWS KMS: Handles observability, EMF metrics, and encrypted log storage under strict IAM controls

## Rationale
This architecture uses serverless and managed AWS services to handle 3,000 TPS under a 25,000 EUR monthly budget. It strictly separates hot operational observability from 7-year immutable storage in S3, ensuring PCI-DSS Level 1 compliance and auditability.