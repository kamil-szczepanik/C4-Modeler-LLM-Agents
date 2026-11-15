## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for mid-size payment processors to prevent fraud and enable suspicious payment reviews. It ensures strict sub-50ms latency, compliance with PCI-DSS Level 1, and tamper-evident 7-year auditability.

## Key Elements
- Real-Time Scoring Engine (Go microservice on AWS ECS EC2)
- Case Management System Frontend (React SPA on S3 + CloudFront)
- Case Management System API (Node.js / Express API on ECS)
- Compliance Reporting Worker (AWS Lambda)
- Amazon SQS (Standard, FIFO, and Dead-Letter Queues)
- Amazon S3 with Object Lock
- Amazon DynamoDB
- Amazon API Gateway
- Amazon CloudWatch
- AWS KMS
- Payment Processor Systems / Acquirer (External)

## Relationships
- Payment Processor -> Amazon API Gateway: Forwards authorization requests [HTTPS / TLS 1.3]
- Amazon API Gateway -> Real-Time Scoring Engine: Routes scoring requests [HTTP/JSON over VPC internal network]
- Real-Time Scoring Engine -> Amazon SQS: Publishes asynchronous case and audit events [AWS SDK over TLS 1.3]
- Amazon SQS (Audit Queue) -> Compliance Reporting Worker: Invokes processing [AWS Lambda event source mapping]
- Compliance Reporting Worker -> Amazon S3 with Object Lock: Persists immutable audit records [AWS SDK over TLS 1.3]
- Fraud Analysts -> Case Management System Frontend: Reviews flagged cases [HTTPS / TLS 1.3]
- Case Management System API -> Amazon DynamoDB: Reads/writes case data [AWS SDK over TLS 1.3]

## Technology Stack
- **Compute:** AWS ECS (EC2 launch type) for low-latency microservices; AWS Lambda for serverless compliance reporting workers.
- **Frontend Storage & Delivery:** Amazon S3 combined with Amazon CloudFront for static asset hosting.
- **Database:** Amazon DynamoDB for low-latency case management storage.
- **Messaging & Buffering:** Amazon SQS (Standard, FIFO, and Dead-Letter Queues) for asynchronous event handling and fail-open resilience.
- **Audit Storage:** Amazon S3 with Object Lock for tamper-evident 7-year record retention.
- **Security & Encryption:** AWS KMS with Customer Managed Keys (CMKs) and TLS 1.3 enforcing data encryption at rest and in transit.
- **Monitoring:** Amazon CloudWatch for metrics, operational alarms, and logging.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational toil for a lean three-engineer team while easily respecting the 25,000 EUR monthly budget. Standardizing entirely on SQS instead of Kinesis ensures predictable scaling, strict audit sequencing via FIFO queues, and robust fail-open continuity under 1 minute.