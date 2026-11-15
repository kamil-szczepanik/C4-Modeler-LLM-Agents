## Overview
The Case Management API is a container component powering fraud analyst review workflows and tamper-evident audit logging for the Real-Time Payment Fraud Screening system. It securely manages suspicious payment cases while strictly enforcing PCI-DSS compliance and 7-year auditability.

## Key Elements
- Fraud Analysts: External users reviewing suspicious payment cases via web UI.
- Case Controller: Node.js/Express service exposing REST endpoints for analyst workflows.
- Audit & Evidence Service: Component capturing analyst decisions with cryptographically verifiable hashes.
- Case Repository: Data access layer interacting with Amazon Aurora PostgreSQL.
- Masking & Tokenization Proxy: Interceptor middleware ensuring card numbers are redacted.

## Relationships
- Fraud Analysts -> Case Controller [HTTPS/JSON]
- Case Controller -> Audit & Evidence Service [In-process Function Call]
- Case Controller -> Case Repository [TCP/PostgreSQL Protocol]
- Case Repository -> Masking & Tokenization Proxy [In-process Middleware]

## Technology Stack
- TypeScript / Node.js with Express: Provides rapid development velocity suited for a three-engineer team.
- Amazon Aurora PostgreSQL: Shared persistent data store for relational case data.
- Prisma / Axios Interceptors: Implements consistent data masking and redaction at the application boundary.

## Rationale
This component architecture fits requirements by isolating security-sensitive workflows, ensuring analysts never see unmasked card data, and generating tamper-evident audit trails within a constrained team size and budget.