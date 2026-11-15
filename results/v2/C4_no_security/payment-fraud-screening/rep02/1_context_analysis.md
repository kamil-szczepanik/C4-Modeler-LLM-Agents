## Overview
Real-Time Payment Fraud Screening system processes card-not-present authorizations to detect fraud in real-time and provides case management for suspicious transactions. It is designed for mid-size payment processors to balance risk mitigation, sub-50ms latency, and compliance.

## Key Elements
- **Payment Gateway / Core Processing System:** External system sending real-time authorization requests.
- **Fraud Analyst & Merchant Support:** Internal users reviewing flagged cases and handling disputes.
- **Data Scientist / Fraud Modeler & Risk Manager:** Internal users updating rules, models, and auditing decisions.
- **API Gateway & AWS Lambda:** Compute containers executing stateless scoring logic.
- **Amazon DynamoDB & ElastiCache (Redis):** Data containers for low-latency feature stores and transaction state.
- **Amazon SQS & Amazon EventBridge:** Containers for asynchronous event routing and case management.
- **Amazon S3 Object Lock:** Tamper-evident storage container for 7-year audit trails.

## Relationships
- **Payment Gateway to API Gateway:** Sends real-time authorization requests via gRPC/REST over TLS.
- **API Gateway to AWS Lambda:** Invokes scoring functions synchronously.
- **AWS Lambda to DynamoDB & Redis:** Queries features and stores evaluation results via TCP.
- **AWS Lambda to Amazon SQS:** Publishes review cases asynchronously.
- **Users to Web Portals:** Accesses case management, rule updates, and audit logs via HTTPS/TLS.

## Technology Stack
- **AWS Lambda / AWS Fargate:** Stateless compute ensuring rapid scaling within budget.
- **Amazon DynamoDB / ElastiCache (Redis):** Sub-10ms data stores for low-latency feature access.
- **Amazon SQS / EventBridge:** Managed messaging for reliable asynchronous case routing.
- **Amazon S3 Object Lock (Compliance Mode):** Immutable storage guaranteeing tamper-evident 7-year audit logs.
- **AWS X-Ray & Amazon CloudWatch:** Observability tools for distributed tracing and latency tracking.

## Rationale
Fully managed serverless AWS services minimize operational overhead for a three-engineer team while easily handling 3,000 TPS under a 25,000 EUR monthly budget. Strict isolation of management planes and use of low-latency data stores ensure P99 latency remains below 50ms while satisfying PCI-DSS Level 1 and 7-year audit requirements.