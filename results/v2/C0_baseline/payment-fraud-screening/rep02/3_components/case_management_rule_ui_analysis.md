## Overview
The Case Management & Rule UI system enables fraud analysts to review suspicious transactions and risk managers to update fraud rules without downtime. It operates within a secure AWS cloud infrastructure while maintaining strict PCI-DSS compliance.

## Key Elements
* Fraud Analysts and Risk Operations Managers
* External Identity Provider
* API Router / BFF (Node.js / Express / tRPC)
* Case Management Service Component
* Rule Authoring & Validation Engine
* Audit Dispatcher Component
* Serverless Sandbox & Audit Lambda Functions
* Amazon DynamoDB
* Amazon SQS
* Amazon S3 with Object Lock

## Relationships
* Identity Provider -> API Router / BFF: User authentication [OIDC / HTTPS]
* Fraud Analysts and Risk Operations Managers -> API Router / BFF: Analyst reviews and rule management [HTTPS / TLS 1.3]
* Case Management Service -> Amazon DynamoDB: Reads and writes active case states [AWS SDK / TCP]
* Rule Authoring & Validation Engine -> Amazon SQS: Publishes validated rules [AWS SDK]
* Audit Dispatcher -> Amazon SQS: Forwards sanitized audit events [AWS SDK]
* Amazon SQS -> Serverless Audit Lambda: Asynchronous log processing [AWS Lambda Event Source]
* Serverless Audit Lambda -> Amazon S3 with Object Lock: Writes immutable audit logs [HTTPS]

## Technology Stack
* Node.js with TypeScript and Express/tRPC: Selected for the BFF and services to maximize development velocity for a 3-engineer team.
* Amazon DynamoDB: Chosen for low-latency active case state storage and real-time SLA metrics.
* Amazon SQS: Utilized for decoupled, asynchronous ingestion of rule updates and audit logs to prevent container blocking.
* AWS Lambda: Deployed for serverless execution of rule sandboxing and audit log persistence to minimize infrastructure management and IAM attack surface.
* Amazon S3 with Object Lock: Implemented to provide tamper-evident, 7-year audit log retention for compliance.

## Rationale
This architecture balances stringent PCI-DSS Level 1 security and 7-year auditability requirements with the resource constraints of a three-engineer team. Leveraging serverless components (AWS Lambda, SQS, S3 Object Lock) offloads operational overhead while guaranteeing high availability and tamper-proof compliance logging within budget.