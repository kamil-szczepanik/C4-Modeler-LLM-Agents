## Overview
[A hybrid claims modernization platform that gradually migrates functionality from a legacy COBOL/DB2 mainframe to Azure while maintaining uninterrupted business operations. The system secures sensitive insurance data and hybrid microservice communications using robust cloud security patterns.]

## Key Elements
* Azure Key Vault & Managed Identities (Container)
* Claims API Gateway & Claims Processing Service (.NET Core on Azure Container Apps)
* User-Assigned Managed Identities (Identity Management)
* Azure Private Endpoints (Network Security)
* Log Analytics Workspace (Auditing & Monitoring)
* Key Rotation & Automated Alerting Engine (Lifecycle Management)

## Relationships
* Claims API Gateway & Claims Processing Service to Azure Key Vault via HTTPS (TLS 1.3 via Azure SDK) over Azure Private Endpoints
* Claims API Gateway & Claims Processing Service authenticate against Azure Key Vault via User-Assigned Managed Identities token exchange
* Azure Key Vault streams audit logs and metrics to Log Analytics Workspace via Azure Monitor Diagnostic Settings

## Technology Stack
* Azure Key Vault: Secures cryptographic keys, database connection strings, and certificates without hardcoding.
* User-Assigned Managed Identities: Decouples service identity lifecycles from container lifecycles for secure, passwordless authentication.
* Azure Private Endpoints: Eliminates public internet exposure by routing secure traffic entirely within the Azure Virtual Network.
* Azure RBAC: Enforces least-privilege access permissions specifically tailored per container microservice.
* Azure Event Grid & Azure Functions: Automates zero-touch key rotation and expiration alerting.

## Rationale
[This architecture secures hybrid connectivity and compensates for the team's low cloud experience through managed, automated cloud primitives. It ensures strict regulatory compliance and eliminates static credentials across the 3-year phased mainframe migration.]