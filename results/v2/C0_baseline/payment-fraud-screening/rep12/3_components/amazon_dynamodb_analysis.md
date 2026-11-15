## Overview
This system provides real-time fraud screening for payment authorizations and case management for fraud analysts. It ensures sub-50ms decision latency, strict PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a fixed budget.

## Key Elements
- Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
- Case Management System API (Node.js / Express API on ECS)
- Hot Feature Table (DynamoDB Table, NoSQL)
- Case Management Table (DynamoDB Table, NoSQL)
- Compliance Reporting Worker (AWS Lambda)
- Amazon S3 with Object Lock

## Relationships
- Real-Time Scoring Engine -> Hot Feature Table: Queries feature attributes [AWS SDK over TLS 1.3, IAM Auth via VPC Gateway Endpoints]
- Case Management System API -> Case Management Table: Reads and updates case states [AWS SDK over TLS 1.3, HTTPS]
- DynamoDB Streams -> Compliance Reporting Worker: Triggers archival of closed cases [AWS Lambda]
- Compliance Reporting Worker -> Amazon S3: Stores historical audit logs [AWS SDK over TLS 1.3]

## Technology Stack
- AWS DynamoDB: Provides single-digit millisecond latency for hot features and active cases while adhering to budget constraints.
- AWS KMS: Encrypts data at rest using customer-managed keys (CMK) with annual rotation for PCI-DSS compliance.
- Amazon S3 with Object Lock: Archives historical audit logs to ensure 7-year tamper-evident retention cost-effectively.
- AWS VPC Gateway Endpoints: Secures data in transit by routing database traffic off the public internet.

## Rationale
This architecture balances ultra-low latency requirements with strict security and auditability mandates. Operational simplicity is maintained for a three-engineer team by leveraging serverless and managed AWS services within the 25,000 EUR monthly budget.