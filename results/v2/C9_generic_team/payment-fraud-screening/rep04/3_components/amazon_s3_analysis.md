## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations for a mid-size payment processor. It securely evaluates transactions, manages suspicious payment cases, and maintains tamper-evident audit records.

## Key Elements
* Fraud Analysts
* Payment Gateway
* API Gateway / Ingress Container
* Real-Time Scoring Container
* Audit Logging Container
* Case Management Container
* Amazon S3 (with Object Lock, Versioning, and SSE-KMS)
* AWS SQS / Kinesis
* AWS Secrets Manager / Parameter Store

## Relationships
* API Gateway / Ingress Container -> Real-Time Scoring Container: Routes authorization requests via gRPC/REST
* Real-Time Scoring Container -> Amazon S3: Asynchronously downloads model artifacts from content-addressable storage (`s3://bucket/models/{model_id}/{sha256}/model.tar.gz`) via local caching sidecars
* Audit Logging Container -> Amazon S3: Writes tamper-evident audit logs via AWS VPC Gateway Endpoints with Object Lock enabled in compliance mode
* Audit Logging Container -> AWS SQS / Kinesis: Streams audit events for processing

## Technology Stack
* AWS (eu-west-1): Primary cloud provider selected for regional compliance and service availability
* Amazon S3 with Object Lock & Glacier: Provides 7-year tamper-evident WORM storage with automated lifecycle tiering
* Terraform / CloudFormation: Infrastructure as Code for repeatable, peer-reviewed infrastructure management
* Local Disk Spooling & DLX: Ensures graceful degradation and prevents log loss during transient S3 network failures

## Rationale
This architecture meets PCI-DSS Level 1 compliance and a 50 ms P99 latency threshold by decoupling real-time scoring from S3 runtime calls using local model caching. It satisfies strict 7-year audit requirements within a 25,000 EUR monthly budget through S3 lifecycle tiering, VPC endpoints, and automated operational verification suitable for a 3-engineer team.