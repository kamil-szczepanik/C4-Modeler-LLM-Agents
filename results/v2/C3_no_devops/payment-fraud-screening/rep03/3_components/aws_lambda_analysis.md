## Overview
- Real-time payment fraud screening system for a mid-size payment processor evaluating card-not-present authorizations.
- Provides sub-50ms fraud scoring, automated case management, and tamper-evident 7-year auditability under PCI-DSS Level 1.

## Key Elements
- **Users**: Fraud Analysts, Risk & Compliance Officers, Fraud Engineers.
- **External Systems**: Payment Processor Systems / Payment Gateway, Identity Provider (IdP), Notification Service, Audit Ledger.
- **Containers**: AWS API Gateway / ALB, Scoring Engine (Rust, AWS ECS Fargate), Case Management App (Node.js/Python + React, AWS ECS Fargate), Model & Rule Management Service (AWS ECS Fargate), Amazon Aurora PostgreSQL, Amazon SQS, AWS Lambda.
- **AWS Lambda Components**: Event Consumer Component, Crypto Signer Component, Ledger Writer Component, Error Handling & DLQ Component.

## Relationships
- **Payment Gateway -> AWS API Gateway / ALB**: Submits real-time authorization requests via HTTPS/TLS 1.3.
- **Scoring Engine -> Amazon SQS**: Asynchronously queues audit payloads using AWS SDK.
- **Amazon SQS -> AWS Lambda**: Triggers audit event processing via Event Source Mapping.
- **AWS Lambda -> AWS KMS**: Requests cryptographic signatures (`kms:Sign`) using IAM least-privilege.
- **AWS Lambda -> Audit Ledger**: Writes cryptographically signed audit logs via HTTPS/TLS 1.3.
- **AWS Lambda -> Amazon SQS (DLQ)**: Forwards unprocessable poison messages using encrypted queues.
- **AWS Lambda -> Amazon CloudWatch & SNS**: Emits operational metrics, redacted logs, and alerts.

## Technology Stack
- **AWS Lambda**: Serverless compute for asynchronous audit signing, respecting the 25,000 EUR/month budget.
- **Amazon SQS**: Asynchronous decoupling layer to protect the critical <50ms scoring path from logging bottlenecks.
- **AWS KMS**: Cryptographic key management for signing audit records and encrypting DLQs to meet R-06 and PCI-DSS Level 1.
- **AWS Encryption SDK**: Payload-level encryption ensuring no cleartext PAN data touches Lambda memory or logs.
- **Amazon CloudWatch & SNS**: Automated monitoring and alerting enabling a 3-engineer team to maintain operational awareness.

## Rationale
- Decouples non-critical asynchronous audit logging from synchronous authorization paths to strictly satisfy the P99 <50ms performance requirement.
- Implements robust serverless components and managed AWS services to maintain PCI-DSS Level 1 compliance within fixed budget and team constraints.