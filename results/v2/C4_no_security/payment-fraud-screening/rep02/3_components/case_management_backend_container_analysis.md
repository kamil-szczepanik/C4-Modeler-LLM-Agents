## Overview
[The Case Management Backend Container provides case review workflows and audit logging for fraud analysts reviewing suspicious payment authorizations. It is built to satisfy PCI-DSS Level 1 compliance and 7-year auditability while maintaining a low-cost, serverless footprint on AWS.]

## Key Elements
* Case API Router / Controller (Node.js/TypeScript)
* Workflow & Assignment Engine
* Audit & Activity Logger
* Metrics Publisher

## Relationships
* Fraud Analyst SPA -> Case API Router: Sends API requests for case reviews [HTTPS/REST]
* Workflow Engine -> Primary Operational Datastore: Writes transactional state [SQL over TLS]
* Metrics Publisher -> Amazon CloudWatch: Publishes EMF telemetry [Asynchronous in-process emission]

## Technology Stack
* Node.js/TypeScript: Selected for rapid case-management feature development by a 3-engineer team
* AWS ECS Fargate: Chosen for serverless container orchestration within the 25,000 EUR monthly budget
* Amazon Aurora PostgreSQL Serverless v2: Utilized for transactional case states and secure SQL over TLS storage
* Amazon CloudWatch EMF: Adopted for zero-infrastructure operational metrics and dashboard generation

## Rationale
[Decomposing the container into in-process modules avoids the operational overhead of managing secondary caching or messaging clusters like Redis. This design strictly adheres to the 25,000 EUR budget, requires minimal maintenance from three engineers, and ensures PCI-DSS Level 1 security.]