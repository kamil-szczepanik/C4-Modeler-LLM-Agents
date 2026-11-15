## Overview
[Azure Service Bus Premium] serves as the asynchronous messaging backbone for the Insurance Claims Modernization platform, ensuring reliable event streaming and decoupling between modern cloud components and the legacy mainframe. It guarantees operational consistency and compliance during the hybrid migration.

## Key Elements
- Azure Service Bus Premium Namespace
- Claim Events Topic (with SQL-filter rules per claim type)
- Legacy Sync Queue (with FIFO Session IDs mapping to Claim IDs)
- System Dead-Letter Sub-system (with DLQs and auto-forwarding)
- Private Endpoints and VNet Integration

## Relationships
- Backend APIs -> Azure Service Bus: Publishes domain events and commands [AMQP 1.0 over TLS 1.3]
- Migration & Sync Engine -> Azure Service Bus: Publishes and consumes sync events [AMQP 1.0 over TLS 1.3]
- Integration Workers -> Azure Service Bus: Consumes FIFO claim messages via sessions [AMQP 1.0 over TLS 1.3]
- Migration Operators -> Dead-Letter Sub-system: Tries, purges, and resubmits poisoned messages [Azure Portal / CLI]

## Technology Stack
- Azure Service Bus Premium Tier: Selected for guaranteed resource isolation, throughput, and disaster recovery.
- AMQP 1.0: Protocol used for efficient, bi-directional messaging across services.
- Microsoft Entra ID Managed Identities: Replaces static connection strings for secure, zero-trust authentication.
- Azure Private Link & Private Endpoints: Secures network traffic across the hybrid boundary, blocking public internet access.
- Bicep / Terraform: Infrastructure-as-Code for repeatable, automated deployments.

## Rationale
This architecture ensures zero claim loss or duplication (R-04) through persistent messaging, built-in duplicate detection, and robust dead-lettering. It accommodates the team's low cloud experience via managed infrastructure while supporting gradual, risk-free claim type migration (R-03).