## Overview
[Azure Key Vault securely manages credentials, encryption keys, and secrets for the hybrid insurance claims modernization platform using managed identities and RBAC. It enables secure communication between Azure containerized microservices and the legacy on-premise mainframe while meeting strict regulatory compliance.]

## Key Elements
- Azure Key Vault (Standard/Premium SKU)
- Azure Container Apps / App Service
- Managed Identities (Azure AD / Entra ID)
- Azure Virtual Network (Private Endpoints)
- Application Insights
- Infrastructure as Code (Terraform / Bicep)

## Relationships
- Azure Container Apps -> Azure Key Vault: Retrieves secrets and connection strings [Managed Identities via Private Endpoints]
- Azure Key Vault -> Application Insights: Emits diagnostic logs, metric alerts, and security telemetry [HTTPS]
- Azure Key Vault -> Azure Defender for Key Vault: Monitors access patterns and anomaly detection [Internal Azure API]

## Technology Stack
- Azure Key Vault: Centralized secret and key management with soft-delete and purge protection enabled
- Managed Identities: Passwordless authentication eliminating hardcoded credentials in container instances
- Azure Private Endpoints: Network isolation disabling public access to the Key Vault
- Azure RBAC & PIM: Least-privilege access enforcement (*Key Vault Secrets User*) with multi-person approval for break-glass scenarios
- Terraform / Bicep: Automated infrastructure as code deployment pipelines enforcing security guardrails

## Rationale
[This architecture secures hybrid integration points while accommodating the team's limited cloud experience through automated credential management and IaC guardrails. It ensures regulatory compliance and high availability for the 3-year migration phase without risking operational downtime.]