## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It ensures zero data loss, supports incremental claim type migration, and respects strict legacy batch windows.

## Key Elements
- **Claims Data Model**: Relational tables and schemas structured per claim type using Entity Framework Core Migrations.
- **Data Access Layer**: .NET 8 libraries implementing Repository and Unit of Work patterns.
- **Database Security & Auditing**: Azure SQL Transparent Data Encryption, Row-Level Security, and Audit logs.
- **Temporal Tables**: SQL Server System-Versioning for immutable historical audit trails.
- **Mainframe Sync Staging Tables**: Dedicated schemas for buffering bi-directional state changes.
- **Stored Procedures & Database Triggers**: T-SQL routines for high-performance batch processing and validation.

## Relationships
- **Claims Core Service** -> **Data Access Layer**: In-process method calls [C# / Entity Framework Core]
- **Data Access Layer** -> **Claims Data Model**: Queries and transactions [T-SQL]
- **Azure Data Factory** -> **Mainframe Sync Staging Tables**: Bulk copy operations [Bulk Insert / T-SQL]
- **Mainframe Integration Adapter** -> **Mainframe Sync Staging Tables**: Read/Write sync states [T-SQL via EF Core]
- **Audit & Compliance System** -> **Database Security & Auditing**: Direct log scraping [Azure Monitor / SQL Audit Output]

## Technology Stack
- **Azure SQL Database**: ACID-compliant transactional persistence layer ensuring zero data loss.
- **Entity Framework Core**: ORM for managing relational mappings and LINQ-based data access.
- **T-SQL**: Procedural language used for bulk inserts, triggers, and stored procedures within the batch window.
- **SQL Server System-Versioning**: Built-in temporal tables for automated historical tracking.

## Rationale
This architecture uses hybrid database patterns, staging tables, and temporal versioning to decouple the modern Azure platform from the legacy mainframe. It guarantees strict ACID consistency and rapid rollback capabilities within fixed operational constraints.