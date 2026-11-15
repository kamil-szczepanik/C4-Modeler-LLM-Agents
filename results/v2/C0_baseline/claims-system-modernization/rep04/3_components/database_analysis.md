## Overview
This architecture establishes a hybrid database platform for modernizing a legacy insurance claims system. It ensures data consistency and targeted rollbacks during a phased 3-year migration.

## Key Elements
- Claim Operational Store (Azure SQL Tables)
- Audit & History Engine (System-Versioned Temporal Tables)
- Integration Staging Store
- Archival & Purging Component (Azure SQL Elastic Jobs)
- Identity Provider (Microsoft Entra ID)
- Key Management (Azure Key Vault)

## Relationships
- Backend Service -> Claim Operational Store / Audit & History Engine: `T-SQL / ADO.NET [Encrypted VNet connection]`
- Mainframe Integration Adapter -> Integration Staging Store: `Bulk Insert / T-SQL [VNet Peering]`
- Azure SQL Database -> Azure Key Vault: `Managed Identity / HTTPS [Key Vault REST API]`

## Technology Stack
- Azure SQL Database: Provides relational storage, temporal tables, and workload governance for high availability and transactional consistency.
- Entity Framework Core: Implements code-first migrations with online index operations to prevent table locking during adjuster workflows.
- Azure Key Vault: Secures Customer-Managed Keys (CMK) for Transparent Data Encryption (TDE).
- Microsoft Entra ID: Enforces secure, passwordless authentication using managed identities.

## Rationale
The hybrid architecture balances low cloud team experience with strict regulatory and performance constraints. Temporal tables and feature flags enable rapid 1-day rollbacks per claim type without risky database-wide restores.