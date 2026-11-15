## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid Azure architecture. It securely manages secrets, credentials, and cryptographic keys using Azure Key Vault to ensure data consistency and compliance during the 3-year migration.

## Key Elements
- Azure Key Vault (Premium Tier, FIPS 140-2 Level 2/3 HSM backed)
- Secrets Engine Component
- Access Control Component
- Audit & Diagnostics Component
- Adjuster Backend & Mainframe Integration Adapter (Azure Container Apps)
- Azure Private Link & Private Endpoints
- Azure Monitor / Azure Entra ID

## Relationships
- Adjuster Backend and Mainframe Integration Adapter interact with Azure Key Vault via Azure REST API over HTTPS (TLS 1.3) using Azure Managed Identities and Azure RBAC.
- On-premises legacy mainframe accesses Azure Key Vault exclusively via Azure Private Link (ExpressRoute/VPN).
- Azure Key Vault streams diagnostic logs and secret lifecycle events to Azure Monitor.
- Access Control Component integrates with Azure Entra ID for identity validation.

## Technology Stack
- Azure Key Vault (Premium Tier): Centralized secrets management with HSM backing for regulatory compliance and PII protection.
- Azure Private Link: Secures hybrid network traffic by denying public network access.
- Azure Managed Identities & Azure RBAC: Eliminates hardcoded connection strings and enforces least-privilege access.
- Bicep / Terraform: Infrastructure-as-Code deployment enforcing Soft Delete and Purge Protection.

## Rationale
This architecture secures hybrid data transit and centralizes credential management without increasing operational complexity for a cloud-inexperienced team. It guarantees zero-downtime secret rotation and strict data protection to maintain claim consistency during the phased mainframe migration.