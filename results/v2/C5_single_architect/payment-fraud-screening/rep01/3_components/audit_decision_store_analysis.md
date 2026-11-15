## Overview
The Audit & Decision Store container provides tamper-evident storage and 7-year audit retention for real-time payment fraud decisions on AWS. It ensures PCI-DSS compliance and high performance while operating within a fixed budget and small team.

## Key Elements
* Data Access Layer (Go / `pgx`)
* Audit & Cryptographic Service (Go)
* Retention & Archival Worker (Go / AWS Lambda)
* Partition Manager (Go)
* Amazon RDS PostgreSQL

## Relationships
* Fraud Scoring Engine -> Data Access Layer: Reads and writes decision logs [PostgreSQL protocol]
* Case Management Backend -> Data Access Layer: Accesses decision and audit records [PostgreSQL protocol]
* Audit & Cryptographic Service -> Partition Manager: Writes chained audit records to active partitions [Internal Go Interface]
* Retention & Archival Worker -> Amazon S3 Glacier: Archives cold partitions [AWS SDK / HTTPS]

## Technology Stack
* Go: Minimizes language sprawl and maintenance overhead for a 3-engineer team.
* Amazon RDS PostgreSQL: Provides reliable ACID compliance and standard relational storage.
* Application-level HMAC/Merkle-tree chaining: Ensures tamper-evidence without complex DB extensions.
* AWS S3 Glacier: Minimizes long-term storage costs for the 7-year retention policy.

## Rationale
This architecture meets strict auditability, security, and PCI-DSS compliance requirements while controlling infrastructure costs. Application-level cryptographic chaining and declarative partitioning maintain high performance and low maintenance effort.