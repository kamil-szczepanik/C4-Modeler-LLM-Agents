## Overview
[The Admin & Reporting Service provides secure analytics, financial reconciliation, and compliance reporting for store operations and authors within the Online Bookstore platform.]

## Key Elements
* Store Operations Manager
* Content/Author Relations Manager
* Admin & Reporting Service REST API Container
* AWS ECS / EKS Worker Pool & Fargate Spot Tasks
* AWS Redshift / OLAP Data Warehouse & Read Replicas
* AWS S3 Report Export Buckets

## Relationships
* Web Frontend SPA/SSR -> Admin & Reporting Service REST API: Sends administrative and reporting queries using REST and gRPC over mTLS
* Admin & Reporting Service -> AWS Redshift / Read Replicas: Queries analytical data using SQL over TLS 1.3
* Admin & Reporting Service -> AWS S3: Persists scheduled and on-demand report exports using AWS SDK with SSE-KMS
* Admin & Reporting Service -> AWS SQS: Queues asynchronous batch export jobs

## Technology Stack
* AWS ECS / EKS: Container orchestration ensuring resource isolation for API and worker nodes
* AWS SQS & Fargate Spot: Asynchronous processing to handle heavy batch report generation without impacting synchronous APIs
* AWS Redshift & Read Replicas: OLAP data storage decoupling analytical queries from primary transactional databases
* AWS KMS & TLS 1.3: Data encryption at rest and in transit ensuring GDPR and CCPA compliance
* JSON Web Tokens (JWT): Cryptographic identity verification enforcing Role-Based Access Control (RBAC) and Row-Level Security (RLS)

## Rationale
[This architecture decouples heavy analytical workloads from transactional datastores to protect the 99.95% customer checkout uptime SLA. Strict resource isolation, RBAC, and asynchronous batch processing secure sensitive financial and PII data while meeting multi-region performance and compliance mandates.]