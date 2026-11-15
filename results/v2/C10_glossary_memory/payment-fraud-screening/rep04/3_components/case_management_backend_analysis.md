## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present transactions, provides case management for fraud analysts, and maintains tamper-evident audit logs. Its core purpose is to screen payment authorizations for fraud within strict latency limits while complying with PCI-DSS Level 1.

## Key Elements
- Fraud Analyst [person]
- Risk Operations Manager / Data Scientist [person]
- Case Management Backend [container] (Node.js monolith on AWS Fargate)
- API Router / Controller [component]
- Case Service [component]
- Case Analytics & Metrics Service [component]
- Audit Logger Component [component]
- Audit & Event Store [container] (AWS Aurora PostgreSQL with read-replicas)
- Identity Provider (IdP) [externalSystem]

## Relationships
- Case Management UI -> API Router / Controller: Sends API requests for case workflows [HTTPS]
- API Router / Controller -> Identity Provider (IdP): Validates JWTs [HTTPS]
- API Router / Controller -> Case Service: Routes case workflows [Internal]
- API Router / Controller -> Case Analytics & Metrics Service: Requests KPI reports [Internal]
- Case Service -> Audit & Event Store: Persists case updates and audit trails [TCP/TLS]
- Case Analytics & Metrics Service -> Audit & Event Store: Queries historical case data [TCP/TLS]

## Technology Stack
- Node.js with Express: Powers the Case Management Backend monolith for rapid development by a 3-person team.
- AWS Fargate (ECS): Hosts the containerized backend without control-plane management overhead to fit within budget.
- AWS Aurora PostgreSQL: Provides scalable relational storage with dedicated read-replicas for analytics.
- AWS Secrets Manager & KMS: Manages secrets and secures tamper-evident audit logs via cryptographic signing.
- Terraform: Automates infrastructure provisioning and ensures secure, repeatable deployments.

## Rationale
This architecture uses a monolithic Node.js container on AWS Fargate to minimize operational complexity for a three-person team within a 25,000 EUR/month budget. Dedicated Aurora PostgreSQL read-replicas and cryptographic signing satisfy strict PCI-DSS compliance and 7-year audit requirements without compromising real-time performance.