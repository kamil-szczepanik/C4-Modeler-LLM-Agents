## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe while maintaining continuous core operations. It enables online claim submissions and adjuster workflows in Azure while securing legacy data synchronization.

## Key Elements
*   **Customers / Brokers**: External users submitting claims online.
*   **Claims Adjusters**: Internal users handling claims via a web application.
*   **New Claims Platform**: Azure West Europe-hosted microservices/containerized application.
*   **Legacy Mainframe**: On-premise COBOL/DB2 system of record.
*   **Enterprise Integration Bus**: Decoupling and buffering layer for hybrid data exchange.
*   **Corporate Active Directory & Azure Entra ID**: Identity providers for single sign-on.
*   **Notification Service**: External provider (SendGrid/Twilio/SMTP) for customer alerts.
*   **Azure Key Vault**: Centralized secret and certificate management.

## Relationships
*   **Customers, Brokers, Adjusters -> New Claims Platform**: HTTPS via TLS 1.3 / OAuth 2.0 / OpenID Connect.
*   **New Claims Platform <-> Enterprise Integration Bus**: Secure asynchronous messaging / APIs.
*   **Enterprise Integration Bus <-> Legacy Mainframe**: Encrypted queues with mTLS and rate-limiting.
*   **New Claims Platform -> Notification Service**: HTTPS for automated alerts.
*   **Users -> Azure Entra ID / Corporate AD**: SSO authentication via Azure AD Connect.

## Technology Stack
*   **Azure West Europe / Azure Container Apps**: Provides managed cloud infrastructure to mitigate the team's limited cloud experience.
*   **Azure Entra ID & OAuth 2.0 / OpenID Connect**: Delivers single sign-on and role-based access control (R-07).
*   **Enterprise Integration Bus**: Decouples services to respect the quarterly mainframe change constraint and prevent batch window overloads.
*   **Azure Key Vault**: Secures hybrid credentials, API keys, and certificates.
*   **TLS 1.3 and mTLS**: Protects data in transit across the hybrid trust boundary.

## Rationale
This hybrid architecture isolates the fragile mainframe behind an integration bus, protecting it from frequent changes and batch window limits while enabling rapid cloud delivery. Managed Azure services reduce operational risk for a team with limited cloud experience, ensuring zero data loss and compliance.