## Overview
- Hybrid insurance claims modernization platform replacing a 30-year-old mainframe.
- Azure SQL Database providing transactional persistence and synchronization for incrementally migrated claims.

## Key Elements
- Azure SQL Database (Managed relational data store in Azure West Europe)
- Claim Data Store (Extensible relational tables)
- Audit & Security Subsystem (Row-Level Security and Azure SQL Audit)
- Change Data Capture / CDC (Row-level change emitter)
- Partitioning & Retention Engine (Sliding window table partitioning)
- Read-Only Replica Routing (Secondary read endpoint)

## Relationships
- Claims Core Processing Service -> Azure SQL Database: Reads and writes claim data via T-SQL / TDS (TLS 1.3)
- Mainframe Integration Adapter -> Azure SQL Database: Synchronizes state via T-SQL / TDS Change Data Capture
- Reporting / Compliance Tools -> Azure SQL Database: Queries analytical data via Read-Only Replica T-SQL / TDS
- Partitioning Engine -> Azure Blob Storage: Archives historical claims via External Tables / Managed Backup

## Technology Stack
- Azure SQL Database: Fully managed service mitigating low team cloud experience
- Azure AD / Managed Identities: Secure passwordless authentication eliminating hardcoded connection strings
- Azure Blob Storage: Cost-effective tier for historical claim archiving
- Bicep / Terraform & Flyway: Infrastructure-as-Code and automated database migration pipelines ensuring rollback safety

## Rationale
- Managed Azure SQL features reduce operational overhead for a team with limited cloud experience while ensuring rapid one-day rollbacks.
- Read replicas and partitioning protect critical performance constraints, maintaining sub-second UI loads and preserving the rigid nightly batch window.