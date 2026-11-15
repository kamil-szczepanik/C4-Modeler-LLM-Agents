## Overview
The system is a modern cloud-based claims platform designed to gradually replace a legacy mainframe claims system for a regional insurer. It ensures seamless hybrid operations, strict data consistency, and rapid rollback capabilities during a multi-year migration.

## Key Elements
* **Claim Tables**: Core relational Azure SQL storage enforcing strict ACID guarantees for migrated claim types.
* **Sync Staging Tables**: Azure SQL staging area for asynchronous replication payloads managed by the integration worker.
* **Audit & Temporal History**: Azure SQL System-Versioned Temporal Tables tracking historical row versions for compliance and rollback.
* **Change Tracking Mechanism**: Azure SQL Change Tracking feature capturing row-level changes asynchronously without table locks.
* **Reconciliation & Rollback Views**: Azure SQL Views encapsulating complex JOINs to expose unified payload views for verification and rollback.

## Relationships
* **Claims Core Service** -> **Claim Tables & Audit History**: Executes domain queries via TDS over TLS (TCP 1433).
* **Integration & Sync Worker** -> **Sync Staging Tables**: Stages reconciliation data via TDS over TLS (TCP 1433).
* **Integration & Sync Worker** -> **Change Tracking Mechanism**: Polls delta changes via TDS over TLS (TCP 1433).
* **Integration & Sync Worker** -> **Reconciliation & Rollback Views**: Reads unified snapshots via TDS over TLS (TCP 1433).

## Technology Stack
* **Azure SQL Database Managed Instance**: Provides relational persistence and ACID consistency.
* **T-SQL**: Used for defining tables, views, and system tracking features.
* **TDS over TLS (TCP 1433)**: Secure protocol for all database connectivity.

## Rationale
This component architecture fits requirements by utilizing native database capabilities for change tracking and temporal history, ensuring zero data loss and strict consistency during hybrid synchronization. Furthermore, it supports the strict nightly batch window and enables rapid one-day rollbacks of migrated claim types to the legacy mainframe.