## Overview
[The system is a hybrid insurance claims modernization platform that gradually replaces a legacy mainframe with an Azure cloud environment. Its core purpose is to maintain secure, immutable audit trails across both systems during the three-year migration.]

## Key Elements
- [Compliance & Audit Officers]
- [Claims Integration Service]
- [Adjuster Workspace]
- [Audit Ingestion Function (Azure Function / .NET Core)]
- [Compliance Indexing & Query API (Azure Function / .NET Core)]
- [Audit Export & Retention Worker (Azure Function / .NET Core)]
- [Audit Data Store (Azure Cosmos DB - SQL API)]
- [Azure Blob Storage]

## Relationships
- [Claims Integration Service -> Audit Ingestion Function: POST /api/audit via HTTPS/JSON]
- [Audit Ingestion Function -> Audit Data Store: Writes immutable audit events via Cosmos DB SDK / TCP]
- [Compliance & Audit Officers -> Compliance Indexing & Query API: Queries audit reports via HTTPS / Azure Front Door]
- [Audit Export & Retention Worker -> Audit Data Store: Reads expired logs via Cosmos DB Change Feed / TCP]
- [Audit Export & Retention Worker -> Azure Blob Storage: Archives immutable snapshots via HTTPS / Azure Blob SDK]
- [Compliance Indexing & Query API -> Audit Data Store: Queries hot compliance data via Cosmos DB SQL API / TCP]

## Technology Stack
- [Azure Functions (.NET Core): Serverless compute for ingestion, querying, and exporting audit data, lowering operational overhead for a low-experience cloud team.]
- [Azure Cosmos DB (SQL API): NoSQL document store utilizing time-to-live (TTL), change feeds, and continuous backups for scalable, tamper-evident audit logs.]
- [Azure Blob Storage: Cost-effective cold storage with immutable time-based retention policies for long-term audit archiving.]
- [Azure Managed Identities & Private Endpoints: Secure identity-based authentication and network isolation replacing public internet exposure and API keys.]

## Rationale
[This architecture fits requirements by decoupling audit ingestion, querying, and retention into resilient Azure Functions backed by Cosmos DB and Blob Storage. It guarantees regulatory compliance, zero data loss (R-04), and tamper-evidence through WORM patterns while operating effectively within a hybrid migration constraint.]