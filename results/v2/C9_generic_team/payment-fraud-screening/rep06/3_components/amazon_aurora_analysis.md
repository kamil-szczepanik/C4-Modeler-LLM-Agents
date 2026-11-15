## Overview
The system provides real-time fraud screening for payment authorizations and case management for financial analysts. It ensures sub-50ms latency, 7-year tamper-evident auditability, and PCI-DSS compliance on AWS within a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analysts: End users reviewing suspicious payments via case management.
- Payment Gateway: External client system submitting payment authorizations.
- API Gateway / Payment Gateway Integration Container: AWS ECS (Fargate) handling HTTPS/TLS 1.3 and OpenAPI/AsyncAPI ingress.
- Tokenization/Masking Proxy Container: AWS ECS (Fargate) protecting cardholder data.
- Real-Time Scoring Engine Container: AWS ECS (Fargate) executing fraud models via gRPC/REST.
- Case Management Container: AWS ECS (Fargate) managing analyst reviews via HTTPS/TLS 1.3.
- Model & Rule Registry Service Container: AWS ECS (Fargate) for zero-downtime rule updates.
- Audit & Compliance Container: AWS ECS (Fargate) managing secure audit logs.
- Amazon Aurora: Relational database cluster for case management and review data storage.
- Amazon RDS Proxy: Connection pooler for ECS Fargate to Aurora.
- Amazon ElastiCache (Redis): In-memory cache for fast scoring and fallback.
- Amazon SQS / SNS: Asynchronous messaging infrastructure.
- Amazon S3 Object Lock: Tamper-evident, long-term storage for 7-year audit retention.

## Relationships
- Payment Gateway -> API Gateway / Payment Gateway Integration Container: Submits payment authorization requests [HTTPS / TLS 1.3].
- API Gateway / Payment Gateway Integration Container -> Tokenization/Masking Proxy Container: Tokenizes card data [gRPC].
- API Gateway / Payment Gateway Integration Container -> Real-Time Scoring Engine Container: Requests fraud score [gRPC].
- Real-Time Scoring Engine Container -> Amazon ElastiCache (Redis): Retrieves cached rules and model weights [RESP].
- Case Management Container -> Amazon RDS Proxy: Queries and mutates case data [SQL].
- Amazon RDS Proxy -> Amazon Aurora: Forwards pooled database connections [SQL].
- Case Management Container -> Amazon S3 Object Lock: Archives historical audit logs [HTTPS].

## Technology Stack
- Cloud Provider: AWS (eu-west-1 region) to ensure reliable regional compliance infrastructure.
- Compute: AWS ECS with Fargate for serverless container orchestration, fitting the 3-engineer team size.
- Database: Amazon Aurora Serverless v2 with Aurora Read Replica for automated scaling and read-write segregation.
- Connection Management: Amazon RDS Proxy to prevent connection exhaustion from Fargate scaling.
- Caching: Amazon ElastiCache (Redis) for low-latency rule lookups meeting P99 performance targets.
- Storage & Compliance: Amazon S3 Object Lock for immutable 7-year audit data retention (R-06).
- Security & Encryption: AWS KMS with customer-managed keys for PCI-DSS compliance and IAM database authentication.
- Infrastructure & Migrations: Terraform/AWS CDK for IaC and Flyway/Liquibase for automated zero-downtime database migrations.

## Rationale
The architecture combines AWS ECS Fargate and Aurora Serverless v2 to minimize operational overhead for a 3-engineer team while easily meeting the 25,000 EUR monthly budget. Dedicated components like RDS Proxy, ElastiCache, and S3 Object Lock guarantee high availability, sub-50ms latency, and strict PCI-DSS Level 1 compliance.