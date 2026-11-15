## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at scale while providing analysts a secure case management interface. It ensures low-latency scoring, 7-year tamper-evident auditability, and PCI-DSS compliance on AWS.

## Key Elements
- Payment Gateway / Acquirer
- Card Networks & Fraud Intelligence Feeds
- Amazon NLB (Network Load Balancer)
- Fraud Scoring Engine (Go / Rust, Amazon ECS on AWS Fargate)
- Case Management Backend (Go / Rust, Amazon ECS on AWS Fargate)
- Amazon Aurora PostgreSQL
- Redis
- Amazon S3 with Object Lock and AWS KMS
  - S3 Bucket (Compliance Audit Store)
  - Key Management Service (Audit Encryption Key)
  - S3 Lifecycle Component
  - Bucket Policy & Access Controller
- Fraud Analyst

## Relationships
- Payment Gateway / Acquirer -> Amazon NLB: Forwards payment authorization requests [HTTPS / REST]
- Amazon NLB -> Fraud Scoring Engine: Routes authorization payloads [gRPC / TCP]
- Fraud Scoring Engine -> Redis: Performs ultra-low latency feature lookups [RESP / TCP]
- Fraud Scoring Engine -> Amazon Aurora PostgreSQL: Reads rules and writes scoring states [PostgreSQL wire protocol / TLS]
- Case Management Backend -> Amazon Aurora PostgreSQL: Manages analyst cases and reviews [PostgreSQL wire protocol / TLS]
- Fraud Analyst -> Case Management Backend: Reviews suspicious payments and updates cases [HTTPS / REST]
- Fraud Scoring Engine & Case Management Backend -> S3 Bucket (Compliance Audit Store): Writes immutable audit logs [HTTPS / AWS SDK via S3 Gateway VPC Endpoint]
- S3 Bucket -> Key Management Service (Audit Encryption Key): Encrypts/Decrypts payloads [AWS internal API via AWS KMS VPC Endpoint]

## Technology Stack
- AWS Fargate & Amazon ECS: Container execution for stateless scoring and case management, minimizing operational overhead for a 3-engineer team.
- Go / Rust: High-performance languages chosen to achieve sub-50ms P99 latency at 3,000 requests per second.
- Amazon Aurora PostgreSQL: Relational database for persistent case management and fraud rules storage.
- Redis: In-memory datastore for fast feature retrieval during real-time transaction scoring.
- Amazon S3 with Object Lock & AWS KMS: Immutable storage utilizing compliance mode and KMS envelope encryption to satisfy 7-year tamper-evident auditability.
- Amazon S3 Glacier: Cost-optimization tier for long-term audit log retention to stay within the 25,000 EUR monthly budget.

## Rationale
This architecture balances strict sub-50ms performance and PCI-DSS compliance requirements through serverless containerization and high-throughput memory stores. It controls operational costs via automated storage tiering while guaranteeing tamper-evident 7-year auditability.