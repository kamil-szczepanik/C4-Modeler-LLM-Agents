## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe while maintaining continuous operations. Its core purpose is to provide modern web interfaces for customers, brokers, and claims adjusters while ensuring zero data loss and seamless data synchronization.

## Key Elements
- Claims Core Domain Service
- Azure SQL Database
- Schema Domain Partitioning Engine
- Temporal Data Tables
- Change Data Capture (CDC) Component
- Row-Level Security (RLS) Policy Engine
- Elastic Pool Management Component
- Integration & Sync Worker (Azure Functions)
- Azure Key Vault

## Relationships
- Claims Core Domain Service -> Row-Level Security (RLS) Policy Engine: Queries transactional data [Tabular Data Stream (TDS) over TLS 1.3 via Managed Identity]
- Integration & Sync Worker -> Change Data Capture (CDC) Component: Streams delta changes [TDS over TLS 1.3 via Managed Identity]
- Azure SQL Database -> Azure Key Vault: Retrieves customer-managed encryption keys [HTTPS / REST]

## Technology Stack
- Azure SQL Database: Provides managed transactional data storage with native high availability and built-in migration safeguards.
- System-Versioned Temporal Tables: Automates audit tracking natively without application-level overhead.
- Change Data Capture (CDC): Exposes low-latency transaction logs for reliable data synchronization.
- Row-Level Security (RLS): Enforces data jurisdiction boundaries directly at the database layer.
- Transparent Data Encryption (TDE): Secures data at rest using keys managed in Azure Key Vault.
- Managed Identity (Azure Entra ID): Eliminates embedded credentials for secure service authentication.

## Rationale
This architecture ensures strict transactional consistency, secure PII handling, and rapid one-day claim type rollbacks. It leverages managed cloud database features to minimize custom code, accommodating the team's limited cloud experience while meeting strict performance and hybrid compliance constraints.