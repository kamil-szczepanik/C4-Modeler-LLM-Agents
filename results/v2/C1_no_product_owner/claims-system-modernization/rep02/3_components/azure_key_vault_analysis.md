## Overview
This architecture summary outlines the Azure Key Vault component within a hybrid cloud platform designed to modernize a regional insurer's legacy mainframe claims system. It centralizes secrets, certificates, and keys securely while supporting phased claim type migration.

## Key Elements
- **Secrets Management Component**: Stores connection strings and API keys for the Adjuster Backend Service and Azure SQL Database.
- **Certificates Management Component**: Manages non-exportable mTLS certificates for the Mainframe Integration Adapter.
- **Access Policy / RBAC Engine**: Enforces least-privilege access using Azure Managed Identities and Azure RBAC roles.
- **Network Ingress Layer**: Secures traffic via Azure Private Endpoint with public internet access disabled.
- **Audit & Monitoring Module**: Streams diagnostic logs to a SIEM and monitors throttling metrics.

## Relationships
- Adjuster Backend Service -> Secrets Management Component: Fetches DB credentials and API keys via HTTPS over Private Link using Azure Managed Identity.
- Mainframe Integration Adapter -> Certificates Management Component: Retrieves mTLS client certificates via HTTPS over Private Link using Azure Managed Identity.
- Azure Key Vault -> SIEM: Streams `AuditEvent` logs in real-time via Azure Diagnostics.

## Technology Stack
- **Azure Key Vault**: Central secrets and certificate management to safeguard hybrid connection data.
- **Azure Private Endpoint**: Restricts network ingress exclusively to internal Azure IPs.
- **Azure RBAC & Managed Identities**: Eliminates hardcoded credentials and enforces least-privilege authorization.
- **Spring Cloud Azure Secret Refresh**: Implements local secret caching with a short TTL to prevent throttling and maintain sub-second UI performance.
- **Terraform/Bicep**: Used for Infrastructure-as-Code deployment to prevent configuration drift.

## Rationale
This architecture secures sensitive hybrid integration data against unauthorized access while protecting system performance through local caching. It successfully accommodates the team's limited cloud experience via automated IaC governance and managed identities.