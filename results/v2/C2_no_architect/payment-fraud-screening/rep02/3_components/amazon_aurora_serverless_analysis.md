## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management tools for analysts. It ensures PCI-DSS Level 1 compliance, 7-year auditability, and sub-50ms latency within a €25,000 monthly budget.

## Key Elements
- Amazon Aurora Serverless v2
- AWS ECS Fargate
- PgBouncer Connection Pooler
- AWS KMS
- AWS Secrets Manager
- Amazon CloudWatch
- Amazon S3 with Object Lock
- AWS IAM Database Authentication

## Relationships
- Scoring Container -> Amazon Aurora Serverless v2: Queries transaction context via Internal TCP/TLS (Port 5432/3306)
- Case Management Container -> Amazon Aurora Serverless v2: Reads and writes case data via Internal TCP/TLS (Port 5432/3306)
- Aurora Serverless v2 -> Amazon CloudWatch: Streams audit logs and performance metrics
- Aurora Serverless v2 -> Amazon S3 with Object Lock: Exports backups and audit trails for long-term retention

## Technology Stack
- Amazon Aurora Serverless v2: Scalable relational database minimizing operational overhead for a 3-engineer team
- AWS KMS: Storage-level encryption using customer-managed keys (CMK) for data protection
- AWS IAM Database Authentication: Eliminates static credentials for ECS Fargate containers
- PgBouncer: Manages database connections to prevent connection storms and maintain <50ms P99 latency

## Rationale
Aurora Serverless v2 automatically scales to handle traffic spikes within the €25k budget while fitting the 3-engineer operational capacity. Multi-AZ deployment and strict security controls satisfy high availability, PCI-DSS compliance, and 7-year auditability requirements.