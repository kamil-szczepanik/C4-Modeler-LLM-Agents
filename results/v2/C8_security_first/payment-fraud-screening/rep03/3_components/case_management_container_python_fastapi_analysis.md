## Overview
The Case Management Container provides secure workflow tools and API backends for fraud analysts reviewing suspicious payment authorizations. It ensures PCI-DSS Level 1 compliance while enabling efficient investigations and feedback loops to fraud scoring models.

## Key Elements
* Case Management Container (Python / FastAPI)
* API / Routing Layer (FastAPI Routers)
* Authentication / RBAC Middleware
* Business Logic / Case Service
* Data Access Layer (SQLAlchemy ORM)
* Event Publisher / Webhook Component
* Audit Logger Sidecar Container
* Amazon Aurora Serverless v2

## Relationships
* AWS Application Load Balancer (ALB) -> Case Management Container: Routes analyst traffic [HTTPS]
* API / Routing Layer -> Authentication / RBAC Middleware: Validates requests [In-process Function Call]
* Business Logic / Case Service -> Amazon Aurora Serverless v2: Persists state changes [SQL/TLS]
* Business Logic / Case Service -> Audit Logger Sidecar Container: Dispatches audit events [gRPC/Local IPC]
* Business Logic / Case Service -> Event Publisher: Dispatches model feedback [In-process Function Call]
* Event Publisher -> Model Registry / Feature Store: Forwards feedback loops [HTTPS/TLS]

## Technology Stack
* Python / FastAPI: High-productivity web framework supporting async operations
* SQLAlchemy with asyncpg: Asynchronous database driver and ORM for high throughput
* AWS ECS with AWS Fargate: Serverless container execution minimizing management overhead for a 3-engineer team
* structlog and AWS FireLens: Structured JSON logging and telemetry routed to CloudWatch
* AWS Secrets Manager & KMS: Secure credential injection and encryption at rest using customer-managed keys

## Rationale
This architecture uses serverless AWS services to remain within the 25,000 EUR monthly budget while supporting a 3-engineer team. Strict internal component layering and field-level data masking enforce PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.