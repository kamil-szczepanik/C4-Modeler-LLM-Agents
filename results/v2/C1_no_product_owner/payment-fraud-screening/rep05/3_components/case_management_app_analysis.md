## Overview
A real-time payment fraud screening system processes card-not-present transactions, while providing fraud analysts a secure case management interface. It ensures sub-50ms P99 decisions at 3,000 TPS under PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget.

## Key Elements
- **API Controller Component (Express.js)**: Handles routing, OIDC/MFA authentication, rate limiting, and RBAC.
- **Case Service Component (TypeScript)**: Manages case workflows, business logic, and Prisma ORM interactions.
- **UI SPA Component (React / Tailwind CSS)**: Renders the analyst dashboard with masked card data.
- **Audit & Compliance Component (TypeScript)**: Generates structured, immutable audit logs.
- **Tokenization Gateway Client (TypeScript)**: Communicates with external tokenization services via mTLS.
- **Amazon RDS Proxy**: Pools database connections and enforces TLS.
- **Amazon RDS PostgreSQL**: Persists relational case data.
- **Amazon CloudWatch Logs & S3 with Object Lock**: Stores tamper-evident, KMS-encrypted audit trails.
- **AWS ECS Fargate & Application Load Balancer**: Runs containers with autoscaling, managed by a three-engineer team.

## Relationships
- **Fraud Analysts** -> **API Controller Component**: Views and updates case statuses [HTTPS/TLS 1.3 with MFA]
- **API Controller Component** -> **Case Service Component**: Delegates business logic [In-memory]
- **Case Service Component** -> **Tokenization Gateway Client**: Requests masked card data [HTTPS/REST with mTLS]
- **Case Service Component** -> **Amazon RDS Proxy**: Persists case data [TCP/TLS]
- **Case Service Component** -> **Audit & Compliance Component**: Dispatches audit events [In-memory]
- **Audit & Compliance Component** -> **Amazon CloudWatch Logs**: Streams structured JSON logs [AWS Firelens/HTTPS]
- **Amazon CloudWatch Logs** -> **Amazon S3 with Object Lock**: Archives immutable logs [Subscription Filter]

## Technology Stack
- **Node.js / Express.js / TypeScript**: Powers backend components for robust, typed service logic within a small team's skill set.
- **React / Tailwind CSS**: Renders a responsive analyst UI served via containerized monolith.
- **Prisma ORM & Amazon RDS PostgreSQL**: Provides type-safe database access and reliable relational storage.
- **Amazon RDS Proxy**: Prevents connection exhaustion during Fargate scaling events.
- **AWS ECS Fargate**: Minimizes operational overhead within the €25k/month budget.
- **Amazon S3 with Object Lock & CloudWatch Logs**: Ensures tamper-evident, 7-year audit compliance.

## Rationale
This architecture balances strict PCI-DSS security, 7-year auditability, and sub-50ms performance requirements using fully managed AWS services. By leveraging serverless containers (ECS Fargate) and managed proxies (RDS Proxy), it maintains high availability within a fixed budget for a three-engineer team.