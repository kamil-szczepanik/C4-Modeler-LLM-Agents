## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations under 50 ms while ensuring PCI-DSS Level 1 compliance and immutable auditability. It uses a cloud-native architecture on AWS to score transactions, manage fraud analyst reviews, and maintain strict operational visibility within a 25,000 EUR monthly budget.

## Key Elements
- Fraud Analyst (Person)
- Merchant / Payment Gateway (External System)
- AWS API Gateway (Container)
- Scoring Engine: AWS Lambda with Provisioned Concurrency, Go runtime (Container)
- Case Management: Node.js / React on ECS Fargate (Container)
- Data Layer: Amazon Aurora Serverless v2 PostgreSQL (Container)
- Async Messaging: AWS SQS (Container)
- Observability: AWS X-Ray, Amazon CloudWatch, Amazon SNS, S3 Object Lock (Container)
- Identity Provider - IdP (External System)
- AWS KMS / S3 Object Lock (External System)

## Relationships
- Merchant / Payment Gateway -> AWS API Gateway: Submits authorization requests [HTTPS / JSON]
- AWS API Gateway -> Scoring Engine: Invokes real-time fraud scoring [gRPC / AWS Lambda API]
- Scoring Engine -> Data Layer: Queries scoring models and rules [PostgreSQL Protocol / TLS 1.3]
- Scoring Engine -> Async Messaging: Queues suspicious payments for review [AWS SQS API]
- Case Management -> Data Layer: Manages review cases and analyst actions [PostgreSQL Protocol / TLS 1.3]
- Scoring Engine & Case Management -> Observability: Sends sanitized telemetry, traces, and logs [AWS X-Ray SDK, CloudWatch Agent / TLS 1.3]
- Observability -> S3 Object Lock: Exports audit logs for tamper-evident 7-year storage [AWS S3 API / TLS 1.3]

## Technology Stack
- AWS Lambda & Go: Chosen for Scoring Engine to guarantee P99 latency under 50 ms at high throughput.
- Amazon Aurora Serverless v2 PostgreSQL: Provides auto-scaling relational data storage within budget constraints.
- AWS X-Ray & Amazon CloudWatch: Delivers distributed tracing, infrastructure metrics, and the Fraud Operations View.
- Amazon S3 Object Lock: Ensures 7-year tamper-evident WORM storage for PCI-DSS audit compliance.
- AWS KMS: Encrypts all data at rest using Customer Managed Keys.

## Rationale
This serverless and managed container architecture scales dynamically to handle 3,000 TPS within a fixed 25,000 EUR monthly budget operated by three engineers. Fully managed AWS services minimize operational overhead while satisfying strict latency, PCI-DSS compliance, and immutable 7-year audit requirements.