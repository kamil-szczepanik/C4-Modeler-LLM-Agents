## Overview
The Online Bookstore system uses a regionally partitioned PostgreSQL database architecture on AWS to ensure GDPR/CCPA compliance and low-latency transactions. It securely manages user data, multi-currency catalogs, and asynchronous event streaming for recommendations.

## Key Elements
- Core Transaction Engine (Amazon RDS PostgreSQL)
- Catalog & JSONB Store
- CDC Publisher (AWS DMS / Debezium)
- Amazon Kinesis
- AWS Secrets Manager
- Amazon CloudWatch

## Relationships
- Checkout & Cart Service -> Core Transaction Engine: Executes ACID writes [PostgreSQL protocol, TLS 1.3, IAM Auth]
- Catalogue & Search Service -> Catalog & JSONB Store: Queries product details [PostgreSQL protocol, TLS 1.3]
- Database -> Amazon Kinesis: Streams transaction events for recommendations [CDC / PostgreSQL Logical Decoding]
- Database -> Amazon CloudWatch: Routes audit logs and performance metrics [AWS API]

## Technology Stack
- Amazon RDS (PostgreSQL with read replicas): Provides ACID compliance and Multi-AZ high availability.
- JSONB: Enables flexible product metadata storage.
- AWS DMS / Debezium: Facilitates low-latency change data capture (CDC).
- AWS Secrets Manager: Secures credentials with automatic rotation.

## Rationale
Regionally isolated database instances enforce strict GDPR/CCPA data residency requirements across all deployment regions. Asynchronous CDC streaming via Kinesis protects checkout performance while feeding recommendations.