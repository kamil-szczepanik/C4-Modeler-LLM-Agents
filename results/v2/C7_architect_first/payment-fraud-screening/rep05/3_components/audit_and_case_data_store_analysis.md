## Overview
This system provides real-time payment fraud screening for a mid-size payment processor, analyzing card-not-present authorizations to approve, decline, or flag transactions. It empowers fraud analysts with a case management interface while ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
* **Real-Time Scoring Service**: Go-based container running on AWS ECS Fargate for low-latency fraud evaluation.
* **Case Management Backend**: Node.js/TypeScript container on AWS ECS Fargate managing analyst workflows.
* **Audit and Case Data Store**: Amazon Aurora PostgreSQL container housing transactional, audit, and case schemas.
* **Feature Cache**: Amazon DynamoDB for fast feature retrieval during scoring.
* **Audit Storage**: Amazon S3 with Object Lock for 7-year immutable audit retention.
* **Messaging & Event Bus**: Amazon SQS and SNS for asynchronous event handling and fallback buffering.
* **Security & Infrastructure**: AWS KMS for customer-managed encryption keys, AWS IAM for database authentication, and AWS Lambda for batch data exports.

## Relationships
* **API Gateway & Fallback Layer -> Real-Time Scoring Service**: Routes authorization requests via HTTPS/443.
* **Real-Time Scoring Service -> Audit and Case Data Store**: Writes immutable decision logs via PostgreSQL wire protocol [TCP/5432] over VPC endpoints.
* **Case Management Backend -> Audit and Case Data Store (Read Replica)**: Executes read-heavy analyst queries via PostgreSQL wire protocol [TCP/5432] with PgBouncer connection pooling.
* **Audit and Case Data Store -> Audit Storage**: Exports partitioned audit logs via scheduled AWS Lambda functions [HTTPS/443] to S3 Object Lock.
* **Real-Time Scoring Service -> Messaging & Event Bus**: Buffers audit writes to Amazon SQS during database latency spikes.

## Technology Stack
* **AWS ECS Fargate**: Serverless container orchestration for lightweight operation by a 3-engineer team.
* **Amazon Aurora PostgreSQL**: Relational data store providing ACID compliance, row-level security, and point-in-time recovery.
* **Amazon DynamoDB**: Key-value cache chosen for sub-millisecond feature lookup performance.
* **Amazon S3 Object Lock**: Compliant Write-Once-Read-Many (WORM) storage satisfying the 7-year retention mandate.
* **Go & Node.js/TypeScript**: High-performance runtime for scoring services and scalable backend logic.

## Rationale
This architecture uses serverless AWS containers and managed databases to maintain low operational overhead for a three-engineer team within a €25,000 monthly budget. Strict read-replica scaling, local SQS buffering, and cryptographic audit chains ensure strict PCI-DSS compliance, sub-50-millisecond scoring latencies, and 7-year tamper-evident auditability.