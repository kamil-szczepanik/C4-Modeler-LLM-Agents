## Overview
[The Real-Time Payment Fraud Screening Platform screens card-not-present payment authorizations for fraud and manages suspicious cases. It ensures secure, low-latency decision-making while meeting strict compliance and audit requirements.]

## Key Elements
* [Scoring Engine Container (Go, ONNX runtime, Amazon ECS on AWS Fargate)]
* [Case Management Container (Next.js / Node.js, Amazon ECS on AWS Fargate)]
* [Amazon SQS Case Queue (Standard/FIFO)]
* [EventBridge Audit Bus (Custom Event Bus with Archive and Replay)]
* [Amazon S3 WORM Bucket & Data Lake]
* [AWS KMS Customer Managed Keys (CMK)]

## Relationships
* [Scoring Engine Container -> SQS Case Queue: SendMessage [AWS SDK / HTTPS]]
* [SQS Case Queue -> Case Management Container: ReceiveMessage [AWS SDK / HTTPS]]
* [Scoring Engine Container -> EventBridge Audit Bus: PutEvents [AWS SDK / HTTPS]]
* [EventBridge Audit Bus -> Amazon Athena & S3 Data Lake: Firehose / S3 Target [AWS Native / HTTPS]]

## Technology Stack
* [Amazon ECS on AWS Fargate: Provides serverless container orchestration to minimize infrastructure management for a 3-engineer team.]
* [Amazon SQS: Handles asynchronous, point-to-point case queuing with Dead Letter Queues to guarantee at-least-once delivery.]
* [Amazon EventBridge: Manages fan-out event distribution and immutable 7-year audit logging via Archive and Replay.]
* [AWS KMS CMK: Enforces strong at-rest encryption to satisfy PCI-DSS Level 1 compliance requirements.]

## Rationale
[This architecture decouples synchronous, low-latency scoring from heavy asynchronous auditing to meet the P99 <50ms performance requirement. Furthermore, leveraging fully managed AWS services keeps operational overhead minimal for a three-engineer team within the 25,000 EUR monthly budget.]