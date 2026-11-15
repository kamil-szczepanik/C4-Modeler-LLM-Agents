## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform on Azure West Europe. It ensures zero claim loss or duplication while maintaining independent processing for migrated claim types.

## Key Elements
- **Claim Event Topic (`claim-events`)**: Azure Service Bus Topic for pub-sub distribution of domain events.
- **Mainframe Outbox Queue (`mainframe-outbox`)**: Azure Service Bus Queue with Sessions for ordered transactions.
- **Dead-Letter Handler**: Built-in Service Bus DLQ with automated Azure Monitor alerting via PagerDuty.
- **Retry & Backoff Policy Engine**: Native Service Bus exponential backoff configured with a `MaxDeliveryCount` ceiling of 5 retries.

## Relationships
- Claims Core Service -> Claim Event Topic: Publishes domain events [AMQP over TLS, Azure RBAC Managed Identity]
- Mainframe Integration Adapter -> Mainframe Outbox Queue: Consumes ordered sync commands using Session IDs [AMQP over TLS, Azure RBAC Managed Identity]
- Mainframe Integration Adapter -> Dead-Letter Handler: Inspects and re-queues poisoned messages [AMQP over TLS]

## Technology Stack
- **Azure Service Bus**: Chosen for reliable, transactional asynchronous messaging across the hybrid boundary.
- **Azure Private Link / Private Endpoints**: Secures the broker namespace, preventing exposure over the public internet.
- **Azure Key Vault (CMK)**: Provides customer-managed keys for encryption-at-rest.
- **Terraform**: Automates drift-free infrastructure provisioning for queues, topics, and access controls.

## Rationale
This architecture ensures strict transactional consistency and zero data loss during hybrid migration while protecting the fragile, expensive-to-change mainframe. It utilizes managed cloud services to compensate for the team's limited cloud experience.