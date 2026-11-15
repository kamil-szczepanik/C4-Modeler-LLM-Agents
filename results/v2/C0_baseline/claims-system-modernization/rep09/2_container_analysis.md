## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted application. It enables online claim submission and adjuster workflows while maintaining synchronization with the legacy system of record.

## Key Elements
*   **Customers & Brokers:** External users submitting and tracking claims online.
*   **Claims Adjusters:** Internal users managing claims via the new web application.
*   **Customer Portal & Adjuster Workspace:** React Single Page Applications hosted in Azure Static Web Apps.
*   **Azure Container Apps (ACA):** Unified serverless container runtime hosting backend APIs, the Migration & Sync Engine, and Integration Workers.
*   **Azure API Management (APIM):** Secure gateway managing traffic and enforcing mTLS with the on-premise mainframe.
*   **Azure Service Bus:** Messaging backbone supporting asynchronous CQRS and reliable event streaming.
*   **Azure SQL Database:** Modern datastore utilizing Entity Framework Core.
*   **Legacy Mainframe:** On-premise COBOL/DB2 system of record.

## Relationships
*   Customers and Brokers interact with the Customer Portal via HTTPS/JSON.
*   Claims Adjusters interact with the Adjuster Workspace via HTTPS/JSON.
*   All external and frontend traffic routes through Azure API Management (APIM) using HTTPS.
*   Backend ACA containers communicate asynchronously using Azure Service Bus queues and topics.
*   The Migration & Sync Engine connects to the Legacy Mainframe via APIM using mTLS and IP whitelisting.
*   Applications authenticate users via Azure Active Directory using OpenID Connect / OAuth 2.0.

## Technology Stack
*   **Azure Static Web Apps:** Hosts React frontends for rapid deployment and scalability.
*   **Azure Container Apps (ACA):** Standardizes microservices deployment, reducing cloud operational complexity for a low-experience team.
*   **Azure SQL Database:** Provides relational storage with Transparent Data Encryption (TDE) for modern claim types.
*   **Azure Service Bus:** Enables reliable asynchronous messaging and CQRS to bypass mainframe latency.
*   **Azure API Management (APIM):** Secures and throttles hybrid traffic, enforcing zero-trust boundaries.
*   **Azure App Configuration:** Powers runtime feature flags for rapid claim-type migration and rollback.

## Rationale
The hybrid Azure-on-premise architecture allows gradual, risk-managed migration of claim types while keeping the costly mainframe as the system of record. Utilizing managed Azure services like Container Apps and Service Bus minimizes cloud operational overhead for an inexperienced team while meeting strict performance (<2s UI load) and rollback requirements.