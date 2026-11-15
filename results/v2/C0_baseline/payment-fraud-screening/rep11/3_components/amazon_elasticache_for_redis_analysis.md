## Overview
Amazon ElastiCache for Redis serves as the high-throughput, in-memory data store providing sub-50ms feature lookups for the Real-Time Payment Fraud Screening system. It empowers the Fraud Screening Engine to evaluate card-not-present transactions against dynamic risk models while respecting strict PCI-DSS constraints.

## Key Elements
- In-Memory Data Store Engine (Redis OSS v7.x)
- Multi-AZ Node Group (1 Primary, 1 Read Replica in eu-west-1)
- Custom Parameter Group (Hardened configuration)
- AWS Secrets Manager (Credential injection)
- Amazon CloudWatch (Audit logging and metrics)

## Relationships
- Fraud Screening Engine -> Amazon ElastiCache for Redis: Queries and updates feature vectors via RESP over TLS (TCP/6379)
- Amazon ElastiCache for Redis -> Amazon CloudWatch: Streams slow queries and connection logs via AWS API
- AWS Secrets Manager -> Amazon ElastiCache for Redis: Provides Redis AUTH authentication tokens via secure API

## Technology Stack
- Amazon ElastiCache for Redis OSS (v7.x): Chosen for sub-50ms latency performance and managed Multi-AZ high availability.
- Terraform: Utilized for Infrastructure as Code to reduce operational overhead for a 3-engineer team.
- AWS KMS: Encrypts data at rest within the managed cluster.
- TLS 1.3: Enforces encryption in transit for PCI-DSS compliance.

## Rationale
This component architecture achieves P99 latency under 50 ms at 3,000 TPS while maintaining operational simplicity for a three-engineer team within a €25,000 monthly budget. Transient cache loss and a 15ms client timeout fulfill the 1-minute fail-safe availability requirement without over-engineering disaster recovery.