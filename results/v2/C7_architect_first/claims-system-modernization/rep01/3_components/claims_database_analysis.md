## Overview
This system modernizes a regional insurer's 30-year-old mainframe claims platform using a hybrid cloud architecture. It gradually migrates claim types to a modern Azure-based platform while maintaining uninterrupted core processing.

## Key Elements
- **Claim Core Store**: Azure SQL with Temporal Tables and Row-Level Security (RLS)
- **Migration Sync Staging**: Azure SQL Staging Tables for batch synchronization
- **Data Access Layer**: Entity Framework Core libraries
- **State Reconciliation Engine**: .NET Claims Processing Service component for idempotent upserts
- **Temporal Audit Dispatcher**: Data Access Layer component for history retention

## Relationships
- **Claims Processing Service -> Data Access Layer**: In-process method calls (`.NET references`)
- **Data Access Layer -> Claim Core Store / Migration Sync Staging**: Executes queries and transactions (`TDS / SQL`)
- **Integration & Anti-Corruption Layer -> Claims Processing Service**: Managed API calls routing all writes to avoid direct database access

## Technology Stack
- **Azure SQL Database**: Relational storage providing Transparent Data Encryption (TDE), Column-Level Encryption (Always Encrypted), and Dynamic Data Masking (DDM) for PII security
- **Entity Framework Core**: ORM for data access and automated migration down-scripts supporting rapid rollbacks
- **Azure Entra ID (Managed Identities)**: Secretless authentication between services and databases
- **Azure Monitor**: Observability platform tracking batch window performance and deadlocks

## Rationale
This architecture decouples the legacy mainframe from modern user workflows while enforcing strict trust boundaries and data consistency. Keeping complex reconciliation logic in the .NET layer rather than database procedures ensures maintainability for a team with limited cloud experience.