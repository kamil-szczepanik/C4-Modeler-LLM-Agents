## Overview
[System: Insurance Claims Modernization platform. Core purpose: Gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform.]

## Key Elements
- Claim Transactional Engine (Azure SQL Core)
- Mainframe-Compatibility Schema Adapter
- Audit Trail Log Table
- Row-Level Security (RLS) & Partitioning Manager
- Temporal Table Archival Engine

## Relationships
- Claims Processing Service -> Claim Transactional Engine: Relational transactional persistence [TDS over TLS]
- Data Sync Worker -> Temporal Table Archival Engine: Reconciles state [TDS over TLS]
- Audit and Reconciliation Service -> Audit Trail Log Table: Cross-references state [TDS over TLS]

## Technology Stack
- Azure SQL Database: Provides relational storage, ACID compliance, and low operational overhead for a team with limited cloud experience.
- TDS over TLS: Secures database communication protocols.
- Azure SQL Temporal Tables: Automatically tracks historical row versions to support rollbacks and auditing.

## Rationale
[This architecture uses a decomposed Azure SQL Database with native features to ensure strict data consistency and seamless one-day mainframe fallbacks without distributed transaction complexity. It balances robust hybrid security with minimal operational overhead for a cloud-novice team.]