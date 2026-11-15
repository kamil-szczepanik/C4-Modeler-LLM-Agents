## Overview
The Audit Storage container provides tamper-evident, 7-year retention logging for payment fraud screening decisions. It ensures strict compliance with PCI-DSS Level 1 requirements within a serverless AWS architecture.

## Key Elements
- **Audit Ingestion API**: AWS Lambda (Python) for receiving audit payloads.
- **Object Lock Manager**: Amazon S3 (Glacier Flexible Retrieval / Compliance Mode) for WORM storage.
- **Audit Indexer & Hash Verifier**: Amazon DynamoDB and AWS Lambda for computing cryptographic hashes and maintaining query indexes.
- **Audit Query Service**: AWS Lambda (Python) for secure compliance reporting and audit retrieval.
- **Compliance Guardrails & IaC**: Terraform/CloudFormation with AWS Config rules and AWS KMS customer-managed keys (CMK).

## Relationships
- Fraud Scoring Engine / Case Management Service -> **Audit Ingestion API**: Sends decision payloads via AWS SDK (HTTPS/TLS 1.3).
- **Audit Ingestion API** -> **Object Lock Manager**: Writes immutable audit objects via AWS SDK (S3 PutObject with Legal Hold/Retention).
- **Audit Ingestion API** -> **Audit Indexer & Hash Verifier**: Stores audit metadata and cryptographic hashes via AWS SDK (HTTPS).
- Fraud Analyst / Compliance & Audit Archive -> **Audit Query Service**: Requests audit trails via HTTPS/TLS 1.3.
- **Audit Query Service** -> **Audit Indexer & Hash Verifier**: Resolves query metadata via AWS SDK.
- **Audit Query Service** -> **Object Lock Manager**: Fetches raw immutable payload data via AWS SDK.
- Compliance & Audit Archive -> **Object Lock Manager** & **Audit Indexer & Hash Verifier**: Reads historical logs and queries indexes via AWS SDK (HTTPS/TLS 1.3).

## Technology Stack
- **AWS Lambda (Python)**: Powers ingestion and query services, minimizing operational overhead for a 3-engineer team.
- **Amazon S3 (Compliance Mode)**: Enforces immutable WORM storage to meet the 7-year audit retention constraint.
- **Amazon DynamoDB**: Stores cryptographic hashes and query indexes for rapid compliance verification.
- **AWS KMS**: Secures data at rest with customer-managed keys to satisfy PCI-DSS Level 1.
- **Terraform/CloudFormation & AWS Config**: Automates infrastructure deployment and prevents configuration drift.

## Rationale
This serverless component model fulfills stringent PCI-DSS Level 1 and 7-year tamper-evident audit mandates while remaining operable by a 3-engineer team under a 25,000 EUR monthly budget. Automated guardrails and fully managed AWS services eliminate infrastructure maintenance overhead.