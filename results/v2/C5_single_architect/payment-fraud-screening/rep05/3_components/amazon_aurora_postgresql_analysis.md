## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides case management tools for fraud analysts. It operates on AWS to meet strict performance, compliance, and auditability requirements.

## Key Elements
- **Case Management Schema**: PostgreSQL tables storing analyst reviews and case states.
- **Audit Log Vault**: `pg_audit` extension and append-only tables capturing immutable decision logs.
- **Row-Level Security (RLS) Enforcer**: PostgreSQL RLS policies enforcing PCI-DSS data segregation.
- **Data Masking & Tokenization Engine**: PostgreSQL functions and `pgcrypto` dynamically masking primary account numbers (PANs).

## Relationships
- Case Management Backend -> Case Management Schema: Reads and writes case data [SQL/TCP]
- Fraud Scoring Engine -> Audit Log Vault: Appends immutable decision logs [SQL/TCP]
- Case Management Schema -> Data Masking & Tokenization Engine: Sanitizes card data on read [PL/pgSQL]

## Technology Stack
- **Amazon Aurora PostgreSQL**: Relational database providing transactional persistence and multi-AZ availability.
- **`pg_audit` & Append-Only Tables**: Ensures tamper-evident auditability for 7-year retention requirements (R-06).
- **PostgreSQL RLS Policies & `pgcrypto`**: Enforces strict PCI-DSS compliance and card data tokenization at the database layer (R-05).

## Rationale
This component architecture leverages native PostgreSQL extensions to satisfy stringent PCI-DSS and tamper-evident audit requirements without adding operational complexity for a three-person engineering team. Keeping security and audit controls inside the database layer minimizes code-level compliance drift while maintaining the required P99 performance under budget.