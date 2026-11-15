## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid Azure platform while legacy claims continue processing. It ensures zero data loss, sub-2-second adjuster response times, and a one-day rollback capability per claim type.]

## Key Elements
- Claims Schema (Relational Tables with Temporal Tables)
- Outbox Schema (Outbox Pattern Tables)
- Sync Tracking Schema
- Read Model Projections (Dedicated projection tables)
- Azure SQL Database (Serverless compute tier with Geo-Replication)

## Relationships
- API Gateway & BFF -> Claims Schema: Queries and mutates data via ADO.NET and Entity Framework Core (TCP/1433 with TLS 1.2 and Azure AD authentication)
- Integration & Anti-Corruption Layer -> Sync Tracking Schema: Reconciles migrated records using SQL bulk operations
- Outbox Schema -> Azure Service Bus: Drained by Azure Functions via managed identity polling

## Technology Stack
- Azure SQL Database: Provides managed relational storage with Transparent Data Encryption (TDE) and Always Encrypted for PII
- Entity Framework Core: Implements data access and application-level validation, replacing T-SQL stored procedures
- GitHub Actions: Automates database migrations and schema deployments
- Azure Key Vault: Manages secure credentials and managed identities for database access

## Rationale
[This hybrid architecture balances cloud modernization with mainframe constraints by decoupling database writes from legacy syncs using the Outbox pattern. Leveraging managed Azure SQL features minimizes operational overhead for a cloud-inexperienced team while meeting strict security and consistency requirements.]