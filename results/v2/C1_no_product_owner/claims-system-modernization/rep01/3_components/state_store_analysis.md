## Overview
[The State Store component provides transactional persistence and point-in-time recovery for the Insurance Claims Modernization platform. It ensures zero data loss and enables rapid rollbacks during the gradual migration of legacy claims.]

## Key Elements
- Claim Operational Table (Azure SQL Relational Table)
- Sync Ledger Table (Azure SQL Relational Table)
- Audit & Fallback Log (Azure SQL Relational Table)
- Stored Procedure Gateway (Database mechanisms for ACID compliance)
- Temporal Tables / Change Tracking (Native Azure SQL history retention)
- Resource Governor (CPU/memory throttling mechanism)

## Relationships
- Claims Modernization Core -> Claim Operational Table: Read/Write claim aggregates [ADO.NET / JDBC via TDS over TLS 1.3]
- Integration & Sync Engine -> Sync Ledger Table: Update sync watermarks [ADO.NET / JDBC via TDS over TLS 1.3]
- Claims Modernization Core -> State Store: Authenticated via Azure AD Managed Identities

## Technology Stack
- Azure SQL Database Managed Instance: Chosen for fully managed transactional persistence and high availability.
- Azure SQL Temporal Tables: Chosen to handle historical audits natively and support R-06 rollbacks without custom logic.
- Flyway / Liquibase: Selected for automated CI/CD schema migrations to mitigate team cloud experience gaps.
- Azure Key Vault with CMK: Provides Transparent Data Encryption (TDE) for strict data protection.
- Azure SQL Resource Governor: Configured to isolate batch workloads and guarantee R-05 (<2s latency).

## Rationale
[This architecture uses managed Azure SQL features and native database mechanisms to minimize custom code overhead for a team with limited cloud experience. It strictly enforces consistency, security, and performance constraints required for the hybrid legacy migration.]