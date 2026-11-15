## Overview
The Case Management Backend is a container within the Real-Time Payment Fraud Screening system that enables fraud analysts to review suspicious transactions. It securely processes case workflows and maintains compliance while adhering to strict PCI-DSS Level 1 constraints.

## Key Elements
- Fraud Analysts: External users reviewing suspicious payments.
- Case API Handler (Node.js/Express): Manages incoming analyst HTTP requests.
- Case Workflow Engine (Go): Executes state transitions and business logic.
- Data Access Repository: Enforces data masking and queries the database.
- Audit Logger Component: Generates and exports tamper-evident compliance trails.
- Amazon Aurora PostgreSQL: Stores case data.
- Amazon S3 Object Lock: Stores immutable audit logs.

## Relationships
- Fraud Analysts -> Case API Handler: Manages cases [HTTPS/REST]
- Case API Handler -> Case Workflow Engine: Invokes business logic [Internal Function Call / gRPC]
- Case Workflow Engine -> Data Access Repository: Persists case state [In-memory / Go interfaces]
- Data Access Repository -> Amazon Aurora PostgreSQL: Reads/writes masked case data [SQL/TCP]
- Case Workflow Engine -> Audit Logger Component: Dispatches audit events [Internal Async / Channel]
- Audit Logger Component -> Amazon S3 Object Lock: Persists tamper-evident audit logs [AWS SDK / HTTPS]

## Technology Stack
- Node.js/Express (Case API Handler): Selected for rapid UI-driven feature iteration by a small engineering team.
- Go (Case Workflow Engine, Data Access Repository, Audit Logger): Chosen for high performance, strong typing, and concurrency support.
- AWS ECS Fargate: Chosen to minimize operational overhead for a three-engineer team within a 25,000 EUR monthly budget.
- Amazon Aurora PostgreSQL: Relational storage enforcing strict PCI-DSS data masking.
- Amazon S3 Object Lock: Provides tamper-evident, write-once-read-many (WORM) storage for 7-year audit requirements.

## Rationale
This architecture balances rapid feature delivery for analysts with strict PCI-DSS and 7-year audit requirements using lightweight serverless containers. The clear separation of concerns ensures card data remains masked while satisfying all non-functional constraints within budget.