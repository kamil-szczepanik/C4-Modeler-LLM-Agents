## Overview
[System: Insurance Claims Modernization Platform] Modern platform gradually replacing a 30-year-old COBOL/DB2 mainframe claims system via a hybrid cloud architecture.

## Key Elements
- **Claims Registry Table**: PostgreSQL / Azure SQL relational tables
- **Operational Read-Model Cache**: Denormalized tables
- **Sync-State Ledger**: Transactional tables
- **Audit Logging Subsystem**: PostgreSQL pgaudit / Azure SQL Ledger / Temporal Tables
- **Consumers & Producers**: Claims API Gateway / BFF, Integration & Sync Service, Audit & Event Store

## Relationships
- **Integration & Sync Service** -> **Sync-State Ledger** & **Claims Registry Table** (via ADO.NET / pgsql over TLS via Azure Private Endpoints)
- **Claims API Gateway / BFF** -> **Operational Read-Model Cache** (via SQL queries via Azure Private Endpoints)
- **Operational Datastore** -> **Audit & Event Store** (via PostgreSQL logical replication / Azure SQL Change Data Capture over TLS)

## Technology Stack
- **Azure SQL Database / PostgreSQL on Azure**: Chosen as the operational datastore for state tracking and low-latency reads.
- **Azure Private Endpoints & Managed Identities**: Mandated for secure, credential-free network isolation and access control.
- **Transparent Data Encryption (TDE) with Customer-Managed Keys**: Used for secure data-at-rest encryption via Azure Key Vault.
- **Azure SQL Ledger / PostgreSQL pgaudit & WORM Blob Storage**: Selected to enforce immutable compliance audit logs.

## Rationale
[This architecture fits the requirements by maintaining a hybrid bridge that guarantees zero data loss and exact claim routing during the 3-year mainframe migration window while delivering sub-2-second UI performance. It embeds strict security controls, automated recovery, and audit capabilities tailored for an insurance system of record.]