## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS, while providing case management and audit tools for compliance officers and fraud analysts. It is operated by a three-engineer team on AWS within a 25,000 EUR monthly budget, maintaining PCI-DSS Level 1 compliance.

## Key Elements
* **Fraud Analyst & Compliance Officer**: Internal users reviewing suspicious transactions and auditing historical decisions.
* **Merchant Operations Manager & End-Customer**: Secondary business stakeholders monitoring false positives and ensuring transaction privacy.
* **API Gateway / Ingress**: AWS API Gateway with mTLS via AWS ACM Private CA and circuit breaking.
* **Fraud Screening Engine**: Containerized stateless service (Go/Rust) running on Amazon ECS on EC2.
* **Case Management & Reporting Backend**: FastAPI Python service backed by an Amazon React SPA frontend on CloudFront/S3, integrating Amazon Athena for compliance queries.
* **Audit & Compliance Worker**: Asynchronous Python worker processing events via Amazon SQS and writing to AWS S3 Object Lock.
* **Data & Secret Stores**: Amazon ElastiCache for Redis, AWS Secrets Manager, and Amazon ECR.

## Relationships
* **Merchant / Payment Gateway** -> **AWS API Gateway**: Forwards authorization requests using HTTPS/REST.
* **AWS API Gateway** -> **Fraud Screening Engine**: Invokes real-time scoring using mTLS over private VPC subnets.
* **Fraud Screening Engine** <-> **Amazon ElastiCache for Redis**: Queries cached features in-memory for low-latency scoring.
* **Fraud Screening Engine** -> **Amazon SQS**: Publishes decision events asynchronously.
* **Amazon SQS** -> **Audit & Compliance Worker**: Delivers decision payloads for tamper-evident logging.
* **Audit & Compliance Worker** -> **AWS S3 Object Lock**: Stores cryptographically signed audit logs (HMAC-SHA256 via AWS KMS).
* **Case Management Backend** -> **Amazon Athena**: Queries historical audit logs for compliance and merchant reporting.

## Technology Stack
* **Compute & Orchestration**: Amazon ECS on EC2 with pre-warmed instances and AWS CodeDeploy for blue/green deployments to ensure predictable <50ms P99 latency.
* **Languages & Frameworks**: Go or Rust for the high-throughput screening engine; Python FastAPI for the case management backend.
* **Storage & Security**: Amazon ElastiCache for Redis (Multi-AZ), AWS S3 Object Lock for 7-year tamper-evident audit retention, AWS KMS for encryption and cryptographic signing, and AWS Secrets Manager for dynamic credentials.
* **Analytics & Observability**: Amazon Athena for serverless compliance queries; Amazon CloudWatch, AWS X-Ray, and Prometheus/Grafana for monitoring and distributed tracing.

## Rationale
This architecture uses managed AWS services and containerization on EC2 to achieve sub-50ms latency at high throughput within a fixed 25,000 EUR budget. It minimizes operational overhead for a three-person engineering team while strictly enforcing PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail.