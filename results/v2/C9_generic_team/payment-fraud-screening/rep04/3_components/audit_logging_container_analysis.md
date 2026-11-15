## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages suspicious cases. It ensures secure, auditable, and sub-50ms fraud decisions within strict PCI-DSS compliance boundaries.

## Key Elements
- Fraud Analysts: End users reviewing suspicious payments via case management.
- Payment Gateway: External system submitting card-not-present authorizations.
- API Gateway / Ingress Container: Entry point utilizing OpenAPI and JSON Schema.
- Real-Time Scoring Container: Core scoring engine operating in AWS (eu-west-1) via gRPC/REST.
- Audit Logging Container: Lightweight validation proxy utilizing AWS Kinesis Data Firehose and Amazon S3 Object Lock.
- Case Management Container: Workflow engine for analyst reviews hosted on AWS.
- Amazon S3: Secure object storage with Object Lock enabled in compliance mode for 7-year retention.
- AWS Kinesis Data Firehose: Managed ingestion service buffering data to S3.
- AWS SQS / Kinesis: Message bus and event streaming infrastructure.
- AWS Secrets Manager / Parameter Store: Secret and configuration management.

## Relationships
- Payment Gateway -> API Gateway / Ingress Container: Submits authorization requests [HTTPS / JSON]
- API Gateway / Ingress Container -> Real-Time Scoring Container: Forwards authorization payloads [gRPC]
- Real-Time Scoring Container -> Audit Logging Container: Dispatches decision events asynchronously with a 15ms write timeout [HTTP/REST or internal IPC]
- Audit Logging Container -> AWS Kinesis Data Firehose: Pushes validated and cryptographically hashed audit batches [AWS API]
- AWS Kinesis Data Firehose -> Amazon S3: Persists WORM-compliant audit logs with S3 Object Lock [AWS Storage API]
- Fraud Analysts -> Case Management Container: Reviews flagged transactions and updates case statuses [HTTPS]

## Technology Stack
- AWS (eu-west-1): Chosen cloud provider and region to maintain low latency and data residency requirements.
- Amazon S3 Object Lock: Enforces WORM storage to guarantee tamper-evident 7-year audit retention (R-06).
- AWS Kinesis Data Firehose: Offloads custom ingestion and batching to managed infrastructure, minimizing operational overhead for a 3-person team.
- JSON Schema & SHA-256: Used for payload validation and cryptographic checksum generation to ensure audit integrity.
- Embedded Append-Only Log: Provides local memory-mapped file buffering during transient network partitions to preserve availability (R-07).

## Rationale
This architecture leverages fully managed AWS services to minimize operational toil for a three-engineer team while strictly adhering to the 25,000 EUR monthly budget constraint. Asynchronous non-blocking logging with localized buffering ensures sub-50ms decision latency and high availability without compromising rigorous PCI-DSS auditability.