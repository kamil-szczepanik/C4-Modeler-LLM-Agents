## Overview
The Case Management Backend provides secure, scalable case administration and review workflows for fraud analysts within the Real-Time Payment Fraud Screening system. It processes suspicious transactions while strictly enforcing PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- Case Management Backend: NestJS (TypeScript) container running on AWS ECS Fargate
- API Router / Controller: Handles REST requests and JWT validation
- Case Service: Implements case lifecycle logic, bulk actions, and SLA-based routing
- SLA Worker / Scheduler Component: Manages background timers and auto-escalations via `@nestjs/schedule`
- Audit Logger Component: Records cryptographically signed analyst actions
- Data Access Layer: Utilizes an ORM to manage relational data
- Amazon Aurora PostgreSQL: Managed relational database with AES-256 encryption
- Immutable Audit Storage: Secure target for tamper-evident audit logs

## Relationships
- Case Management UI -> API Router / Controller: Sends API requests for case operations [HTTPS/REST, TLS 1.3]
- API Router / Controller -> Identity Provider: Validates JWTs and enforces RBAC [HTTPS/REST]
- Case Service -> Amazon Aurora PostgreSQL: Reads and writes case state and search indexes [TCP/TLS, Port 5432]
- Audit Logger Component -> Immutable Audit Storage: Writes signed analyst action logs [HTTPS/REST]

## Technology Stack
- TypeScript & NestJS: Chosen for structured modularity and high developer velocity
- Amazon Aurora PostgreSQL: Selected for relational ACID guarantees and built-in search indexing without operational complexity
- AWS ECS Fargate: Provides container orchestration within a 3-engineer constraint
- AWS KMS: Implements AES-256 encryption and key rotation for data protection

## Rationale
This architecture balances robust security and strict compliance requirements with rapid developer velocity for a small team. The serverless container and managed database approach fits within the fixed budget while supporting sub-minute failover and long-term auditability.