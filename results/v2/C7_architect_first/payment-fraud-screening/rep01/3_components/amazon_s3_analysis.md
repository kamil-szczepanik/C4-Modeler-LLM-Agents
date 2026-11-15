## Overview
This architecture details the Amazon S3 storage container for a real-time payment fraud screening system on AWS. It provides secure, WORM-compliant, 7-year audit retention and pseudonymized analytics within PCI-DSS Level 1 constraints.

## Key Elements
- **Bucket Policy Enforcer (IAM / AWS Lake Formation)**: Manages fine-grained access control and IAM conditions.
- **Object Lock & Vault Manager (S3 Object Lock)**: Enforces Write-Once-Read-Many (WORM) compliance in Compliance Mode.
- **Server-Side Encryption Engine (AWS KMS)**: Applies envelope encryption using customer-managed keys (CMK).
- **S3 Lifecycle Engine (AWS S3 Lifecycle)**: Manages automated tiering from Standard to S3 Glacier Deep Archive.
- **Athena Query Gateway (Amazon Athena)**: Executes sanitized queries over partitioned audit data.
- **Merchant Risk Manager & Compliance Officer**: External personas querying reporting and audit logs.

## Relationships
- Real-Time Scoring Engine -> Object Lock & Vault Manager: Writes decision audit payloads via AWS SDK (HTTPS/TLS 1.3).
- Compliance Officer -> Bucket Policy Enforcer: Queries archived audit logs via AWS Management Console / Athena (HTTPS).
- Merchant Risk Manager -> Athena Query Gateway: Queries pseudonymized fraud trends via BI tools (HTTPS).
- Athena Query Gateway -> Object Lock & Vault Manager: Reads parquet-formatted audit partitions via internal AWS backbone.
- DevOps Specialist -> S3 Lifecycle Engine: Manages automated tiering policies via Terraform (IaC).

## Technology Stack
- **Amazon S3**: Core object storage providing 99.999999999% durability and S3 Object Lock for tamper-evident retention.
- **AWS KMS**: AES-256 envelope encryption with annual key rotation to satisfy PCI-DSS data protection requirements.
- **Amazon Athena**: Serverless query service enabling analytics on stored audit data without managing infrastructure.
- **AWS Glue / Lambda**: Compacts raw JSON logs into compressed Apache Parquet format to optimize query costs.
- **Terraform (HashiCorp)**: Infrastructure as Code for automated, drift-free deployment by a three-engineer team.

## Rationale
This architecture meets the 7-year tamper-evident audit and PCI-DSS Level 1 requirements through S3 Object Lock and KMS encryption. Automated lifecycle tiering and Parquet compaction optimize storage and query costs to respect the 25,000 EUR monthly budget.