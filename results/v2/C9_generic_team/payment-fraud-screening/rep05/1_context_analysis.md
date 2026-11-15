## Overview
The system screens card-not-present payment authorizations for fraud in real-time while providing case management for suspicious payments. It is operated by a three-engineer team on AWS within a strict monthly budget and PCI-DSS Level 1 constraints.

## Key Elements
* Payment Gateway / Acquirer
* Fraud Analysts
* Cardholder / Merchant
* Fraud Screening Engine (AWS Fargate / Lambda)
* Case Management System
* Content-Addressable Model Registry (Amazon S3)
* Audit Trail Store (Amazon DynamoDB & S3 Glacier Vault Lock)
* Fallback Proxy

## Relationships
* Payment Gateway invokes Fraud Screening Engine via HTTPS REST API with strict 30ms timeout.
* Fraud Analysts access Case Management System via HTTPS.
* Fraud Screening Engine retrieves model weights from Amazon S3 via internal AWS network.
* Fraud Screening Engine writes tamper-evident audit logs to Amazon DynamoDB, transitioning to S3 Glacier Vault Lock.

## Technology Stack
* AWS Fargate / Lambda: Stateless scoring to ensure high throughput and meet P99 <50ms latency.
* Amazon S3: Content-addressable model registry storing immutable cryptographic hashes for zero-downtime updates.
* Amazon DynamoDB and S3 Glacier Vault Lock: Tiered audit storage ensuring 7-year tamper-evident compliance within budget.
* AWS API Gateway: Native request timeouts and canary deployments for fail-open resilience.

## Rationale
Serverless and managed AWS services eliminate infrastructure maintenance overhead, fitting the three-engineer team and €25k/month budget constraints. Immutable storage patterns and isolated VPC subnets guarantee strict PCI-DSS compliance and verifiable 7-year auditability.