## Overview
The system modernizes a regional insurer's 30-year-old mainframe by introducing a hybrid cloud claims platform. It gradually migrates claim types while ensuring zero data loss and maintaining high-performance adjuster workflows.

## Key Elements
- Azure SQL Database (Managed relational datastore)
- Claims Core Module (Relational tables with Temporal Tables)
- Sync & Integration Module (Idempotency and outbox pattern tables)
- Performance Views (Indexed views)
- Backend APIs & Integration Workers (Clients accessing the database)

## Relationships
- Backend APIs -> Azure SQL Database: Reads and writes modern claim types [Entity Framework Core / T-SQL]
- Migration & Sync Engine -> Azure SQL Database: Reads/Writes sync states and mirrored data [T-SQL / EF Core]
- Integration Workers -> Azure SQL Database: Updates claim processing status [EF Core / T-SQL]

## Technology Stack
- Azure SQL Database: Chosen for managed features and relational flexibility supporting gradual claim migration (R-03) and rapid rollback (R-06).
- Entity Framework Core: Used for domain logic and automated schema migrations to simplify CI/CD pipelines.
- Temporal Tables & Indexed Views: Built-in features used for auditability and sub-2-second adjuster screen loads (R-05).
- Microsoft Entra ID & Private Endpoints: Enforced for secure authentication via managed identities and network isolation (R-07).

## Rationale
This architecture fits the requirements by leveraging managed cloud services that require minimal custom infrastructure code, accommodating the team's low cloud experience. It guarantees zero data loss (R-04) and high performance (R-05) while safely bridging the modern Azure environment with the legacy mainframe.