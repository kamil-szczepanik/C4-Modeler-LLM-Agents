## Overview
The Amazon Aurora Serverless v2 PostgreSQL container provides secure, auto-scaling relational data storage for real-time payment fraud screening. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a 25,000 EUR monthly AWS budget.

## Key Elements
- Audit Ledger Schema (PostgreSQL tables with cryptographic extensions for R-06)
- Case Management Schema (Relational tables for analyst workflows via R-02)
- Connection Pooler (PgBouncer Sidecar for traffic management)
- PostgreSQL RLS Enforcement Component (Tenant and analyst isolation)
- AWS IAM Database Authentication Plugin (Zero static credentials)
- AWS KMS Custom Managed Key (CMK for encryption at rest)

## Relationships
- Case Management Backend -> PostgreSQL RLS Enforcement Component: Validates isolation via PostgreSQL wire protocol [TLS]
- Auditor Query Service -> Audit Ledger Schema: Reads immutable audit logs via PostgreSQL wire protocol [TLS]
- Amazon Aurora Serverless v2 PostgreSQL -> AWS KMS (CMK): Encrypts storage and backups [AWS API]

## Technology Stack
- Amazon Aurora Serverless v2 PostgreSQL: Serverless auto-scaling within budget limits while preventing cold starts via minimum ACU configuration
- PgBouncer: Connection pooling sidecar for DoS mitigation and resource efficiency
- AWS KMS: Customer Managed Key encryption for PCI-DSS Level 1 compliance
- AWS IAM: Database authentication and credential management

## Rationale
This architecture guarantees sub-50ms performance and 99.99% availability by tuning Aurora auto-scaling parameters to prevent cold starts. It satisfies stringent PCI-DSS Level 1 and 7-year auditability mandates through immutable ledger tables, Row-Level Security, and KMS encryption.