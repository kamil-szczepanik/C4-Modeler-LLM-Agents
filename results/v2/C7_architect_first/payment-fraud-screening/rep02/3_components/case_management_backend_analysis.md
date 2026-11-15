## Overview
The Case Management Backend is an event-driven, secure service powering analyst reviews for the Real-Time Payment Fraud Screening system. It provides real-time case handling, strict audit logging, and role-based access control while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- **API Router / Controller (Express.js):** Manages incoming HTTPS REST requests and JWT validation.
- **Case Service (TypeScript):** Handles domain business logic, case lifecycles, and WebSockets.
- **Audit Logger Component (TypeScript):** Asynchronously processes tamper-evident audit records.
- **Metrics & Telemetry Collector (OpenTelemetry):** Captures operational SLAs and review turnaround times.
- **Data Access Layer (AWS SDK v3):** Enforces data masking and tokenization against databases.
- **Infrastructure (AWS):** Amazon ECS Fargate, Amazon SQS FIFO (with DLQ), Amazon DynamoDB, and Amazon Aurora PostgreSQL ledger tables.

## Relationships
- **Fraud Analyst UI** -> **API Router / Controller**: HTTPS / REST and WebSockets
- **API Router / Controller** -> **Case Service**: In-process function calls
- **Case Service** -> **Metrics & Telemetry Collector**: In-process telemetry calls
- **Case Service** -> **Data Access Layer**: Reads/writes hot cases [DynamoDB SDK]
- **Audit Logger Component** -> **Amazon SQS FIFO Queue**: Publishes audit events [HTTPS / SigV4]
- **Amazon SQS FIFO Queue** -> **Data Access Layer**: Batched consumption [Aurora SDK]
- **Case Management Backend** -> **AWS Services (DynamoDB, SQS, Aurora)**: Interface VPC Endpoints

## Technology Stack
- **Node.js / TypeScript / Express.js:** Selected for rapid feature development by a three-engineer team.
- **Amazon ECS Fargate:** Provides serverless container orchestration within the €25,000/month budget.
- **Amazon SQS FIFO with DLQ:** Guarantees ordered, reliable, and retriable audit event dispatching.
- **Amazon Aurora PostgreSQL Ledger Tables:** Ensures tamper-evident, 7-year auditable storage for compliance.
- **AWS Cognito & KMS:** Secures user identity, RBAC, and encryption-at-rest with customer-managed keys.

## Rationale
This architecture balances strict regulatory constraints like PCI-DSS Level 1 and 7-year auditability with the operational realities of a three-engineer team. Asynchronous queuing and serverless containers maximize system reliability, data security, and cost efficiency.