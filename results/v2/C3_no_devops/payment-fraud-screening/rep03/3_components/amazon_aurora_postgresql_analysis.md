## Overview
The system provides real-time card-not-present payment fraud screening for a mid-size payment processor, enforcing low-latency decisions and case management. It is designed to meet strict PCI-DSS Level 1 compliance and 7-year auditability constraints within a fixed cloud infrastructure budget.

## Key Elements
- **Amazon Aurora PostgreSQL:** System-of-record relational database deployed in AWS eu-west-1.
- **Aurora PostgreSQL Instance:** Primary and Read Replica nodes running PostgreSQL 15+.
- **Storage Volume:** Distributed, six-way replicated virtual volume across three Availability Zones.
- **Scoring Engine:** Rust-based microservice running on AWS ECS Fargate.
- **Case Management App:** Node.js/Python backend with a React SPA running on AWS ECS Fargate.
- **Amazon ElastiCache (Redis):** In-memory cache for hot rule evaluations.

## Relationships
- Scoring Engine -> Amazon Aurora PostgreSQL Instance: Writes audit states via Synchronous SQL over TLS 1.3 using IAM Authentication.
- Case Management App -> Amazon Aurora PostgreSQL Instance: Performs CRUD operations for case reviews via Synchronous SQL over TLS 1.3 using IAM Authentication.
- Scoring Engine -> Amazon ElastiCache (Redis): Reads hot rules and model data via Redis Protocol over TLS 1.3.

## Technology Stack
- **Amazon Aurora PostgreSQL 15+:** Selected for ACID compliance, multi-AZ high availability, and 7-year audit data storage.
- **AWS IAM Database Authentication & TLS 1.3:** Enforced to eliminate hardcoded credentials and secure data in transit.
- **AWS KMS Customer Managed Key (CMK):** Used for encryption at rest to satisfy PCI-DSS Level 1 requirements.
- **PostgreSQL Row-Level Security & Column-Level Encryption:** Implemented to prevent unauthorized access to sensitive Primary Account Number (PAN) data.

## Rationale
This architecture uses an in-memory cache for hot evaluations to achieve sub-50ms P99 latency while delegating state persistence to Aurora PostgreSQL. Multi-AZ deployment and strict access controls ensure high availability and PCI-DSS compliance within the 25,000 EUR monthly budget.