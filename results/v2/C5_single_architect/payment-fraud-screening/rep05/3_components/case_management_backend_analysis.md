## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in AWS (eu-west-1) to prevent fraud and manage suspicious cases. It achieves sub-50ms P99 latency at 3,000 requests/sec while maintaining PCI-DSS Level 1 compliance and strict auditability.

## Key Elements
- Fraud Analyst (Person)
- Payment Gateway / Acquirer (External System)
- Card Networks & Fraud Intelligence Feeds (External System)
- Archival / Compliance Storage (External System)
- AWS Network Load Balancer (AWS NLB)
- Fraud Scoring Engine (Amazon ECS on AWS Fargate)
- Case Management Backend (Amazon ECS on AWS Fargate)
- Amazon Aurora PostgreSQL (Database)
- Redis (Cache)
- Amazon S3 with Object Lock and AWS KMS (Storage)
- API Router / Controller (Component)
- Masking & Sanitization Middleware (Component)
- Case Service (Component)
- Audit Logger (Component)
- Data Repository (Component)

## Relationships
- Fraud Analyst -> Case Management Backend: Accesses case management features [HTTPS]
- API Router -> Masking Middleware: Sanitizes incoming requests [In-Process]
- Masking Middleware -> Case Service: Forwards clean payload [In-Process]
- API Router -> Case Service: Method calls [In-Process]
- Case Service -> Data Repository: Reads/Writes case state [SQL over TCP]
- Case Service -> Audit Logger: Emits audit events [In-Process]
- Case Management Backend -> Amazon Aurora PostgreSQL: Reads and writes transactional case management data [TCP]
- Case Management Backend -> Amazon S3 with Object Lock and AWS KMS: Streams audit logs [AWS SDK]

## Technology Stack
- Go / Rust: Powers the Fraud Scoring Engine and Case Management Backend containers for high throughput and low resource usage.
- Amazon ECS on AWS Fargate: Container orchestration matching the 3-engineer team constraint and fixed budget.
- Amazon Aurora PostgreSQL: Managed relational database for transactional case management data.
- Redis: Fast in-memory cache supporting high-performance scoring lookups.
- Amazon S3 with Object Lock and AWS KMS: Tamper-evident storage for 7-year audit requirements.

## Rationale
This architecture utilizes serverless containers and managed AWS services to minimize operational overhead for a three-engineer team within a fixed 25,000 EUR monthly budget. Furthermore, it incorporates strict isolation, tokenization, and object-locked storage to fulfill rigorous PCI-DSS Level 1 compliance and 7-year tamper-evident audit mandates.