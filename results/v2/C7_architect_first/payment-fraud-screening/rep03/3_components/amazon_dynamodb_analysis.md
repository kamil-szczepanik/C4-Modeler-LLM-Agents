## Overview
The Amazon DynamoDB container provides high-throughput, low-latency hot data storage for payment fraud scoring state, rule definitions, and transaction audit logs. It ensures strict PCI-DSS Level 1 compliance while supporting sub-50ms fraud decision latency for 3,000 requests per second.

## Key Elements
- Table: `FraudDecisions` (Partition Key: `TransactionId`, Sort Key: `Timestamp`)
- Table: `FraudRules` (Partition Key: `RuleId`)
- Table: `EntityState` (Partition Key: `EntityFingerprint`)
- DynamoDB Streams: Captures item-level modifications for S3 archival
- AWS Key Management Service (KMS): Manages customer-managed encryption keys

## Relationships
- Fraud Scoring Engine -> `FraudDecisions`: Writes immutable audit payloads [AWS SDK / HTTPS]
- Fraud Scoring Engine -> `FraudRules` & `EntityState`: Reads compiled rules and updates velocity counters [AWS SDK / HTTPS]
- `FraudDecisions` -> DynamoDB Streams: Streams real-time transaction events [AWS Internal]
- DynamoDB Streams -> Amazon S3 Object Lock: Archives tamper-evident audit logs for 7 years [AWS Kinesis Firehose / HTTPS]

## Technology Stack
- Amazon DynamoDB: Serverless NoSQL database chosen to eliminate operational overhead for a 3-engineer team and guarantee sub-10ms query latencies within budget.
- DynamoDB Streams: Real-time change data capture mechanism utilized to trigger automated S3 data archival.
- AWS KMS: Customer-managed encryption keys enforcing AES-256 encryption at rest to satisfy PCI-DSS Level 1 data protection mandates.
- Amazon S3 Object Lock: Long-term tamper-evident storage backend fulfilling 7-year regulatory auditability constraints cost-effectively.

## Rationale
This architecture uses serverless AWS managed services to maintain a fixed infrastructure budget under 25,000 EUR per month while operating with only three engineers. The design successfully delivers sub-50ms P99 transaction latency and 7-year regulatory auditability without adding complex cache infrastructure.