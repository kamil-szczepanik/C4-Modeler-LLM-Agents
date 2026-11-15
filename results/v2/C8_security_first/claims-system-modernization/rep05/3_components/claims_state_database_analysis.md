## Overview
This architecture summary outlines the modern Claims State Database for an insurance claims modernization initiative. It provides a secure, ACID-compliant data store enabling hybrid coexistence between a legacy mainframe and a new cloud platform.

## Key Elements
- **Claims State Database Container**: Azure SQL Database (PaaS) serving as the transactional data store.
- **Transactional Store Component**: Manages ACID compliance and relational integrity.
- **Outbox Table Component**: Implements the Transactional Outbox pattern for zero data loss.
- **Audit Log Component**: Captures immutable change history for compliance.
- **Versioned State Schema Component**: Tracks metadata like source system and version for 1-day rollbacks.
- **Change Data Capture (CDC) Component**: Streams state changes for downstream event publishing.

## Relationships
- **Claims Orchestrator Container** -> **Transactional Store Component**: Reads and writes claim aggregates [T-SQL via TDS / Azure Managed Identity, Port 1433]
- **Claims Orchestrator Container** -> **Outbox Table Component**: Writes transactional events atomically [T-SQL]
- **Claims Orchestrator Container** -> **Versioned State Schema Component**: Reads and updates claim aggregates [T-SQL via TDS]

## Technology Stack
- **Azure SQL Database (PaaS)**: Chosen to guarantee ACID compliance for financial state.
- **Azure Managed Identities**: Eliminates connection string secrets for secure database access.
- **Azure Virtual Network & Private Endpoints**: Secures network isolation by blocking public internet access.
- **Flyway / DbUp**: Automates database migrations via CI/CD pipelines.

## Rationale
This architecture ensures zero data loss and supports rapid adjuster screens under 2 seconds during the 3-year hybrid migration phase. It also enables seamless 1-day rollbacks of claim types to the legacy mainframe while accommodating the team's cloud skill level.