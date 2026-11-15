## Overview
The system provides real-time card-not-present payment fraud screening and case management for a mid-size payment processor. It screens payment authorizations in real-time while ensuring strict PCI-DSS compliance and 7-year tamper-evident auditability.

## Key Elements
- **Hot State Table Module**: DynamoDB provisioned capacity table storing transaction velocity counters and card profiles.
- **Case Management Table Module**: DynamoDB on-demand capacity table storing analyst investigation cases and audit logs.
- **DynamoDB Streams Processor**: AWS Lambda function capturing mutation events for downstream audit export.
- **Audit Ledger Archive Module**: Amazon S3 with Object Lock (Compliance Mode) for immutable 7-year retention.
- **IAM Fine-Grained Access Policy Module**: AWS IAM enforcing least-privilege attribute-based access control (ABAC).
- **Global Table Replication Module**: DynamoDB Global Tables ensuring multi-AZ resilience in `eu-west-1`.
- **Time-To-Live (TTL) Expiry Module**: Native DynamoDB background process purging transient records.
- **DynamoDB Point-in-Time Recovery (PITR) Module**: Continuous backup module for investigation logs.

## Relationships
- Scoring Engine Container -> Hot State Table Module: Reads/Writes velocity state via *AWS SDK (TCP/443 via VPC Endpoint)*.
- Case Management Backend Container -> Case Management Table Module: Reads/Writes case data via *AWS SDK (TCP/443)*.
- Hot State Table Module -> DynamoDB Streams Processor: Triggers audit logging via *DynamoDB Streams*.
- DynamoDB Streams Processor -> Audit Ledger Archive Module: Flushes encrypted mutation logs via *AWS SDK (HTTPS)*.
- Case Management Table Module -> AWS KMS: Encrypts data at rest via *AWS KMS CMK (Envelope Encryption)*.
- IAM Fine-Grained Access Policy Module -> Hot State Table Module: Secures access boundaries via *IAM Policies*.
- Hot State Table Module -> TTL Expiry Module: Automatically purges expired records via *Native DynamoDB TTL background process*.
- Case Management Table Module -> DynamoDB PITR Module: Continuously backs up logs via *DynamoDB PITR*.

## Technology Stack
- **Amazon DynamoDB**: Chosen for single-digit millisecond latency (R-04) without the operational overhead of DAX.
- **AWS Lambda**: Chosen for serverless execution of mutation capture without managing compute infrastructure.
- **Amazon S3 Object Lock**: Chosen for immutable, tamper-evident 7-year audit retention (R-06).
- **AWS KMS**: Chosen for envelope encryption to satisfy PCI-DSS data security constraints (R-05).

## Rationale
The architecture uses fully managed AWS services to meet strict performance and compliance mandates while respecting a 25,000 EUR monthly budget. It limits operational toil, enabling a three-engineer team to maintain high availability and security.