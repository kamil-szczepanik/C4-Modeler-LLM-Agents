## Overview
[The system provides real-time fraud screening for payment authorizations and case management for analysts using AWS. It ensures sub-50ms latency, PCI-DSS compliance, and 7-year tamper-evident auditability.]

## Key Elements
- Fraud Scoring Engine (Java / Spring Boot)
- Case Management & Rule UI (Node.js / TypeScript)
- Amazon DynamoDB (AWS DynamoDB Tables)
- DynamoDB Streams (AWS DynamoDB Streams)
- DynamoDB VPC Endpoint (AWS PrivateLink Interface Endpoint)
- AWS KMS Customer Managed Keys (AWS KMS CMK)
- Amazon S3 with Object Lock (Amazon S3)

## Relationships
- Fraud Scoring Engine -> DynamoDB VPC Endpoint: Reads and writes rule metadata [HTTPS / TLS 1.3, AWS SDK]
- Case Management & Rule UI -> DynamoDB VPC Endpoint: Reads and writes active case states [HTTPS / TLS 1.3, AWS SDK]
- DynamoDB Streams -> Amazon S3: Emits change data capture events for asynchronous audit logging [HTTPS]

## Technology Stack
- Amazon DynamoDB: Selected for sub-50ms latency and zero-downtime rule updates within budget
- AWS PrivateLink: Enforces TLS 1.3 data-in-transit security for PCI-DSS compliance
- AWS KMS CMK: Provides cryptographic data protection at rest for cardholder data
- Amazon S3 Object Lock: Guarantees tamper-evident 7-year audit log retention

## Rationale
[The architecture meets strict PCI-DSS and auditability constraints while maintaining sub-50ms latency at high throughput. Serverless AWS components optimize costs for a three-engineer team within a 25,000 EUR monthly budget.]