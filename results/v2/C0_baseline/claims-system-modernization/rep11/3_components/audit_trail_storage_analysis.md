## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform via a hybrid Azure cloud migration. It ensures non-repudiation and regulatory compliance for hybrid claim processing.]

## Key Elements
*   [Compliance Officers and External Auditors]
*   [Customer Support]
*   [Audit Trail Storage Container (Azure Blob Storage)]
*   [Event Ingestion Route (Azure Event Grid and Azure Service Bus)]
*   [Security & Access (Azure Key Vault and Azure AD RBAC)]

## Relationships
*   [Claims API and Mainframe Adapter -> Azure Service Bus: Publishes business audit events [AMQP]]
*   [Azure Service Bus -> Azure Event Grid: Triggers event routing [Managed Azure Integration]]
*   [Azure Event Grid -> Azure Blob Storage: Writes immutable audit logs [HTTPS / Blob REST API]]
*   [Compliance Officers -> Azure Blob Storage: Read-only access for auditing [Azure AD RBAC / HTTPS]]

## Technology Stack
*   [Azure Blob Storage: Immutable WORM storage with 7+ year Time-Based Retention for regulatory compliance]
*   [Azure Event Grid & Service Bus: Serverless ingestion pipeline to minimize custom code for low-cloud-experience team]
*   [Azure Key Vault: Encryption-at-rest using Customer-Managed Keys (CMK) with annual rotation]
*   [Azure AD RBAC & Private Link: Strict least-privilege access control and network isolation]

## Rationale
[Serverless managed Azure services reduce operational risk and maintenance overhead for a team with low cloud experience. Immutable WORM storage guarantees strict compliance and satisfies R-04 by preventing data loss or tampering during migration.]