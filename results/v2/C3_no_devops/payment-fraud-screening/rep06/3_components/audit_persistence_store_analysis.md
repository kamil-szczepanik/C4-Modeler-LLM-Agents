## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud under 50 ms while enforcing strict PCI-DSS Level 1 compliance. It uses an AWS cloud architecture to process transactions and provide secure audit trails for fraud analysts.

## Key Elements
- **Amazon Aurora PostgreSQL**: Primary relational database with cryptographic chaining for tamper-evident storage.
- **Audit Ledger Writer**: PL/pgSQL append-only component using SHA-256 cryptographic hashing.
- **Data Retention Manager**: Automated monthly table partitioning and lifecycle policies targeting AWS S3 Glacier.
- **Transaction & Case Repository**: Stores operational transaction states and case management data.
- **Audit Query & Retrieval Gateway**: Read-replica routing service with an internal Redis caching layer and batch hydration APIs.
- **AWS S3 Glacier Flexible Retrieval**: Cold storage tier featuring AWS S3 Object Lock for WORM immutability.

## Relationships
- **Scoring Engine to Aurora PostgreSQL**: Connects via JDBC over TLS 1.3 with mutual TLS (mTLS) and AWS IAM database authentication.
- **Case Management API to Aurora PostgreSQL**: Connects via JDBC over TLS 1.3 with mTLS and IAM database authentication, restricted by Row-Level Security (RLS).
- **Data Retention Manager to AWS S3 Glacier**: Archives aged partitions via AWS SDK using VPC endpoints with WORM Object Lock.
- **Audit Query & Retrieval Gateway to S3 Glacier**: Fetches cold data asynchronously using pre-signed S3 URLs with 15-minute expiration windows.

## Technology Stack
- **Amazon Aurora PostgreSQL**: Chosen for reliable relational storage, read replicas, and native partitioning to support 7-year audit requirements.
- **SHA-256 Cryptographic Chaining**: Implemented via PL/pgSQL to ensure tamper-evident audit logs (R-06).
- **AWS KMS**: Utilized with customer-managed keys (CMK) and key rotation for data encryption at rest.
- **AWS S3 Glacier Flexible Retrieval with S3 Object Lock**: Selected for cost-effective 7-year long-term retention with WORM immutability.
- **Amazon ElastiCache Redis**: Deployed within the retrieval gateway for caching hot historical queries.

## Rationale
This architecture ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability while adhering to the 25,000 EUR monthly infrastructure budget. Automated data tiering and read-replica routing minimize operational overhead, allowing a three-engineer team to maintain high availability and performance.