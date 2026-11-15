## Overview
The system is an online bookstore providing catalog browsing, shopping carts, secure checkout, reviews, and recommendations. It utilizes an AWS-hosted microservices architecture designed for high scalability and compliance.

## Key Elements
- **Query Router & Protocol Engine**: Handles incoming MongoDB wire protocol requests over TCP/TLS.
- **Storage Subsystem**: Manages distributed SSD storage volumes across 3 Availability Zones.
- **Replication Manager**: Synchronizes writes across primary and up to 15 replica instances.
- **Transaction & Index Manager**: Handles document-level ACID transactions and maintains B-tree indexing.
- **Catalog Service**: Microservice connecting to the database.

## Relationships
- Catalog Service -> Query Router & Protocol Engine: Sends MongoDB wire protocol requests via [TCP/TLS].
- Amazon DocumentDB -> AWS KMS: Uses customer-managed keys for storage-at-rest encryption.
- Amazon DocumentDB -> Amazon CloudWatch Logs: Streams advanced audit logs.

## Technology Stack
- **Amazon DocumentDB**: Managed NoSQL database ensuring MongoDB 5.0 compatibility and high availability.
- **AWS KMS**: Provides customer-managed keys for encryption to meet GDPR/CCPA standards.
- **AWS Secrets Manager**: Enables automated, zero-downtime database password rotation.
- **Amazon CloudWatch**: Used for tracking database metrics, `IndexCacheHitRatio`, and streaming audit logs.

## Rationale
This architecture ensures 99.95% uptime and scalability for 1M MAU through multi-AZ replication and auto-scaling read replicas. Strict network isolation and audit logging satisfy GDPR, CCPA, and OWASP security requirements.