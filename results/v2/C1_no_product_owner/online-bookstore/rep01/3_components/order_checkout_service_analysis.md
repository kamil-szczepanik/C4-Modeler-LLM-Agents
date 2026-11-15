## Overview
The Order & Checkout Service processes customer transactions, payments, and fulfillment workflows for the Online Bookstore. It ensures secure, resilient, and compliant e-commerce operations across multiple global regions.

## Key Elements
- **Order API Controller**: Exposes gRPC endpoints for inbound requests.
- **Checkout Orchestrator**: Manages multi-step checkout sagas using AWS Step Functions.
- **Payment Client**: Integrates securely with external Payment Gateways via HTTPS.
- **Fulfillment Adapter**: Interfaces with third-party Shipping Provider APIs via HTTPS.
- **Order Repository**: Handles transactional persistence using Prisma ORM.

## Relationships
- **AWS API Gateway & ALB** -> **Order API Controller**: Routes incoming requests via App Mesh sidecars [gRPC over mTLS]
- **Order API Controller** -> **Checkout Orchestrator**: Delegates workflow execution [Internal method calls]
- **Checkout Orchestrator** -> **Payment Client** & **Fulfillment Adapter**: Executes external API calls [HTTPS/REST]
- **Checkout Orchestrator** -> **AWS Secrets Manager**: Fetches rotated API keys [AWS SDK/HTTPS]
- **Checkout Orchestrator** & **Order Repository** -> **Amazon Aurora PostgreSQL**: Persists saga state and order data [PostgreSQL Protocol via TLS]

## Technology Stack
- **Node.js / TypeScript**: Core runtime for service components ensuring rapid execution.
- **AWS ECS Fargate**: Serverless container hosting for reliable scalability.
- **AWS Step Functions**: Managed durable workflow engine for resilient saga orchestration without self-hosted infrastructure.
- **Prisma ORM**: Type-safe database toolkit for transactional persistence.
- **Amazon Aurora PostgreSQL**: Multi-region relational data store providing strong consistency and ACID guarantees.
- **AWS KMS**: Provides envelope encryption for PII and workflow state data.

## Rationale
AWS Step Functions and serverless containers eliminate operational toil while meeting the 99.95% uptime requirement. Native IAM integration, KMS encryption, and tokenized payment flows ensure strict GDPR, CCPA, and OWASP security compliance.