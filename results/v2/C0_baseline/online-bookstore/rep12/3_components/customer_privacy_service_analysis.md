## Overview
The Customer Privacy Service ensures strict GDPR and CCPA compliance for the Online Bookstore by handling user data export, deletion, and audit logging. It operates securely within a distributed AWS cloud architecture spanning three regions.

## Key Elements
- **End Customers & Compliance Officers**: Primary users accessing privacy features and audit logs.
- **Privacy API Controller**: Node.js/Express component handling REST endpoints and RBAC/ABAC authorization.
- **GDPR/CCPA Workflow Engine**: Node.js/BullMQ engine orchestrating asynchronous tasks and DLQs.
- **Data Exporter Worker**: Node.js worker packaging PII into encrypted ZIP archives.
- **Audit & Retention Logger**: Node.js component writing compliance trails.
- **Amazon S3**: Storage for encrypted PII exports with 48-hour auto-deletion.
- **Amazon DynamoDB**: Global tables providing immutable audit storage and PITR.
- **Redis**: Secure broker for BullMQ job queues.
- **External Notification Service**: External system sending secure email alerts.

## Relationships
- **API Gateway** -> **Privacy API Controller**: Routes requests via [mTLS].
- **Privacy API Controller** -> **GDPR/CCPA Workflow Engine**: Enqueues jobs via [Redis/BullMQ].
- **GDPR/CCPA Workflow Engine** -> **Redis (BullMQ)**: Manages async queues via [TCP with TLS].
- **Data Exporter Worker** -> **Amazon S3**: Uploads encrypted archives via [AWS SDK / HTTPS].
- **Audit & Retention Logger** -> **Amazon DynamoDB**: Persists audit trails via [AWS SDK / HTTPS].
- **GDPR/CCPA Workflow Engine** -> **External Notification Service**: Dispatches alerts via [HTTPS / REST].

## Technology Stack
- **Node.js & Express**: Powers lightweight, scalable privacy microservices.
- **BullMQ & Redis**: Manages asynchronous workflows and job queues reliably.
- **Amazon S3**: Secures temporary PII exports with KMS CMK encryption and lifecycle rules.
- **Amazon DynamoDB Global Tables**: Ensures multi-region replication and immutable audit persistence.
- **AWS Secrets Manager**: Automatically rotates database and encryption credentials.

## Rationale
This decoupled, asynchronous architecture guarantees strict regulatory compliance and high scalability without impacting storefront performance. Encrypted storage, multi-region replication, and automated workflows fulfill stringent security and availability SLAs.