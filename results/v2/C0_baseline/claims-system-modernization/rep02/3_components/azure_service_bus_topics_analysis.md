## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old on-premise mainframe with a hybrid cloud platform while ensuring uninterrupted legacy claim processing.]

## Key Elements
*   **Users**: Customers / Brokers, Claims Adjusters
*   **External Systems**: Legacy Mainframe, Active Directory / Microsoft Entra ID, Payment Gateway
*   **Containers**: Azure API Management, Customer Portal (React), Adjuster Workspace (Angular), Claims Core Engine (Java / Spring Boot), Routing & Integration Service (Azure Functions), Business Analytics & Reporting (Azure SQL / Power BI), Azure SQL Database, Azure Service Bus Topics
*   **Components (Azure Service Bus Topics)**: Topic Router, Subscription Filters, Dead-Letter Manager

## Relationships
*   **Claims Core Engine** -> **Azure Service Bus Topics**: Publishes claim events with Session IDs (`[AMQP over TLS]`)
*   **Azure Service Bus Topics** -> **Routing & Integration Service**: Dispatches events using peek-lock mode (`[AMQP over TLS]`)
*   **Dead-Letter Manager** -> **Claims Core Engine**: Alerts on message failures (`[AMQP over TLS]`)

## Technology Stack
*   **Azure Service Bus Topics**: Asynchronous messaging with session IDs for data consistency and duplicate detection
*   **Terraform**: Infrastructure-as-Code for automated deployments and configuration drift elimination
*   **Microsoft Entra ID**: Managed Identities for secure, passwordless authentication and RBAC
*   **Azure Monitor & Log Analytics**: Observability and diagnostic logging for active sessions and dead-letter queues

## Rationale
[This hybrid architecture isolates expensive mainframe interactions while using modern cloud components to achieve sub-2-second UI responses and guaranteed zero-loss claim migration. It safely accommodates a team with low cloud experience via automated Terraform deployments and managed identity security controls.]