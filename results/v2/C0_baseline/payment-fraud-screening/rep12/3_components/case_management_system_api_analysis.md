## Overview
The Case Management System API provides backend services for fraud analysts to review suspicious transactions and execute overrides. It ensures strict PCI-DSS compliance and maintainable operations for a 3-engineer team within budget.

## Key Elements
* **Case Controller / Router**: Express-based routing layer handling HTTP requests and JWT authentication.
* **Masking & Security Interceptor**: Middleware layer stripping PANs and validating RBAC scopes.
* **Case Service**: Core domain logic managing case states, analyst assignments, and aggregated DTO payloads.
* **Audit & Compliance Logger**: Component dispatching batched audit payloads asynchronously.
* **Data Access Layer**: Interfacing with Amazon DynamoDB for persistence.

## Relationships
* **Case Controller** invokes **Case Service** via internal TypeScript interfaces.
* **Audit & Compliance Logger** dispatches payloads to **Amazon SQS** asynchronously using AWS SDK.
* **Data Access Layer** reads and writes encrypted data to **Amazon DynamoDB** using AWS KMS.

## Technology Stack
* **Node.js / Express on AWS ECS Fargate**: Selected for zero-patching operational overhead and containerized deployment.
* **Amazon DynamoDB**: Chosen for low-latency scalable persistence of case data.
* **Amazon SQS with KMS**: Used to decouple audit logging and guarantee tamper-evident S3 delivery.
* **AWS KMS**: Utilized for envelope encryption of persistent case data and SQS message encryption.

## Rationale
This architecture fits requirements by utilizing serverless containers (ECS Fargate) and managed AWS services to minimize operational toil for a 3-engineer team. It enforces robust security boundaries and async SQS buffering to maintain compliance and performance without exceeding budget.