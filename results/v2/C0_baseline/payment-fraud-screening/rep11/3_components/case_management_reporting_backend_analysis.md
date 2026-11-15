## Overview
The Case Management & Reporting Backend is a Python FastAPI service that supports fraud analysts in reviewing suspicious transactions and enables compliance officers to run historical audits. It ensures secure, low-latency case workflows while strictly adhering to PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
- Case API Controller (FastAPI Router)
- Case Service & Business Logic Layer
- Case Repository (SQLAlchemy ORM)
- Compliance & Audit Service
- Tokenization Gateway Client
- Amazon RDS PostgreSQL (Provisioned Instance)
- Amazon ElastiCache for Redis
- Amazon Athena

## Relationships
- Case API Controller -> Case Service & Business Logic Layer: Internal function calls [Python]
- Case Service & Business Logic Layer -> Case Repository: Database queries and updates [SQLAlchemy / PostgreSQL Protocol]
- Case Service & Business Logic Layer -> Tokenization Gateway Client: Retrieves masked card data [HTTPS/REST]
- Compliance & Audit Service -> Amazon Athena: Executes historical compliance queries [AWS SDK / Athena API]
- Compliance & Audit Service -> Amazon ElastiCache for Redis: Caches frequent report data [RESP Protocol]

## Technology Stack
- Python FastAPI: Chosen for rapid iteration and rich ecosystem suited for a 3-engineer team.
- Amazon RDS PostgreSQL: Single provisioned instance with AWS KMS encryption for predictable costs and simple maintenance.
- Amazon ElastiCache for Redis: Caches frequent reports to reduce Athena query costs and latency.
- Amazon Athena: Runs asynchronous, batch-oriented compliance reports for 7-year audit data.
- SQLAlchemy ORM: Manages database interactions within the Case Repository.
- AWS Secrets Manager: Secures and rotates database credentials and external API tokens.

## Rationale
This architecture balances a strict €25,000 monthly infrastructure budget and a 3-engineer team capacity by avoiding unpredictable scaling costs while enforcing robust security. Decoupling synchronous case management from asynchronous compliance reporting ensures predictable performance and meets all PCI-DSS and 7-year audit requirements.