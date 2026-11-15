## Overview
Real-time payment fraud screening system for card-not-present authorizations, providing low-latency fraud decisions, case management, and tamper-evident auditing. Operated by a three-engineer team within AWS (eu-west-1) under a strict 25,000 EUR monthly budget.

## Key Elements
- **AWS MSK Serverless**: Managed event streaming platform handling real-time data ingestion and distribution.
- **`payment-authorizations-in`**: Kafka topic receiving incoming payment events for parallel scoring.
- **`fraud-decisions-out`**: Kafka topic publishing scored outcomes back to edge services.
- **`fraud-decisions-audit`**: Kafka topic streaming transaction records for compliance and auditing.
- **Go Audit Consumer**: Lightweight service streaming audit events from MSK to long-term storage.
- **Amazon S3 with Object Lock**: Secure, tamper-evident object storage for 7-year audit retention.

## Relationships
- **Scoring Engine (Go)** *produces/consumes via* -> **MSK Topics** (Kafka Protocol over TLS 1.3 with SASL/SCRAM authentication)
- **Go Audit Consumer** *consumes via* -> **`fraud-decisions-audit`** (Kafka Protocol)
- **Go Audit Consumer** *writes to* -> **Amazon S3** (HTTPS / AWS SDK)

## Technology Stack
- **AWS MSK Serverless**: Chosen to eliminate operational overhead for a three-engineer team while scaling for 3,000 TPS.
- **Apache Kafka Protocol (TLS 1.3, SASL/SCRAM)**: Ensures secure, encrypted, and authenticated event streaming.
- **Amazon S3 with Object Lock (Compliance Mode)**: Provides tamper-evident, cost-effective 7-year audit storage without inflating Kafka broker costs.
- **AWS KMS**: Utilized with Customer Managed Keys (CMK) for encryption at rest across MSK and S3.

## Rationale
This architecture uses serverless streaming and automated managed services to minimize operational complexity for a small engineering team while strictly enforcing PCI-DSS compliance, 7-year tamper-evident auditability, and sub-50ms P99 latency. Offloading long-term audit data from Kafka to S3 protects the fixed monthly infrastructure budget.