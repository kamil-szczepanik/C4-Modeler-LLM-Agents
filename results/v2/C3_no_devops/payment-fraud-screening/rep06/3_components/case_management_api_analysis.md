## Overview
[Real-Time Payment Fraud Screening system screens card-not-present payment authorizations and manages analyst reviews. It ensures PCI-DSS Level 1 compliance and sub-50ms P99 latency within a strict budget.]

## Key Elements
- Fraud Analyst SPA (React / Amazon S3 / Amazon CloudFront)
- Case Management API (Python / FastAPI / Amazon ECS Fargate)
- Case Workflow Controller
- Audit & Persistence Adapter (SQLAlchemy)
- Audit & Persistence Store (Amazon Aurora PostgreSQL)
- Asynchronous Event Bus (Amazon EventBridge)
- API Gateway / Ingress Router (Amazon API Gateway / AWS ALB)
- Identity Provider (AWS Cognito)
- Secrets Manager (AWS Secrets Manager)

## Relationships
- Fraud Analyst SPA -> API Gateway: Managing analyst workflows and review queues [HTTPS/REST with OAuth2/OIDC via AWS Cognito]
- API Gateway -> Case Management API: Forwards validated requests [HTTP/TLS 1.3]
- Case Workflow Controller -> Amazon Aurora PostgreSQL: Persists case states and audit logs [JDBC/TLS]
- Case Workflow Controller -> Asynchronous Event Bus: Publishes review outcomes [HTTPS]

## Technology Stack
- Python/FastAPI: Lightweight framework for Case Management API and component logic.
- Amazon ECS Fargate: Serverless container orchestration fitting the 3-engineer team constraint.
- Amazon Aurora PostgreSQL: Managed database utilized with native controls for tamper-evident append-only logging (R-06).
- Pydantic: Framework-level serialization for explicit data minimization and exclusion of PAN fields (R-05).
- AWS Cognito: Managed service handling OAuth2/OIDC and RBAC.
- AWS Secrets Manager: Provides secure injection and rotation of database credentials.

## Rationale
[This architecture leverages managed AWS services and lightweight frameworks to minimize engineering overhead for a three-person team within a 25,000 EUR monthly budget. It meets strict PCI-DSS Level 1 compliance and 7-year auditability constraints using native platform capabilities.]