## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management for fraud analysts.]

## Key Elements
- Fraud Analyst & Risk Manager (Users)
- Payment Gateway / Acquirer, Payment Network / Card Brands (External Systems)
- AWS API Gateway (Ingress/TLS Termination)
- Go Scoring Engine (AWS ECS on Fargate)
- Node.js Case Management (AWS ECS on Fargate)
- Amazon SQS / EventBridge
- Amazon Aurora PostgreSQL Serverless v2
- AWS QLDB (Amazon QLDB) with Ledger Core, Audit Ingestion Service (AWS Lambda), and Verification & Export Worker (AWS Lambda)
- AWS Cognito & AWS Secrets Manager

## Relationships
- Payment Gateway -> AWS API Gateway: Submits payment authorization requests [HTTPS / TLS 1.3]
- Go Scoring Engine -> Amazon Aurora PostgreSQL Serverless v2: Reads/writes fraud rules and scoring data [PostgreSQL Wire Protocol / TLS]
- Go Scoring Engine -> Amazon SQS / EventBridge: Publishes scoring decisions and audit payloads [AWS SDK / HTTPS]
- Amazon SQS / EventBridge -> Audit Ingestion Service (AWS Lambda): Consumes audit payloads asynchronously [AWS SDK / SQS Polling]
- Audit Ingestion Service (AWS Lambda) -> AWS QLDB: Writes tamper-evident audit logs using PartQL [AWS SDK / HTTPS]
- Verification & Export Worker (AWS Lambda) -> AWS QLDB: Executes cryptographic digest verifications [AWS SDK / HTTPS]
- Verification & Export Worker (AWS Lambda) -> Amazon S3: Exports periodic cryptographic proofs [AWS SDK / HTTPS]

## Technology Stack
- AWS ECS on Fargate: Runs containerized Go and Node.js microservices without cluster management overhead.
- Amazon Aurora PostgreSQL Serverless v2: Provides auto-scaling relational storage for rules and case management within budget.
- AWS QLDB: Delivers native cryptographic immutability and tamper-evident audit trails for PCI-DSS compliance.
- AWS Lambda (Python): Implements asynchronous audit ingestion and verification workers to minimize operational burden.
- AWS KMS: Secures ledger data at rest using Customer Managed Keys (CMK) with automated annual rotation.

## Rationale
- The architecture meets the sub-50ms P99 latency and high-throughput requirements by decoupling real-time scoring from asynchronous audit logging via Amazon SQS. It satisfies strict 7-year PCI-DSS compliance and auditability mandates using native AWS QLDB cryptographic verification without custom application overhead.