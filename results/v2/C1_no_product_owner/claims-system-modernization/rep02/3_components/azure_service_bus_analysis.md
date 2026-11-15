## Overview
[The hybrid Azure Service Bus messaging architecture coordinates claims modernization by routing asynchronous events between the legacy on-premises COBOL/DB2 mainframe and the new Azure cloud platform. It ensures zero claim loss (R-04) and rapid one-day rollbacks (R-06) while respecting the 23:00-05:00 batch window constraints.]

## Key Elements
- **Topic Router Component**: Inspects incoming claim messages and routes them to type-specific subscriptions using Azure Service Bus Topics.
- **Modernization Switcher Component**: Evaluates dynamic routing rules to direct migrated claim types to cloud handlers and unmigrated types to the mainframe.
- **Mainframe Sync Queue Component**: Buffers messages destined for the mainframe to handle backpressure during the batch window.
- **Dead-Letter Handler Component**: Captures poisoned messages exceeding max delivery retries into a secure Dead-Letter Queue (DLQ).
- **Azure App Configuration**: Stores migration feature flags for the Modernization Switcher.

## Relationships
- **Adjuster Backend Service -> Topic Router Component**: Publishes claim events via AMQP over TLS.
- **Topic Router Component -> Modernization Switcher Component**: Evaluates claim type migration status via In-Memory calls.
- **Topic Router Component -> Mainframe Sync Queue Component**: Forwards unmigrated claim payloads via AMQP.
- **Mainframe Sync Queue Component -> Mainframe Integration Adapter**: Delivers buffered payloads via AMQP.

## Technology Stack
- **Azure Service Bus**: Core messaging broker chosen for enterprise reliability, AMQP protocol support, and built-in DLQ capabilities.
- **Azure App Configuration**: Stores feature flags to enable one-day rollback (R-06) without code deployments.
- **Microsoft Entra ID (RBAC)**: Replaces SAS keys to enforce least-privilege managed identity access.
- **Azure Key Vault & Customer-Managed Keys (CMK)**: Provides encryption-at-rest for messaging data and configuration.
- **Private Endpoints & TLS 1.3**: Secures hybrid network traffic and prevents public internet exposure.
- **Bicep/Terraform**: Ensures automated, repeatable Infrastructure-as-Code deployments.

## Rationale
[This architecture fits the requirements by decoupling cloud and legacy workflows via asynchronous messaging, protecting the fragile mainframe from traffic spikes. Additionally, it empowers a team with low cloud experience through managed Azure PaaS services, automated Bicep provisioning, and centralized feature flags.]