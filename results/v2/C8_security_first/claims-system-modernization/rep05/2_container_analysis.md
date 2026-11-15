## Overview
Gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform using a Strangler Fig pattern. The system ensures continuous operations, sub-second UI responsiveness, and zero data loss during migration.

## Key Elements
*   **Users:** End Customers & Brokers, Claims Adjusters, Operations & Migration Team
*   **Frontend Containers:** Customer Portal Container, Adjuster Web App Container (Next.js/React)
*   **Gateway & Core Containers:** API Gateway (Azure Front Door / APIM), Claims Orchestrator Container (Node.js/.NET Core)
*   **Integration & Data Containers:** Legacy Mainframe Adapter Container, Claims State Database (Azure SQL / Azure Cosmos DB)
*   **External Systems & Services:** Legacy Mainframe (CICS/MQ), Microsoft Entra ID, Azure Service Bus, Azure Key Vault

## Relationships
*   **Users to Frontends:** HTTPS/REST over TLS 1.3
*   **Frontends to API Gateway:** HTTPS/REST with OIDC token validation via Microsoft Entra ID
*   **API Gateway to Core Containers:** HTTPS/REST and gRPC
*   **Orchestrator to Mainframe Adapter:** Asynchronous messaging via Azure Service Bus and synchronous gRPC
*   **Mainframe Adapter to Legacy Mainframe:** CICS/MQ protocols over Site-to-Site VPN / Azure ExpressRoute with mTLS

## Technology Stack
*   **Cloud Provider:** Hybrid (On-premise mainframe and Azure West Europe)
*   **Compute:** Azure Container Apps to abstract Kubernetes complexity for a team with limited cloud experience
*   **Databases:** Azure SQL / Azure Cosmos DB for enterprise-grade transactional consistency and Transactional Outbox pattern
*   **Integration & Messaging:** Azure Service Bus to queue messages during the 23:00–05:00 mainframe batch window
*   **Security & Identity:** Microsoft Entra ID with OpenID Connect (OIDC) and Azure Key Vault for customer-managed encryption keys (CMK)
*   **Observability:** Azure Application Insights / OpenTelemetry for distributed tracing and synthetic monitoring

## Rationale
This architecture decouples modern web applications from legacy mainframe latencies using asynchronous queuing and an anti-corruption layer, satisfying strict performance and consistency constraints. Containerizing workloads on Azure Container Apps minimizes operational overhead while enabling seamless blue/green rollbacks within one day if migrated claim types fail.