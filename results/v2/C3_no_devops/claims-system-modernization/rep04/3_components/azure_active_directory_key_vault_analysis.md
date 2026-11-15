## Overview
The system provides a hybrid insurance claims modernization platform, gradually replacing a legacy mainframe with modern cloud services while maintaining legacy operations. It ensures secure authentication, secrets management, and zero-loss claim processing during migration.

## Key Elements
- Token Service (Azure Entra ID)
- Secrets Provider (Azure Key Vault)
- Customer Portal (React SPA in Azure Static Web Apps)
- Adjuster Web Application (React SPA + ASP.NET Core BFF)
- Claims Processing Engine (ASP.NET Core Microservices on Azure Kubernetes Service)
- Anti-Corruption Layer (Azure Functions & Azure Service Bus)
- Legacy Mainframe (COBOL/DB2)

## Relationships
- Customer Portal & Adjuster Web Application -> Token Service: Authenticates users and validates JWT tokens [HTTPS / OpenID Connect]
- Claims Processing Engine & Anti-Corruption Layer -> Secrets Provider: Retrieves secrets securely at runtime [HTTPS / Azure REST API via Azure Managed Identity]
- Anti-Corruption Layer <-> Legacy Mainframe: Synchronizes claims data [Batch / Asynchronous messaging]

## Technology Stack
- Azure Entra ID: Centralizes single sign-on and identity federation with on-premise Active Directory for R-07.
- Azure Key Vault: Secures runtime secrets and cryptographic keys using Private Endpoints to mitigate cloud-inexperience risks.
- Azure Managed Identities: Eliminates hardcoded credentials for microservices accessing Key Vault.
- ASP.NET Core / AKS: Powers modern claims processing microservices.

## Rationale
This architecture securely isolates identity and secrets management to support a cloud-inexperienced team while maintaining strict compliance. It enables gradual claim migration without extending the rigid nightly batch window.