## Overview
[This system modernizes a regional insurer's claims platform by gradually migrating claims from a legacy COBOL/DB2 mainframe to a hybrid cloud architecture. It ensures zero claim loss and rapid rollback capabilities while keeping the legacy system operational.]

## Key Elements
* Claim Translation Component (.NET 8 Azure Function)
* Mainframe Adapter (.NET 8 Azure Function with Polly)
* Sync & Reconciliation Router (Azure Service Bus & Event Grid)
* Routing Registry Component (Azure App Configuration)
* Legacy Mainframe (On-premise COBOL/DB2 system of record)

## Relationships
* API Gateway & BFF -> Claim Translation Component [mTLS and HTTPS/JSON]
* Claim Translation Component -> Sync & Reconciliation Router [AMQP]
* Sync & Reconciliation Router -> Mainframe Adapter [AMQP]
* Mainframe Adapter -> Legacy Mainframe [HTTPS over Secure VPN/ExpressRoute]
* Claim Translation Component -> Routing Registry Component [REST/HTTPS]

## Technology Stack
* Azure Functions (.NET 8 / C#): Serverless execution for claim translation and mainframe adaptation
* Azure Service Bus & Event Grid: Asynchronous messaging with dead-letter queues to guarantee consistency
* Azure App Configuration: Dynamic feature flags for one-day claim-type rollbacks
* Azure Key Vault & Managed Identities: Secure credential storage and service-to-service authentication
* Polly Library: Circuit-breakers and retry policies for mainframe latency handling

## Rationale
[This hybrid architecture abstracts rigid mainframe dependencies behind resilient asynchronous queues and dynamic routing registries. It directly satisfies stringent consistency, security, and rollback requirements despite the team's limited cloud experience.]