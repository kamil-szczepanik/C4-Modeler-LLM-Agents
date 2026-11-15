## Overview
The Case Management Backend provides secure workflow and review capabilities for fraud analysts within the Real-Time Payment Fraud Screening system. It ensures strict PCI-DSS compliance and 7-year auditability while allowing analysts to process suspicious payment cases.

## Key Elements
- Case API Controller: Entry point handling HTTPS requests with OIDC token validation and Data Masking Middleware.
- Case Service: Orchestrates business workflow logic, state transitions, and SLA/workload metrics.
- Audit & Export Service: Manages asynchronous report generation and publishing to Amazon SQS.
- Data Access Repository: Interfaces with Amazon Aurora Serverless v2 PostgreSQL using parameterized queries.
- Amazon Aurora Serverless v2 PostgreSQL: Persistent storage for case metadata and operational records.
- Amazon S3 & Amazon SQS: Staging storage for secure audit exports and asynchronous message queuing.

## Relationships
- Fraud Analyst to Case API Controller: Accesses review queues and case details via [HTTPS].
- Case API Controller to Case Service: Invokes workflow operations internally.
- Audit & Export Service to Amazon SQS: Publishes asynchronous export jobs via [AWS SDK / HTTPS].
- Data Access Repository to Amazon Aurora Serverless v2 PostgreSQL: Persists and retrieves encrypted case data via [TLS / TCP 5432].
- Audit & Export Service to Amazon S3: Stages exported audit reports via [AWS SDK / HTTPS].

## Technology Stack
- Node.js / TypeScript: Core runtime and language chosen for rapid development by a three-person engineering team.
- Amazon ECS on AWS Fargate: Serverless container execution ensuring isolated, scalable deployments within budget.
- Amazon Aurora Serverless v2 PostgreSQL: Relational database providing automatic scaling and robust transactional integrity.
- AWS KMS: Encryption mechanism using customer-managed keys for data at rest compliance.

## Rationale
This modular monolith architecture fits the requirements by maintaining a low operational overhead suitable for a three-person team while strictly enforcing PCI-DSS Level 1 security. Asynchronous processing and serverless infrastructure guarantee compliance with budget limits and performance constraints.