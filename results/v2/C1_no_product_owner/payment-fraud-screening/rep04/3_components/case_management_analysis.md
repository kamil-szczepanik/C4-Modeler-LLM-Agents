## Overview
The Case Management container provides secure investigation and workflow tools for fraud analysts reviewing suspicious payment authorizations. It ensures PCI-DSS compliance and cryptographic auditability within strict budget and team constraints.

## Key Elements
- **Case API Controller**: NestJS-based entry point handling HTTPS/REST requests from analysts.
- **Masking Interceptor Component**: In-process middleware that sanitizes payloads and enforces R-05 data masking.
- **Case Workflow Engine**: Manages review states and consumes asynchronous messages from Amazon SQS.
- **Audit Logger Component**: Generates tamper-evident cryptographic signatures using AWS KMS and persists data to Amazon Aurora PostgreSQL.
- **Infrastructure**: AWS Fargate (ECS), AWS Secrets Manager, and Amazon CloudWatch.

## Relationships
- **Fraud Analyst** -> **Case API Controller**: Manages cases via HTTPS/REST [JSON, OIDC/OAuth2, TLS 1.3].
- **Case API Controller** -> **Masking Interceptor Component**: Sanitizes payloads [In-process].
- **Case Workflow Engine** -> **Amazon SQS**: Consumes review-routed events [HTTPS/SQS Protocol].
- **Case Workflow Engine** -> **Amazon Aurora PostgreSQL**: Persists case states and audit logs [TLS/JDBC].
- **Audit Logger Component** -> **AWS KMS**: Generates cryptographic signatures [AWS SDK / TLS].

## Technology Stack
- **NestJS (Node.js/TypeScript)**: Chosen for rapid feature development and modular architecture suitable for a 3-engineer team.
- **Amazon SQS**: Replaces Kafka to provide scale-to-zero queueing and eliminate cluster management overhead.
- **Amazon Aurora PostgreSQL & AWS KMS**: Provides secure relational storage and cryptographic audit trails to meet 7-year compliance (R-06).
- **AWS Fargate**: Container execution platform eliminating OS patching overhead within a 25,000 EUR monthly budget.
- **AWS Secrets Manager**: Injects rotating runtime secrets securely into task definitions.

## Rationale
This serverless component architecture minimizes operational toil for a three-person team by leveraging fully managed AWS services within budget. Cryptographic signing and strict payload masking fulfill rigorous PCI-DSS and 7-year audit requirements.