## Overview
The Customer Privacy/Compliance Service is a distributed microservice designed to ensure strict GDPR and CCPA compliance for the Online Bookstore. It securely handles user consent, data portability, and cryptographic deletion workflows across multiple AWS regions.

## Key Elements
- Consent & Preference Controller: Manages opt-ins/opt-outs and self-service privacy portal APIs.
- Data Erasure & Anonymization Engine: Executes distributed saga patterns via Amazon SQS for data deletion.
- Data Export Handler: Aggregates customer data and generates secure Amazon S3 export packages.
- Compliance Audit Logger: Records immutable regulatory audit trails in Amazon DynamoDB.
- Infrastructure: Amazon ECS Fargate, AWS App Mesh, Amazon Aurora PostgreSQL, and Amazon DynamoDB.

## Relationships
- React SPA to Amazon API Gateway: Exposes privacy endpoints via gRPC-Web/gRPC over HTTP/2.
- API Gateway to Customer Privacy/Compliance Service: Routes gRPC requests secured via mTLS and AWS App Mesh.
- Data Erasure Engine to Amazon SQS: Publishes and consumes asynchronous deletion and saga events.
- Compliance Controllers to Amazon Aurora PostgreSQL & DynamoDB: Manages state using standard database drivers with AWS KMS encryption.

## Technology Stack
- Amazon ECS Fargate: Provides scalable, serverless container hosting across multi-region AWS deployments.
- AWS App Mesh & mTLS: Ensures zero-trust inter-service communication and distributed tracing via AWS X-Ray.
- Amazon SQS & DLQs: Decouples asynchronous compliance workflows and handles poison-pill retries.
- AWS KMS & AES-256: Enforces data-at-rest encryption and cryptographic erasure for PII protection.

## Rationale
This architecture ensures 99.95% uptime and high scalability while strictly satisfying GDPR and CCPA data residency mandates across regions. Decoupled asynchronous messaging guarantees reliable compliance request fulfillment without impacting core checkout performance.