## Overview
[The Claim Reconciliation Service ensures data consistency between the modern Azure-hosted platform and the legacy mainframe during hybrid migration. It prevents data loss, manages state synchronization safely outside batch windows, and surfaces discrepancies to compliance officers and adjusters.]

## Key Elements
- Claim Reconciliation Service (Azure AKS, .NET)
- Azure Service Bus (Topics & Dead-Letter Queues)
- Azure Blob Storage (Immutable WORM storage)
- COBOL/DB2 Mainframe (On-premises System of Record)
- Claims Web App (Azure AKS)
- Azure Active Directory / Entra ID

## Relationships
- Claim Reconciliation Service -> COBOL/DB2 Mainframe: Asynchronous state verification via read-replicas/CDC [mTLS]
- Claim Reconciliation Service -> Azure Service Bus: Publishes discrepancy events [TLS 1.3]
- Azure Service Bus -> Claims Web App: Asynchronously delivers reconciliation alerts [TLS 1.3]
- Claim Reconciliation Service -> Azure Blob Storage: Writes cryptographically signed, PII-masked audit trails [HTTPS]
- Claims Web App -> Azure Active Directory: RBAC authentication for compliance and adjuster dashboards [OAuth 2.0 / OIDC]

## Technology Stack
- Azure AKS (.NET): Containerized runtime for scalable reconciliation workers
- Azure Service Bus: Asynchronous messaging with dead-letter queues to decouple services and prevent cascading failures
- Azure Blob Storage (WORM): Immutable storage ensuring non-repudiable, tamper-proof audit trails
- Azure Active Directory (Entra ID): Centralized Identity and Access Management for strict RBAC/ABAC enforcement

## Rationale
- This architecture isolates the brittle mainframe from active transactional queries during the strict 23:00-05:00 batch window using asynchronous patterns. It directly satisfies R-04 (consistency) and R-06 (rapid rollback) while accommodating the team's limited cloud experience through robust managed Azure services.