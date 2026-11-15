## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in the AWS eu-west-1 region. It provides real-time fraud scoring, case management, and compliant 7-year audit logging within a 25,000 EUR monthly budget.

## Key Elements
- Stream Ingestion: Amazon Kinesis Data Firehose
- Secure Vault: Amazon S3 with Object Lock in Compliance Mode
- Key Governance: AWS KMS
- Replication: S3 Cross-Region Replication (CRR)
- Archival: Amazon S3 Glacier Flexible Retrieval / Deep Archive
- Monitoring: AWS CloudWatch Alarms and S3 Storage Lens

## Relationships
- Messaging & Event Bus -> Stream Ingestion: Pushes batch audit events via AWS SQS/SNS integration (HTTPS)
- Stream Ingestion -> Secure Vault: Writes encrypted, immutable objects using TLS 1.3 and AWS SigV4
- Secure Vault -> S3 Cross-Region Replication: Replicates immutable audit objects across AWS regions (HTTPS)

## Technology Stack
- Amazon Kinesis Data Firehose: Natively handles batching, compression, and buffering without custom code to minimize operational overhead for a 3-engineer team
- Amazon S3 Object Lock (Compliance Mode): Enforces strict WORM storage to satisfy 7-year regulatory retention mandates (R-06)
- AWS KMS: Manages customer-managed keys (CMK) and envelope encryption to protect cardholder and audit data
- Amazon S3 Glacier Flexible Retrieval: Automatically transitions aged audit logs to low-cost storage to stay within the 25,000 EUR monthly budget

## Rationale
This architecture uses serverless, managed AWS services to minimize operational complexity for a three-engineer team while scaling to 3,000 TPS. Furthermore, it strictly enforces PCI-DSS compliance, encryption, and tamper-evident 7-year auditability.