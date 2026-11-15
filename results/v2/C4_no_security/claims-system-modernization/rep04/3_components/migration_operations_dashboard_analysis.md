## Overview
The Migration Operations Dashboard provides real-time monitoring and discrepancy detection for the hybrid Insurance Claims Modernization platform. It ensures zero data loss and supports rapid rollback decisions during the phased migration from the legacy mainframe.

## Key Elements
- Migration Leads and Operations Managers (Primary Users)
- Dashboard UI (React SPA)
- Dashboard BFF / API (Node.js/Express)
- Reconciliation Processor (Python/Pandas)
- Compliance & Audit Component (Node.js / Serverless)
- Operations Datastore (Azure PostgreSQL)
- Asynchronous Batch Staging Queue (Azure Blob Storage)

## Relationships
- Migration Leads & Operations Managers -> Dashboard UI: Monitors migration progress and discrepancy alerts via HTTPS/WSS
- Dashboard UI -> Dashboard BFF / API: Fetches aggregated metrics and audit logs via HTTPS/REST/GraphQL
- Dashboard BFF / API -> Operations Datastore: Queries audit logs and discrepancy states via SQL/TLS
- Reconciliation Processor -> Operations Datastore: Persists audit logs and discrepancy states via SQL/TLS
- Reconciliation Processor -> Asynchronous Batch Staging Queue: Buffers mainframe batch dumps via Azure Blob SDK/HTTPS
- Polyglot Persistence Layer -> Reconciliation Processor: Streams real-time updates via Change Data Capture (CDC)

## Technology Stack
- React SPA: Matches the Customer Portal stack to reduce cognitive load for low-cloud-experience teams
- Node.js/Express BFF: Provides familiar backend development patterns matching existing services
- Python/Pandas Reconciliation Processor: Delivers powerful data validation capabilities for cross-system comparisons
- Azure PostgreSQL: Ensures robust relational integrity, audit tracking, and Row-Level Security
- Azure Blob Storage: Buffers heavy mainframe batch extracts during the 23:00-05:00 window to prevent resource contention

## Rationale
This architecture minimizes operational risk by using familiar technologies that align with the team's skillset. It isolates heavy batch workloads while providing reliable, auditable governance to safely manage the hybrid mainframe-to-cloud migration.