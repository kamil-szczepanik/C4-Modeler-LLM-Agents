## Overview
The Case Management & Analytics API processes fraud investigation workflows and reporting for analysts and risk managers. It enforces PCI-DSS compliance and sub-50ms latency while maintaining immutable 7-year audit logs on AWS.

## Key Elements
- Fraud Analyst & Risk Manager (Primary users)
- Frontend Web App (React SPA)
- Case Management & Analytics API (NestJS backend service)
- REST/GraphQL Handler with Data Masking Middleware
- Case Service and Analytics Query Engine
- Amazon RDS PostgreSQL Primary (OLTP) and Read Replica (OLAP)
- Amazon S3 with Object Lock and AWS KMS

## Relationships
- Frontend Web App -> REST/GraphQL Handler: API requests [HTTPS]
- REST/GraphQL Handler -> Case Service: Transactional state updates [In-Memory / TCP]
- Case Service -> Amazon RDS PostgreSQL Primary: Case reads and writes [TCP/SQL]
- Analytics Query Engine -> Amazon RDS Read Replica: Reporting queries [TCP/SQL]
- Audit Logger -> Amazon S3 with Object Lock: Immutable audit records [HTTPS via AWS SDK]

## Technology Stack
- Node.js with NestJS: Chosen for rapid API development with a 3-engineer team
- Amazon RDS PostgreSQL: Provides transactional persistence with CQRS Read Replica for OLAP isolation
- Amazon S3 with Object Lock: Ensures tamper-evident, 7-year audit log retention for PCI-DSS
- AWS ECS Fargate: Provides serverless container orchestration within the 25,000 EUR monthly budget

## Rationale
CQRS architecture separates OLTP case management from OLAP analytics, protecting performance under high load. Automated AWS Fargate scaling and managed databases minimize operational overhead for the 3-engineer team.