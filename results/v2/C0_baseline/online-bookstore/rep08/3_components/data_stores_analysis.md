## Overview
The Online Bookstore data architecture provides secure, multi-region, and compliant storage for catalog, transactional, recommendation, and privacy data. It supports global scale (1M MAU) and high availability across AWS regions.

## Key Elements
- **Catalog & Transaction DB**: Amazon Aurora PostgreSQL (Multi-AZ, Global Database)
- **Compliance & Audit Store**: Amazon DynamoDB with DynamoDB Streams
- **Recommendation Cache**: Amazon ElastiCache for Redis (Global Datastore)
- **Security & Governance**: AWS KMS (CMK), AWS Secrets Manager, IAM Database Authentication, AWS Organizations SCPs
- **Observability**: Amazon CloudWatch, AWS CloudTrail, GuardDuty, VPC Flow Logs

## Relationships
- **Catalog & Search Service -> Aurora PostgreSQL**: Reads/writes catalog data via JDBC over TLS
- **Checkout & Order Service -> Aurora PostgreSQL**: Persists ACID-compliant transactional data via JDBC over TLS
- **Recommendation Service -> ElastiCache for Redis**: Retrieves pre-computed recommendations via RESP protocol
- **User Privacy Service -> DynamoDB**: Manages compliance and right-to-be-forgotten data via AWS SDK over HTTPS
- **Global Regions (us-east-1, eu-west-1, ap-southeast-1) -> Aurora/Redis**: Replicates data globally using encrypted inter-region transit and VPC peering

## Technology Stack
- **Amazon Aurora PostgreSQL**: Chosen for ACID compliance, multi-currency support, and global read replicas.
- **Amazon DynamoDB**: Selected for rapid compliance data handling, TTL-based purging, and regional data residency.
- **Amazon ElastiCache for Redis**: Deployed for sub-millisecond recommendation retrieval to meet performance targets.
- **AWS KMS & IAM**: Implemented for end-to-end encryption at rest and passwordless database authentication.

## Rationale
This architecture ensures strict GDPR/CCPA compliance and 99.95% availability while delivering low-latency (<2s) global performance for 1M MAU. Multi-region replication and robust security controls protect revenue and customer trust.