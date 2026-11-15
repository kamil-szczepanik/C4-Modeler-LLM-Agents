## Overview
- Hybrid insurance claims modernization platform gradually replacing a 30-year-old COBOL/DB2 mainframe.
- Provides scalable relational data storage and reliable asynchronous messaging to ensure business continuity during migration.

## Key Elements
- Database: Azure SQL Database (provisioned tier)
- Schemas & Tables: Claims relational tables, Transactional Outbox table, Audit & Reconciliation log table
- Access Clients: Claims Core Services, Integration / Anti-Corruption Layer (ACA Worker)
- Security & Operations: Microsoft Entra ID, Azure Private Endpoints, Azure Monitor

## Relationships
- Claims Core Services -> Database: Reads and writes claim data [T-SQL / TDS over Private Endpoint]
- Integration / Anti-Corruption Layer -> Database: Synchronizes legacy data and updates outbox state [T-SQL / TDS over Private Endpoint]
- Database -> Azure Monitor: Streams auditing and diagnostic logs [HTTPS / TLS]

## Technology Stack
- Azure SQL Database (Provisioned Tier): Ensures predictable performance and avoids cold-start latency.
- Entity Framework Core: Provides robust ORM mapping for relational claims data.
- Transparent Data Encryption (TDE) & Always Encrypted: Secures data at rest and protects PII.
- Azure Private Endpoints: Isolates database traffic within a secure virtual network.

## Rationale
- Provisioned tier and table partitioning guarantee sub-2-second query performance and stable batch processing windows.
- Transactional outbox pattern and audit logging ensure zero lost or duplicated claims and support rapid 1-day rollbacks.