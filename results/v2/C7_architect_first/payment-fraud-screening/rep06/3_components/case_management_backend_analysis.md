## Overview
The Case Management Backend is a Node.js/Express container on AWS ECS Fargate that manages suspicious payment fraud cases for fraud analysts. It ingests review-routed events via Amazon MSK Serverless to provide structured case workflows and tamper-evident audit logging.

## Key Elements
- **Case API Router:** Express.js controller handling REST endpoints over HTTPS for fraud analysts.
- **Case Service:** TypeScript domain logic managing case assignment, prioritization, notes, and workflows.
- **Audit Logger:** TypeScript SDK securing tamper-evident audit logs for 7-year retention.
- **Event Consumer:** KafkaJS background worker ingesting asynchronous review events from Amazon MSK Serverless.

## Relationships
- Fraud Analysts -> Case API Router [HTTPS via AWS ALB with OIDC-backed JWT validation]
- Case API Router -> Case Service [In-process function call]
- Case Service -> Audit Logger [In-process function call]
- Case Service -> Amazon Aurora Serverless v2 [SQL/TCP over TLS 1.3 via Prisma ORM]
- Amazon MSK Serverless -> Event Consumer [Kafka Protocol over TLS 1.3 with IAM authentication]
- Event Consumer -> Case Service [In-process function call]

## Technology Stack
- **Node.js & Express.js:** Chosen for rapid development and lightweight execution within the 3-engineer team constraint.
- **TypeScript:** Ensures type safety across domain logic and event schemas.
- **Amazon Aurora Serverless v2:** Provides auto-scaling relational storage for case data and audit records within budget.
- **KafkaJS & Amazon MSK Serverless:** Decouples real-time payment ingestion from downstream case creation.
- **AWS ECS Fargate:** Eliminates server management overhead to fit operational constraints.

## Rationale
This architecture decouples asynchronous case management from the ultra-low latency real-time scoring engine while maintaining strict PCI-DSS Level 1 compliance. Using serverless AWS components and TypeScript maximizes feature delivery speed for a three-engineer team within a 25,000 EUR monthly budget.