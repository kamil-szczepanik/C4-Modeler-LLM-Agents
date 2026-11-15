## Overview
The Case Management Service empowers fraud analysts to efficiently review suspicious payment authorizations while strictly maintaining PCI-DSS Level 1 compliance. It securely processes case workflows, guarantees 7-year tamper-evident auditability, and operates efficiently within fixed budget constraints.

## Key Elements
- **Case API Handler (FastAPI)**: Exposes REST/JSON endpoints and enforces strict RBAC and token masking.
- **Token Masking Filter**: Programmatically strips and masks card details at the serialization boundary.
- **Case Workflow Engine**: Manages payment review states (Pending, Approved, Declined).
- **Encryption Middleware**: Enforces client-side envelope encryption via AWS KMS.
- **Audit Trail Emitter**: Formats, cryptographically signs, and emits immutable action logs.
- **SQS DLQ**: Decouples audit logging to ensure uninterrupted analyst workflows.

## Relationships
- **Amazon API / Application Load Balancer (ALB)** -> **Case API Handler**: Routes case management requests [gRPC over mTLS].
- **Case API Handler** -> **Token Masking Filter** -> **Case Workflow Engine**: Passes sanitized case data [In-memory Python objects].
- **Case Workflow Engine** -> **Encryption Middleware** -> **Amazon DynamoDB**: Persists encrypted case states [AWS SDK over TLS, port 443].
- **Audit Trail Emitter** -> **SQS DLQ** -> **Amazon QLDB**: Asynchronously flushes tamper-evident audit logs [AWS SDK over TLS, port 443].

## Technology Stack
- **Python (FastAPI)**: Chosen for rapid development and robust data-handling libraries suitable for a 3-person engineering team.
- **AWS ECS Fargate**: Provides serverless container orchestration with blue/green deployments for zero-downtime updates.
- **Amazon QLDB & S3 Glacier Deep Archive**: Ensures tamper-evident, cost-effective 7-year audit log retention.
- **AWS KMS**: Manages customer-managed keys for column-level encryption and asymmetric audit event signing.

## Rationale
This architecture uses serverless AWS containers and managed databases to minimize operational overhead for a three-person engineering team within a strict €25k monthly budget. It strictly enforces PCI-DSS Level 1 and 7-year audit constraints via robust encryption, token masking, and immutable cryptographic logging.