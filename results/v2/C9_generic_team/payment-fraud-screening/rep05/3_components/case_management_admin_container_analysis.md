## Overview
The Case Management & Admin Container provides fraud analysts with tools to review suspicious payment authorizations and update rules. It ensures secure, compliant, and zero-downtime administration for the payment fraud screening system.

## Key Elements
- Case Management & Admin Container (AWS ECS on Fargate)
- Amazon Aurora Serverless
- AWS Systems Manager Parameter Store
- AWS SNS / SQS
- AWS X-Ray

## Relationships
- Case Management & Admin Container -> Amazon Aurora Serverless: Reads and writes audit data, cases, and outbox events via TLS
- Case Management & Admin Container -> AWS Systems Manager Parameter Store: Reads configuration via AWS API
- Case Management & Admin Container -> AWS SNS / SQS: Broadcasts rule updates and outbox notifications

## Technology Stack
- AWS ECS on Fargate: Selected for low operational overhead to fit the three-person engineering team and budget constraints.
- Amazon Aurora Serverless: Provides scalable relational storage for cases and audit logs.
- Flyway: Automates schema migrations during ECS task startup for zero-downtime deployments.
- AWS X-Ray: Enables centralized structured logging and distributed tracing with correlation IDs.

## Rationale
This architecture uses a modular monolith pattern and managed AWS services to minimize operational complexity for a three-person team. It enforces rigorous security and tamper-evident auditability to satisfy PCI-DSS compliance and financial regulations within a fixed budget.