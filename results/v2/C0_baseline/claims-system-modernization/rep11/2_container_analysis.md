## Overview
A hybrid cloud architecture gradually modernizes a legacy COBOL/DB2 mainframe insurance claims system while maintaining business continuity. It decouples legacy latency using an asynchronous event-driven platform hosted in Azure West Europe alongside the on-premise mainframe.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters, Operations Managers
- Frontends: Web Portal (SPA), Adjuster Portal (SPA), Dispute & Exception Dashboard
- Core Services: Claims API (BFF), Mainframe Adapter, Feature Flag / Routing Service
- Infrastructure & Storage: Azure Kubernetes Service (AKS), Azure Service Bus, Azure Cosmos DB, Azure App Configuration, Azure Blob Storage / SQL, Azure Key Vault

## Relationships
- Customers & Brokers interact with the Web Portal via HTTPS (TLS 1.3)
- Claims Adjusters interact with the Adjuster Portal via HTTPS (TLS 1.3)
- Portals communicate with the Claims API (BFF) via REST over HTTPS with OAuth 2.0 / OIDC (Azure AD)
- Claims API interacts with Azure Cosmos DB via TCP/TLS for read-model caching and Azure App Configuration for routing rules
- Claims API publishes messages to Azure Service Bus via AMQP/HTTPS
- Mainframe Adapter syncs data with Azure Service Bus and communicates with the on-premise COBOL/DB2 mainframe via mutually authenticated TLS (mTLS) over Azure ExpressRoute/VPN
- Business Audit Trail consumes immutable events into Azure Blob Storage / SQL

## Technology Stack
- Frontend: React hosted on Azure Static Web Apps for responsive user interfaces
- Backend: Node.js/TypeScript in Azure Kubernetes Service (AKS) for the Claims API (BFF) and Mainframe Adapter
- Messaging & Integration: Azure Service Bus for reliable, asynchronous event-driven processing
- Storage & Caching: Azure Cosmos DB for low-latency read models; Azure Blob Storage / SQL for audit trails
- Configuration & Security: Azure App Configuration for dynamic claim-type routing; Azure Key Vault with Managed Identities for secret management

## Rationale
This hybrid architecture isolates expensive mainframe changes and bridges legacy 5-second latencies through asynchronous messaging and local caching to achieve sub-2-second adjuster screens. Managed Azure services reduce operational risk for a team with low cloud experience while ensuring zero claim loss and enabling rapid one-day rollbacks per claim type.