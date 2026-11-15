## Overview
The Online Bookstore system uses a polyglot persistence strategy with AWS Aurora PostgreSQL and AWS DynamoDB to support high-throughput e-commerce operations. It ensures multi-region scalability, strict GDPR/CCPA compliance, and secure data isolation.

## Key Elements
* Transactional Data Store (AWS Aurora PostgreSQL Multi-AZ with Primary Writer and Read-Replica Cluster)
* NoSQL Data Store (AWS DynamoDB)
* Key Management Component (AWS KMS)
* Microservices (Catalog & Search, Order & Checkout, Recommendation, Content Management)

## Relationships
* Catalog & Search Microservice -> Aurora Read-Replica Cluster: Reads catalog data [PostgreSQL over TLS 1.3 with IAM Authentication]
* Order & Checkout Microservice -> Aurora Primary Writer: Reads and writes order data [PostgreSQL over TLS 1.3 with IAM Authentication]
* Recommendation Microservice -> DynamoDB & Aurora Read-Replica: Reads recommendations and cart data [AWS SDK (HTTPS) / PostgreSQL over TLS 1.3]
* Content Management & Moderation Microservice -> Aurora Primary Writer: Writes moderation data [PostgreSQL over TLS 1.3 with IAM Authentication]
* Data Stores -> AWS KMS: Enforces encryption-at-rest, Column-Level Encryption, and cryptographic erasure [Internal AWS API]

## Technology Stack
* AWS Aurora PostgreSQL: Chosen for ACID compliance, multi-currency decimal handling, and relational catalog/order integrity.
* AWS DynamoDB: Chosen for sub-10ms key-value latency supporting recommendations and cart sessions.
* AWS KMS: Chosen for encryption-at-rest, CMK least-privilege management, and GDPR cryptographic erasure.
* TLS 1.3 & mTLS: Chosen for encrypted data-in-transit across all internal database links.
* AWS IAM Database Authentication: Chosen to eliminate static credentials in favor of short-lived tokens.

## Rationale
This architecture uses polyglot persistence to separate relational transactional workloads from high-volume NoSQL lookups, meeting the 1M MAU scalability goal. Robust security controls, including IAM auth, least-privilege RBAC, and KMS encryption, ensure full GDPR/CCPA compliance and OWASP mitigation.