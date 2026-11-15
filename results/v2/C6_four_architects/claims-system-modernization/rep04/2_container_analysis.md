## Overview
This hybrid cloud architecture gradually modernizes a legacy insurance claims platform while keeping the COBOL/DB2 mainframe as the system of record. It decouples modern user experiences from legacy constraints using asynchronous messaging and a robust anti-corruption layer.

## Key Elements
*   **Clients**: Customers, Brokers, and Claims Adjusters using the system.
*   **Frontend**: React SPA hosted in Azure Static Web Apps.
*   **Edge Tier**: Azure API Management & Node.js/TypeScript BFF.
*   **Application Tier**: Modern Claims Service, Routing Service / Anti-Corruption Layer (ACL), and Azure Functions (Document & Notification Workers) running on Azure Container Apps.
*   **Data Tier**: Azure Database for PostgreSQL (supporting transactional storage and CQRS read models).
*   **Integration Tier**: Azure Service Bus and Azure Relay.
*   **Hybrid Bridge**: On-premise Spring Boot Mainframe Adapter and IBM DB2/COBOL Mainframe.
*   **External Systems**: Azure Active Directory / Entra ID, Document Management System, Core Banking / Payout System, and Notification Service.

## Relationships
*   **Clients to Frontend**: HTTPS.
*   **Frontend to Edge Tier**: HTTPS / OIDC (Entra ID for SSO).
*   **Edge Tier to Application Tier**: gRPC and HTTPS/REST.
*   **Application Services to Integration**: AMQP via Azure Service Bus.
*   **Cloud to On-Premises**: Azure Relay / VPN Gateway bridging Azure Service Bus to the Mainframe Adapter.
*   **Mainframe Adapter to Legacy Mainframe**: IBM MQ and DB2 queries.

## Technology Stack
*   **Frontend**: React, Azure Static Web Apps (chosen for modern UI and ease of hosting).
*   **Edge**: Azure API Management, Node.js/TypeScript (for request orchestration and security).
*   **Backend Services**: Java/Spring Boot on Azure Container Apps, Python/C# Azure Functions (chosen for robust enterprise capabilities and team familiarity).
*   **Database**: Azure Database for PostgreSQL (standardized to simplify operations given low cloud experience).
*   **Messaging & Integration**: Azure Service Bus and Azure Relay (provides a gentler learning curve than Kafka and native hybrid connectivity).
*   **Security**: Azure Active Directory / Entra ID via OAuth2/OIDC.

## Rationale
This architecture isolates the expensive and constrained legacy mainframe using an on-premise adapter and asynchronous service bus messaging, ensuring nightly batch windows and change budgets are respected. Standardizing on managed PostgreSQL and Azure Service Bus minimizes operational complexity for a team with limited cloud experience while meeting strict performance, consistency, and one-day fallback requirements.