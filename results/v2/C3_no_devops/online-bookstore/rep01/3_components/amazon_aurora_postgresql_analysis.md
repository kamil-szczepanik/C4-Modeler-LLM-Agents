## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with recommendations and reviews. It handles high-traffic transactions globally while enforcing strict GDPR/CCPA compliance and 99.95% availability.

## Key Elements
- **Order & Checkout Container**: Node.js/TypeScript container processing cart and secure checkout operations.
- **Amazon Aurora PostgreSQL**: Primary relational database handling transactional order data, customer history, and multi-currency schemas.
- **Primary DB Instance (Writer)**: Accepts write-heavy transactions from the checkout container.
- **Replica DB Instances (Readers)**: Offloads read-only queries across Availability Zones.
- **Aurora Storage Volume**: Distributed SSD volume spanning three AZs for fault tolerance.
- **Aurora Global Database**: Cross-region deployment across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- **Database Migration Manager**: Flyway/Liquibase managing schema versioning.

## Relationships
- **Order & Checkout Container -> Primary DB Instance (Writer)**: Persists transactional order data via PostgreSQL Wire Protocol over TLS 1.3.
- **Primary DB Instance (Writer) -> Aurora Storage Volume**: Performs block-level replication across 3 AZs using AWS Proprietary Protocol.
- **Aurora Global Database -> Regional Replications**: Synchronizes data across cross-region clusters using AWS KMS encrypted transit.

## Technology Stack
- **Amazon Aurora PostgreSQL**: Provides ACID compliance, high availability, and multi-region replication.
- **AWS KMS**: Enforces encryption-at-rest and encrypted cross-region replication with region-specific customer-managed keys.
- **AWS IAM & AWS Secrets Manager**: Eliminates hardcoded credentials and provides secure database authentication.
- **Flyway / Liquibase**: Manages automated database schema versioning and multi-currency decimal types.

## Rationale
This architecture guarantees zero data loss, ACID transaction reliability, and low-latency local reads across multiple regions. Furthermore, private VPC isolation and comprehensive audit logging fulfill strict GDPR/CCPA and OWASP security requirements.