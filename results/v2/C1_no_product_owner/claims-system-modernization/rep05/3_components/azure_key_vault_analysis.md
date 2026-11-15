## Overview
[The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe claims system with a modern Azure cloud solution while maintaining continuous hybrid operations.]

## Key Elements
- Azure Key Vault (Standard/Premium HSM-backed SKU)
- Secrets Management Component (Azure Key Vault Secrets, HTTPS/REST)
- Certificates Management Component (Azure Key Vault Certificates)
- Access Control & Policy Enforcement Component (Azure RBAC & Private Link)
- API Gateway & BFF (Azure Container Apps / Node.js or .NET)
- Integration & Anti-Corruption Layer (Azure Functions & Service Bus)
- New Claims Database (Azure SQL Database)
- Azure Application Insights / Log Analytics

## Relationships
- API Gateway & BFF -> Secrets Management Component: Retrieves runtime secrets and database connection strings via Private Endpoint [HTTPS/REST, TLS 1.3, Managed Identities]
- Integration & Anti-Corruption Layer -> Secrets Management Component: Retrieves mainframe integration credentials via Private Endpoint [HTTPS/REST, TLS 1.3, Managed Identities]
- API Gateway & BFF -> Certificates Management Component: Handles TLS/SSL certificates via Private Endpoint [HTTPS/REST, TLS 1.3]
- Azure Key Vault -> Azure Application Insights: Routes diagnostic settings and access logs [HTTPS]

## Technology Stack
- Azure Key Vault: Centralized secret management to avoid hardcoded credentials for a cloud-inexperienced team
- Azure RBAC: Granular least-privilege access control instead of legacy access policies
- Private Endpoints / Azure Virtual Network: Eliminates public internet exposure for secret retrieval
- TLS 1.3: Enforces secure cryptographic transport and prevents downgrade attacks
- Premium HSM-backed SKU: Protects high-value cryptographic assets in FIPS 140-2 Level 2 validated hardware security modules
- Microsoft Defender for Key Vault: Advanced threat detection for anomalous access patterns

## Rationale
[This architecture secures hybrid operations by isolating sensitive cloud credentials behind private endpoints and enforcing strict access controls. It mitigates cloud inexperience risks through managed identities, automated secret rotation, and robust monitoring.]