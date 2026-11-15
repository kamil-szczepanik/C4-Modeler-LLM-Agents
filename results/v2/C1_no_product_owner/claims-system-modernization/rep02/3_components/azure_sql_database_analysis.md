## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy mainframe with a modern Azure-based platform. Its core purpose is to process and migrate claims incrementally while maintaining synchronization with the on-premise legacy system.

## Key Elements
- Claim Entity Store (Relational Tables, Temporal Tables)
- Data Access Layer (Spring Data JPA, Hibernate)
- Migration & Audit Sync Component (SQL Stored Procedures, Change Data Capture)
- Adjuster Backend Service (Java, Spring Boot)
- Azure SQL Database (Azure SQL Database)

## Relationships
- Adjuster Backend Service -> Data Access Layer: Invokes domain repositories [In-process / Java Method Call]
- Data Access Layer -> Claim Entity Store: Executes queries and updates [TDS / TCP Port 1433]
- Adjuster Backend Service -> Migration & Audit Sync Component: Queries migration sync status [In-process / Java Method Call]
- Migration & Audit Sync Component -> Claim Entity Store: Reads/writes audit logs and temporal history [Internal SQL]

## Technology Stack
- Azure SQL Database: Provides managed relational persistence with high availability and automated failover.
- Temporal Tables: Enables point-in-time auditing and supports quick rollback requirements.
- Change Data Capture (CDC): Tracks data changes for migration synchronization and reconciliation.
- Spring Data JPA / Hibernate: Manages object-relational mapping and data access transactions.
- Azure Active Directory & Managed Identities: Secures database authentication without embedding credentials.

## Rationale
This architecture uses temporal tables and CDC within Azure SQL Database to guarantee zero data loss and enable rapid 1-day rollbacks. The secure, isolated database design meets strict compliance and performance SLAs for adjusters despite hybrid constraints.