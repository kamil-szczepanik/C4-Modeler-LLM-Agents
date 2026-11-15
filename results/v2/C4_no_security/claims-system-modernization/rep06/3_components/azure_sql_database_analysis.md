## Overview
Azure SQL Database serves as the core transactional persistence layer for the new Insurance Claims Modernization platform. It enables gradual, risk-mitigated claim type migration from the legacy mainframe while ensuring high performance and data consistency.

## Key Elements
* Claims Transactional Store (Relational tables with Snapshot Isolation)
* Migration Routing & State Registry (Feature-flag tables for claim-type ownership)
* Transactional Outbox Table (Domain event buffer for reliable asynchronous messaging)
* Claims Processing Core & Integration/Anti-Corruption Layer (Java / Spring Boot container client)
* Azure Service Bus (Downstream event broker)

## Relationships
* Claims Processing Core -> Claims Transactional Store: Reads and writes transactional state [JDBC / TLS]
* Claims Processing Core -> Transactional Outbox Table: Atomically writes domain events [JDBC / TLS]
* Transactional Outbox Table -> Azure Service Bus: Relays synchronization and migration events [AMQP / TLS]

## Technology Stack
* Azure SQL Database (Paas, General Purpose Tier, Gen5, 4 vCores): Managed relational database minimizing operational overhead for a cloud-inexperienced team
* Transactional Outbox Pattern: Replaces complex CDC to guarantee reliable event dispatch without database-level streaming infrastructure
* Bicep / Terraform: Infrastructure-as-Code for automated, drift-free database deployments
* Point-in-Time Restore (PITR): Configured with 7-day retention for compliance and disaster recovery

## Rationale
This architecture guarantees strict transactional consistency (R-04) and sub-2-second adjuster screen performance (R-05) by caching migrated claims locally. Furthermore, the Outbox pattern and state registry directly support one-day claim type rollbacks (R-06) while respecting the team's limited cloud operational experience.