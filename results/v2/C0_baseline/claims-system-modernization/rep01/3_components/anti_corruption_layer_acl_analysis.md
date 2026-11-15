## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe. Its core purpose is to process and migrate claims safely while maintaining continuity with the legacy system.

## Key Elements
*   Policyholders and Brokers
*   Claims Adjusters
*   Migration Operations Team
*   Customer Portal (React SPA in Azure Static Web Apps)
*   Adjuster Web Application (Node.js / ASP.NET Core BFF)
*   Claims Processing Service (.NET Core microservices)
*   Anti-Corruption Layer (ACL) (Azure Container Apps)
*   Legacy Mainframe (COBOL/DB2 on-premise)
*   Microsoft Entra ID and Azure Key Vault

## Relationships
*   Customer Portal -> Claims Processing Service via HTTPS/REST
*   Adjuster Web Application -> Claims Processing Service via HTTPS/REST
*   Claims Processing Service -> Anti-Corruption Layer (ACL) via Azure Service Bus
*   Anti-Corruption Layer (ACL) -> Legacy Mainframe via gRPC over mTLS
*   Migration Operations Dashboard -> ACL Replay Coordinator via REST over HTTPS with Entra ID JWT validation

## Technology Stack
*   **Frontend:** React SPA for user portals and operations dashboards
*   **Backend:** .NET Core microservices and Node.js/ASP.NET Core for modern services
*   **Integration:** Azure Container Apps hosted Anti-Corruption Layer with JSON-to-COBOL mapping
*   **Security:** Microsoft Entra ID for SSO/RBAC and Azure Key Vault for mTLS secrets
*   **Infrastructure:** Hybrid deployment across on-premise mainframe and Azure West Europe

## Rationale
This hybrid architecture isolates expensive mainframe changes while using Azure cloud services for modern web applications. The Anti-Corruption Layer ensures zero data loss and enables rapid one-day rollbacks per claim type.