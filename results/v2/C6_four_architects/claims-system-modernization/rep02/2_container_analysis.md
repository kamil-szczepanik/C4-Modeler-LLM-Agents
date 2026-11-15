## Overview
This hybrid cloud architecture modernizes a legacy regional insurer's claims platform by incrementally migrating claim types from an on-premises mainframe to Microsoft Azure. It ensures continuous processing, strict data consistency, and low-latency adjuster experiences while maintaining the legacy system of record.

## Key Elements
*   **Web Portal**: React on Azure Static Web Apps for customer and broker claim submission.
*   **Adjuster Workspace**: React on Azure App Service with asynchronous caching for claims handlers.
*   **API Management Proxy**: Azure API Management handling routing and Azure AD (Entra ID) SSO.
*   **Claims Processing Service**: Java / Spring Boot on Azure Container Apps for core domain logic.
*   **Claim Routing Service**: Azure Service Bus managing messaging and fallback routing.
*   **Primary Datastore**: Azure SQL Database providing ACID compliance for the new platform.
*   **Claim Read Model Store**: Azure Cosmos DB / Redis providing read-optimized projections.
*   **Mainframe Integration Adapter**: IBM MQ on-premises managing legacy batch integration.
*   **Data Sync Worker**: Java / Spring Boot on Azure Container Apps handling state reconciliation.
*   **Audit and Reconciliation Service**: Azure Functions cross-referencing state to prevent discrepancies.

## Relationships
*   **Clients to API Gateway**: HTTPS/TLS for secure web portal and adjuster traffic.
*   **API Gateway to Services**: Internal mTLS for service-to-service communication.
*   **Processing Service to Datastore**: TDS over TLS for relational transactional persistence.
*   **Processing Service to Read Store**: Change Data Capture (CDC) and domain events via Azure Service Bus.
*   **Mainframe to Adapter**: AMQP over Azure ExpressRoute/VPN for hybrid synchronization.

## Technology Stack
*   **Azure Static Web Apps / App Service (React)**: Chosen for rapid frontend delivery and low cloud-experience team onboarding.
*   **Azure Container Apps (Java / Spring Boot)**: Selected for scalable, managed microservices execution.
*   **Azure SQL Database & Cosmos DB**: Chosen to balance strict transactional ACID consistency with high-performance read projections.
*   **Azure Service Bus & IBM MQ**: Selected to guarantee reliable asynchronous messaging and hybrid mainframe integration.

## Rationale
The hybrid architecture isolates fragile legacy components while utilizing managed Azure services to meet strict performance and consistency constraints. Asynchronous messaging and decoupled read models successfully shield modern microservices from mainframe latency and migration risks.