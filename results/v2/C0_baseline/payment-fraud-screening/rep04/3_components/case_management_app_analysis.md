## Overview
[The Case Management App enables fraud analysts and compliance officers to review suspicious payment transactions, manage cases, and execute audit checks. It balances rapid analyst workflows with strict PCI-DSS Level 1 compliance and a €25k/month AWS budget constraint.]

## Key Elements
- Fraud Analyst
- Risk / Compliance Officer
- Case API Controller (TypeScript / NestJS)
- Case Orchestrator Service (TypeScript)
- Audit & Evidence Proxy (TypeScript)
- Feedback & Telemetry Emitter (TypeScript)
- Case & Audit Read Store (Amazon DynamoDB)
- Audit Storage (Amazon S3 with Object Lock)
- Audit & Streaming Pipeline (Amazon Kinesis Data Streams / Firehose)
- Identity Provider / IdP (OIDC/OAuth2)

## Relationships
- Fraud Analyst -> Case API Controller: Reviews cases and manages screening workflows [HTTPS / mTLS]
- Compliance Officer -> Case API Controller: Inspects audit trails and logs read-only [HTTPS / mTLS]
- Case API Controller -> Case Orchestrator Service: Dispatches workflow commands [In-memory function calls]
- Case Orchestrator Service -> Case & Audit Read Store: Reads and updates case state [HTTPS / AWS SDK via VPC Endpoints]
- Audit & Evidence Proxy -> Case & Audit Read Store: Queries tamper-evident decision logs and model explanations [HTTPS / AWS SDK via VPC Endpoints]
- Feedback & Telemetry Emitter -> Audit & Streaming Pipeline: Streams analyst feedback tags for offline model retraining [HTTPS / Kinesis API]

## Technology Stack
- Node.js & TypeScript / NestJS: Chosen for rapid UI-driven feature delivery and low operational overhead for a three-person engineering team.
- Amazon ECS Fargate: Container orchestration platform ensuring zero server management within the fixed infrastructure budget.
- Amazon DynamoDB: Indexed read store for fast, secure audit retrieval and case caching without direct S3 query overhead.
- Zod / class-validator: Strict schema validation library for input sanitization and preventing injection vulnerabilities in the analyst UI.
- AWS Secrets Manager: Secure runtime storage and automatic rotation for IdP tokens and database connection strings.

## Rationale
[This architecture fits the requirements by utilizing serverless and managed AWS services to minimize operational toil for a three-person team while enforcing robust security, RBAC/ABAC controls, and tamper-evident auditing. Decoupling audit queries via DynamoDB and routing telemetry through resilient pipelines ensures sub-second analyst workflows remain uninterrupted and compliant with PCI-DSS Level 1.]