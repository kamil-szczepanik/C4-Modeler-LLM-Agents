## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and provides case management tools for analysts to review suspicious transactions. It ensures sub-50ms P99 decision latency while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability on a fixed budget.

## Key Elements
* Fraud Analysts
* Risk & Compliance Officers
* API Gateway / Application Load Balancer (AWS API Gateway / ALB)
* Case Management App (Node.js backend + React SPA, AWS ECS Fargate)
* API Router & Auth Middleware (Node.js/Express)
* Case Business Logic Component (Node.js)
* Analyst SPA Frontend (React)
* Amazon Aurora PostgreSQL
* Amazon SQS
* Identity Provider (IdP)
* Audit Ledger

## Relationships
* Fraud Analysts -> Case Management App: Reviews suspicious transactions [HTTPS, OAuth2/OIDC]
* Risk & Compliance Officers -> Case Management App: Audits historical data and compliance logs [HTTPS, OAuth2/OIDC]
* Case Management App -> Identity Provider (IdP): Authenticates users [OAuth2/OIDC with short-lived JWTs]
* Analyst SPA Frontend -> API Router: Transmits API requests [HTTPS/REST]
* API Router & Auth Middleware -> Case Business Logic Component: Forwards validated requests [In-memory / REST]
* Case Business Logic Component -> Amazon Aurora PostgreSQL: Persists case and transaction data [TLS/SQL]
* Case Business Logic Component -> Audit Ledger: Sends signed analyst actions [HTTPS / signed requests]
* Case Business Logic Component -> Amazon SQS: Offloads asynchronous SLA checks and notifications [AWS SDK / TLS]

## Technology Stack
* AWS ECS Fargate: Runs containerized backend and frontend workloads without server management within budget.
* Node.js / Express: Powers the backend API and business logic for high concurrency and fast execution.
* React: Implements the analyst SPA frontend and productivity dashboard.
* Amazon Aurora PostgreSQL: Stores relational case data with encryption-at-rest via AWS KMS.
* Amazon SQS: Decouples asynchronous workflows to protect synchronous review performance.

## Rationale
This architecture leverages managed serverless container infrastructure on AWS to meet performance, strict PCI-DSS Level 1 security, and auditability requirements. It keeps operational overhead minimal for a three-engineer team while strictly enforcing budget and compliance constraints.