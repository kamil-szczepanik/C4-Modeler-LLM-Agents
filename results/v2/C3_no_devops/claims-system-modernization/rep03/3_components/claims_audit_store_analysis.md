## Overview
- Architecture summary for the Claims Audit Store within the hybrid Insurance Claims Modernization platform.
- Provides tamper-proof, compliant event sourcing and long-term audit logging during the 3-year mainframe migration.

## Key Elements
- Claims Audit Store (Azure Cosmos DB): Append-only, immutable database container.
- Audit Event Writer (.NET Core / Cosmos SDK): Component handling PII tokenization and persistence.
- Compliance Query Service (.NET Core): Component providing secure, role-based query endpoints for auditors.
- Cosmos DB Change Feed Processor (.NET Core): Component powering asynchronous projections and archival triggers.
- Audit Archival Worker (Azure Function / .NET Core): Component moving historical logs to cold storage.
- Azure Blob Storage: Long-term WORM-compliant storage tier for 7-year retention.
- Azure Key Vault: Manages Customer-Managed Keys (CMK) and encryption keys.

## Relationships
- Claims Domain Services -> Audit Event Writer: Writes domain events via HTTPS (Document API)
- Finance/Compliance Auditors -> Compliance Query Service: Queries audit reports via HTTPS with Azure Active Directory SSO (R-07)
- Cosmos DB Change Feed Processor -> Audit Archival Worker: Triggers historical data offloading via internal Azure messaging
- Audit Archival Worker -> Azure Blob Storage: Archives immutable logs via HTTPS (Blob REST API)

## Technology Stack
- Azure Cosmos DB (SQL API & Analytical Store): Selected for low latency (R-05) and change feed capabilities.
- .NET Core: Used for containerized microservices and workers due to team familiarity.
- Azure Blob Storage (Cool/Archive tier with WORM): Provides cost-effective 7-year regulatory retention.
- Azure Key Vault: Secures data at rest via Customer-Managed Keys (CMK).
- Azure Monitor / Log Analytics: Generates immutable read-access audit logs.

## Rationale
- This architecture guarantees zero data loss and strict consistency (R-04) through immutable event storage and strict access controls. It offloads historical data to meet 7-year retention rules without impacting sub-second adjuster performance (R-05).