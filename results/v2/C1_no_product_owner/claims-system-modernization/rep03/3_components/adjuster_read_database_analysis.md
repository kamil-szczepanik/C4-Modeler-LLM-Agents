## Overview
The Adjuster Read Database provides a high-performance CQRS read model using Azure Cosmos DB to enable sub-2-second UI load times for claims adjusters. It supports a hybrid cloud migration strategy while ensuring zero data loss and strict security compliance.

## Key Elements
- Cosmos DB SQL API Container: Azure Cosmos DB instance hosting the read model
- Claims Collection: Cosmos DB Container partitioned by `ClaimId` for optimized query distribution
- Audit Collection: Cosmos DB Container storing immutable change logs for tracing
- Change Feed Processor: Cosmos DB Change Feed for downstream auditing and triggers
- Private Endpoint: Azure Private Endpoint ensuring isolated network access

## Relationships
- Read Model Projector -> Claims Collection: Upserts denormalized documents via [Cosmos DB SDK / TCP]
- API Gateway -> Claims Collection: Executes point-reads and queries via [Cosmos DB SDK / TCP]
- Read Model Projector -> Change Feed Processor: Triggers event processing via [Cosmos DB Change Feed]

## Technology Stack
- Azure Cosmos DB (SQL API): Selected for global distribution and low-latency NoSQL document storage meeting R-05 performance requirements
- Azure AD RBAC & Managed Identities: Replaces master key connection strings for secure least-privilege access
- Azure Key Vault: Provides Customer-Managed Keys (CMK) for encryption at rest for data and backups
- Azure Virtual Network & Private Endpoints: Secures database traffic by disabling public network access

## Rationale
This architecture resolves the team's lack of cloud experience by enforcing strict infrastructure-as-code, continuous backups, and private networking. It guarantees high availability, sub-2s query performance, and robust security isolation required during the legacy mainframe migration.