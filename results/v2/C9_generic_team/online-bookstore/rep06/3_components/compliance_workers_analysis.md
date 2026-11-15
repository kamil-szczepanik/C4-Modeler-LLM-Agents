## Overview
The Compliance Workers container handles asynchronous GDPR and CCPA data anonymization, exports, and deletion requests for the Online Bookstore. It ensures regulatory adherence while protecting the core e-commerce platform's performance and availability.

## Key Elements
* Compliance Workers Container (Docker, Amazon ECS/EKS)
* Amazon SQS (Primary message queue and Dead Letter Queue)
* Amazon Aurora/RDS (Isolated database connection pool)
* Amazon S3 (Immutable compliance audit logs bucket)
* AWS Step Functions / Local State Tracking

## Relationships
* Compliance Workers -> Amazon SQS: Consumes compliance requests [SQS Protocol]
* Compliance Workers -> Amazon Aurora/RDS: Executes isolated batch data anonymization and deletions [Database Protocol]
* Compliance Workers -> Amazon S3: Emits immutable audit logs and data exports [HTTPS/S3 API]

## Technology Stack
* Docker & Amazon ECS/EKS: Enables horizontally autoscaled, stateless background workers based on SQS queue depth.
* AWS SQS & Dead Letter Queue (DLQ): Ensures reliable message delivery, retry backoff, and isolation of poisoned payloads.
* AWS Step Functions: Manages multi-step compliance request state machines (`Pending`, `Processing`, `Completed`, `Failed`).
* Dedicated DB Connection Pool (Bulkhead Pattern): Prevents heavy compliance queries from starving checkout and catalog traffic.

## Rationale
This decoupled, event-driven architecture prevents heavy compliance queries from degrading user-facing performance and uptime. Implementing idempotency, state machines, and isolated database pools ensures reliable, auditable, and secure handling of sensitive data regulations.