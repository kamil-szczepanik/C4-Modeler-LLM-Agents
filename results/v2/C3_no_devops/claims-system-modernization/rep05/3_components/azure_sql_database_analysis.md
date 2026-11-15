## Overview
[System: Insurance Claims Modernization, Purpose: Gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while ensuring business continuity.]

## Key Elements
- Claims Schema (SQL Server Engine)
- Temporal Audit Tables (System-Versioned Temporal Tables)
- Change Feed Engine (Change Data Capture)
- Maintenance & Index Manager (Azure SQL Elastic Jobs)
- Geo-Replication Controller (Azure SQL Active Geo-Replication)

## Relationships
- Claims Processing Service -> Claims Schema: Reads/writes transactional claim data via TDS over TLS 1.3
- Change Feed Engine -> Azure Service Bus: Streams entity deltas via AMQP
- Geo-Replication Controller -> Secondary Region Azure SQL: Replicates encrypted storage blocks via Azure Backbone Network

## Technology Stack
- Azure SQL Database: Provides relational storage for migrated claim types ensuring rapid rollback capability
- Azure Active Directory: Enforces SSO and centralized identity management
- Azure Key Vault: Manages encryption keys for Transparent Data Encryption with Customer-Managed Keys
- Microsoft Defender for SQL: Delivers automated threat protection and database auditing

## Rationale
[This architecture ensures zero claim loss and sub-second performance while maintaining strict security and a one-day mainframe fallback capability.]