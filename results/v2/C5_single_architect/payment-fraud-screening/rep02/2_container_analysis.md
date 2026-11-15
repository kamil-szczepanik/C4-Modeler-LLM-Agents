## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in real time and provides a case management interface for fraud analysts. It is designed to meet strict PCI-DSS Level 1 compliance and sub-50ms latency requirements on AWS.

## Key Elements
* Fraud Analyst (Person)
* Payment Gateway / Core Processing Platform (External System)
* Identity Provider (External System)
* AWS Key Management Service (KMS) / HSM (External System)
* API Gateway / Application Load Balancer (Container)
* Fraud Scoring Engine service built in Go or Rust on AWS ECS Fargate (Container)
* Case Management Service built in Node.js/TypeScript on AWS ECS Fargate (Container)
* Amazon ElastiCache Redis for feature stores and rule caching (Container/Data Store)
* Amazon Aurora PostgreSQL for transactional case data and audit logs (Container/Data Store)
* Amazon S3 Immutable Vault with Object Lock in Compliance Mode (Container/Storage)
* Amazon SQS / SNS for asynchronous event publishing (Container/Messaging)

## Relationships
* Payment Gateway invokes API Gateway / ALB via HTTPS using TLS 1.3
* API Gateway calls Fraud Scoring Engine using gRPC over HTTP/2
* Fraud Scoring Engine reads/writes from ElastiCache Redis and queries Amazon Aurora PostgreSQL
* Fraud Scoring Engine publishes asynchronous events to Amazon SQS / SNS
* Case Management Service consumes from SQS, reads/writes to Aurora PostgreSQL, and archives to S3 Immutable Vault
* Fraud Analyst accesses Case Management Service via HTTPS authenticated through Identity Provider

## Technology Stack
* AWS ECS Fargate: Chosen for serverless simplicity and low operational overhead for a 3-engineer team within budget.
* Go or Rust: Selected for the Fraud Scoring Engine to guarantee sub-50ms P99 latency at 3,000 TPS.
* Node.js / TypeScript: Utilized for the Case Management Service for rapid development.
* Amazon Aurora PostgreSQL & S3 Immutable Vault: Implemented for tamper-evident, 7-year audit logging and transactional data.
* Amazon ElastiCache Redis: Deployed for sub-millisecond feature and rule retrieval.

## Rationale
This architecture uses managed AWS services on ECS Fargate to minimize operational overhead, fitting the constraints of a three-engineer team and a 25,000 EUR monthly budget. Furthermore, it combines gRPC communication, Redis caching, and immutable storage to reliably meet strict sub-50ms latency and 7-year auditability mandates.