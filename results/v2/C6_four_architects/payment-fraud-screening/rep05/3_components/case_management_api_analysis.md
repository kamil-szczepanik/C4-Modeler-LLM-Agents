## Overview
[A modular monolith architecture built for the Case Management API container to handle fraud analyst review workflows securely on AWS. It screens payment transactions and manages suspicious cases while meeting strict compliance and budget limits.]

## Key Elements
- API Controller Component (Python, FastAPI)
- Masking & Tokenization Interceptor Component (Python)
- IAM Authorization Component (Python, FastAPI Dependency Injection)
- Case Service Component (Python)
- Audit Logger Component (Python)
- Amazon Aurora PostgreSQL
- Amazon S3 Object Lock
- Amazon SQS

## Relationships
- API Gateway -> API Controller Component: Forwards REST requests [HTTPS/REST]
- API Controller Component -> Masking & Tokenization Interceptor Component: In-process middleware hook [Python native]
- API Controller Component -> IAM Authorization Component: In-process dependency check [Python native]
- Masking & Tokenization Interceptor Component -> Case Service Component: Passes sanitized case data payloads [Python native]
- Case Service Component -> Amazon Aurora PostgreSQL: Reads and writes relational case state [TCP/TLS via SQLAlchemy ORM]
- Case Service Component -> Amazon SQS: Emits case resolution events [HTTPS/SQS API]
- Audit Logger Component -> Amazon S3 Object Lock: Writes tamper-evident audit trails [HTTPS/S3 API]

## Technology Stack
- Python with FastAPI: Provides lightweight, high-performance API routing and dependency injection for a 3-engineer team.
- Amazon ECS Fargate: Runs the modular monolith container without server management overhead.
- Amazon Aurora PostgreSQL: Stores operational case data reliably with robust ACID compliance.
- Amazon S3 Object Lock: Implements write-once-read-many (WORM) storage for 7-year tamper-evident auditability (R-06).
- Amazon SQS: Decouples downstream event publishing for model retraining.

## Rationale
[This modular monolith architecture minimizes operational complexity and infrastructure overhead, allowing a three-engineer team to operate within a 25,000 EUR monthly budget. Furthermore, internal component boundaries and managed AWS services enforce strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.]