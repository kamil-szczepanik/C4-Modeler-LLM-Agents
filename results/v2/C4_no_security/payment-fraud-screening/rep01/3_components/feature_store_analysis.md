## Overview
[System screens card-not-present payment authorizations for fraud in real time and provides a case management system for analyst reviews. Core purpose is ensuring sub-50ms fraud detection while maintaining PCI-DSS compliance and 7-year auditability.]

## Key Elements
- **Users**: Fraud Analyst, Risk Operations Manager, Compliance Auditor
- **External Systems**: Merchant / Payment Gateway, External IdP, Amazon S3 / Glacier
- **Containers**: AWS API Gateway / ALB, Real-Time Scoring Engine, Case Management Backend & UI, Amazon ElastiCache Redis (Feature Store), Amazon S3 / Athena (Audit Log Storage)
- **Feature Store Components**: Feature Retrieval API, Feature Snapshotter, Feature Ingestion Worker, Feature Definition Registry

## Relationships
- **Real-Time Scoring Engine -> Feature Retrieval API**: Fetches online features [Redis Protocol]
- **Feature Snapshotter -> Audit Log Storage**: Flushes immutable feature vectors [HTTPS / S3 API]
- **Case Management Backend -> Audit Log Storage**: Queries historical snapshots [Amazon Athena]
- **Merchant -> API Gateway**: Submits payment authorization requests [HTTPS]

## Technology Stack
- **Compute**: AWS ECS Fargate (scalable container orchestration for a 3-person team)
- **Languages**: Go (high-performance scoring engine and retrieval API), Python (feature ingestion, snapshotting, and machine learning models)
- **Databases & Caching**: Amazon ElastiCache Redis (sub-millisecond feature lookups with Multi-AZ and `volatile-lru`), PostgreSQL / AWS RDS (feature definition registry and case management)
- **Audit & Storage**: Amazon S3 and Amazon Athena (tamper-evident 7-year audit logging and querying)
- **Security**: AWS KMS and TLS (encryption at-rest and in-transit for PCI-DSS compliance)
- **Infrastructure as Code**: Terraform (fully automated provisioning within the 25,000 EUR monthly budget)

## Rationale
[This architecture uses managed AWS services and ECS Fargate to minimize operational overhead for a three-person team while strictly enforcing PCI-DSS compliance. ElastiCache Redis and Go containers guarantee sub-50ms P99 latencies, while asynchronous S3 snapshots ensure immutable 7-year auditability within the 25,000 EUR budget.]