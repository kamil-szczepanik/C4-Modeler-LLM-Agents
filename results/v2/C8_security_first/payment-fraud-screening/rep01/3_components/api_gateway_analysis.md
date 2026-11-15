## Overview
- Real-Time Payment Fraud Screening system evaluating card-not-present payment authorizations for a mid-size payment processor.
- Screens transactions for fraud, manages analyst review cases, and ensures PCI-DSS Level 1 compliance with sub-50ms P99 latency.

## Key Elements
- Payment Gateway / Acquirer (External System)
- Fraud Analyst & Risk Manager (Users)
- Corporate IdP (External System)
- AWS API Gateway (Container - HTTP APIs)
- Scoring Engine Container (Container - Amazon ECS on AWS Fargate)
- Case Management Container (Container - Amazon ECS on AWS Fargate)
- Amazon S3 WORM Bucket (Container - Amazon S3 with Object Lock)
- Amazon Kinesis Data Firehose (Container)

## Relationships
- Payment Gateway / Acquirer -> AWS API Gateway: Sends payment authorization requests [mTLS]
- Fraud Analyst & Risk Manager -> AWS API Gateway: Accesses Case Management UI [HTTPS via ALB]
- AWS API Gateway -> Scoring Engine Container: Routes authorization scoring requests [/v1/authorize via gRPC over HTTP/2]
- AWS API Gateway -> Case Management Container: Routes analyst management requests [/v1/cases via HTTPS]
- AWS API Gateway -> Amazon Kinesis Data Firehose: Streams compressed access logs for auditability [AWS Native Integration]
- Amazon Kinesis Data Firehose -> Amazon S3 WORM Bucket: Persists tamper-evident transaction logs for 7 years [AWS Native Integration]

## Technology Stack
- AWS API Gateway (HTTP APIs): Manages ingress, TLS termination, and path segregation with minimal operational overhead.
- Amazon ECS on AWS Fargate: Runs stateless scoring and case management containers, matching the 3-engineer team capacity.
- Amazon Kinesis Data Firehose: Provides batching and compression for zero-code telemetry without Lambda latency on the critical path.
- Amazon S3 WORM Bucket (Object Lock): Implements tamper-evident storage to meet the 7-year audit retention constraint.

## Rationale
- Managed AWS services minimize operational complexity, allowing a 3-engineer team to maintain the platform within the 25,000 EUR monthly budget.
- Path segregation and native API Gateway integrations protect the sub-50ms P99 latency threshold for 3,000 req/s while satisfying PCI-DSS and audit mandates.