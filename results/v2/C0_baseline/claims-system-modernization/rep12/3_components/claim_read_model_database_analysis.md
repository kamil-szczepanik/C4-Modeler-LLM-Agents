## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL mainframe with a cloud-native Azure platform. It modernizes customer claim submissions and adjuster workflows while maintaining seamless hybrid coexistence with the legacy system of record.

## Key Elements
- **Claim Read Model Database:** Azure Cosmos DB container storing denormalized low-latency views.
- **Claim Document Store:** Cosmos DB Core/SQL API component for JSON claim models.
- **Change Feed Processor:** Asynchronous event synchronization component.
- **Schema Version Router:** Lightweight routing component for backward compatibility.
- **Integration & Anti-Corruption Layer:** .NET Core / MassTransit service bridging mainframe and cloud.
- **Adjuster Workspace:** React / .NET Core web application for claims processing.

## Relationships
- Integration & Anti-Corruption Layer -> Claim Document Store: Writes projected claim models [TCP/HTTPS]
- Change Feed Processor -> Claim Document Store: Manages state synchronization [Cosmos DB SDK]
- Adjuster Workspace -> Schema Version Router: Requests claim read models [HTTPS/REST]
- Schema Version Router -> Claim Document Store: Retrieves versioned documents [TCP/Cosmos DB SDK]

## Technology Stack
- Azure Cosmos DB: Multi-model NoSQL database ensuring sub-2-second UI responses despite mainframe latency.
- .NET Core & MassTransit: Integration framework for reliable event-driven data synchronization.
- Terraform: Infrastructure-as-Code tool for deploying database and security components to mitigate low cloud experience.
- Microsoft Entra ID: Identity provider enforcing RBAC and JWT validation for Active Directory SSO.

## Rationale
This architecture uses a hybrid event-driven Cosmos DB read model to bypass mainframe latency constraints while ensuring zero data loss. It empowers an inexperienced cloud team through serverless scaling, automated IaC, and robust version routing.