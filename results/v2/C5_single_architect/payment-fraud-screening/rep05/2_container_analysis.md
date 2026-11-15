## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage suspicious cases. It delivers sub-50ms decisions at 3,000 TPS while ensuring PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Fraud Analyst (User)
- Payment Gateway / Acquirer (External System)
- Card Networks & Fraud Intelligence Feeds (External System)
- Archival / Compliance Storage (External System)
- AWS Network Load Balancer (Ingress)
- Fraud Scoring Engine (Container)
- Case Management Backend (Container)
- Amazon Aurora PostgreSQL (Data Tier)
- Amazon S3 with Object Lock and AWS KMS (Audit Tier)

## Relationships
- Payment Gateway calls AWS Network Load Balancer via HTTPS/TCP at 3,000 TPS.
- AWS Network Load Balancer routes requests to Fraud Scoring Engine via TCP.
- Fraud Scoring Engine queries Amazon Aurora PostgreSQL and Redis via TCP.
- Fraud Analyst accesses Case Management Backend via HTTPS.
- Case Management Backend reads/writes to Amazon Aurora PostgreSQL via TCP.
- Fraud Scoring Engine and Case Management Backend stream audit logs to Amazon S3 via AWS SDK.

## Technology Stack
- AWS Network Load Balancer: Low-latency ingress routing without API Gateway overhead.
- Go or Rust: High-performance backend language to guarantee P99 latency below 50 ms.
- Amazon ECS on AWS Fargate: Container orchestration minimizing operational overhead for a 3-engineer team.
- Redis: In-memory store for low-latency feature lookup.
- Amazon Aurora PostgreSQL: Relational database for transactional case management data.
- Amazon S3 with Object Lock and AWS KMS: Immutable, tamper-evident storage for 7-year compliance audit logs.

## Rationale
This architecture leverages managed AWS services to minimize operational burden for a three-engineer team while staying within the 25,000 EUR monthly budget. High-performance containers and load balancing meet the strict sub-50ms latency requirement at 3,000 TPS.