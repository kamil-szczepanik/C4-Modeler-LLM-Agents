## Overview
The system is a hybrid cloud-based Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern, scalable web application. Its core purpose is to enable online claim submissions and adjuster workflows while maintaining strict data consistency during incremental migrations.

## Key Elements
* Claim Data Access Component (Entity Framework Core)
* Migration Audit Log Component (Azure SQL Ledger)
* Reference Data Component (Azure SQL Database)
* Schema Versioning & Temporal Component (Azure SQL Temporal Tables)
* Outbox Event Dispatcher Component (Transactional Outbox pattern)
* Database Maintenance & Archival Component (T-SQL partitioning)

## Relationships
* Claims Core Service -> Claim Data Access Component: Reads and writes claim records [TDS (SQL)]
* Claims Core Service -> Schema Versioning & Temporal Component: Queries historical claim snapshots [Entity Framework / TDS]
* Outbox Event Dispatcher Component -> Message Broker: Publishes domain events [AMQP / Azure Service Bus SDK]
* Database Maintenance & Archival Component -> Claim Data Access Component: Manages table partitions and index maintenance [SQL / T-SQL]

## Technology Stack
* Azure SQL Database: Provides ACID compliance for strict consistency requirements (R-04)
* Azure SQL Ledger: Enables tamper-evident, cryptographically verifiable migration audit logs
* Azure SQL Temporal Tables: Native time-slicing to support rapid one-day claim-type rollbacks (R-06)
* Transactional Outbox Pattern: Guarantees atomic database writes and reliable messaging without distributed transactions

## Rationale
This architecture uses native Azure SQL features to ensure zero data loss and strict consistency during the complex hybrid migration. It delivers high-performance sub-2-second adjuster screens and rapid one-day rollbacks while keeping legacy mainframe integration costs minimal.