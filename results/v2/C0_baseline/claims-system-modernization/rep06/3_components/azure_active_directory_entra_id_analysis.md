## Overview
[Hybrid Insurance Claims Modernization Platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native platform using Azure services. It enables online claim submission for customers/brokers and web-based claims handling for adjusters while maintaining system consistency.]

## Key Elements
- Azure Active Directory (Entra ID)
- Token Service (STS)
- Directory & Graph API Component
- B2C / External Identity Federation Gateway
- Audit & Reporting Component
- Azure API Management
- Claims Processing Service (Java, Spring Boot, Azure Container Apps)
- Migration Dashboard (React, Node.js, Azure Container Apps)
- Azure Service Bus
- Azure Logic Apps / Functions
- Azure SQL Database
- Azure Key Vault
- Azure Application Insights

## Relationships
- Claims Processing Service validates JWT tokens from Token Service via HTTPS (OIDC metadata/JWKS)
- Azure API Management enforces token validation at the edge using OAuth 2.0 introspection and JWT validation policies
- Azure Application Insights / Log Analytics ingests telemetry from Audit & Reporting Component via HTTPS (Azure Diagnostic Settings)
- Claims Processing Service and Azure API Management consume public JWKS endpoints from Token Service via HTTPS (GET)

## Technology Stack
- Azure Active Directory (Entra ID) for identity management and SSO (R-07 requirement)
- OAuth 2.0 / OpenID Connect (OIDC) protocols for token issuance and validation
- Terraform / Bicep for Infrastructure-as-Code to prevent environment drift
- Azure Application Insights for sign-in and audit telemetry monitoring
- Azure Container Apps hosted on Azure West Europe for modern containerized services

## Rationale
[The hybrid architecture utilizes Azure services to safely modernize claims processing while keeping the legacy mainframe as the system of record for 3-year migration safety. This decouples the cloud web applications from expensive mainframe changes while meeting strict consistency and security requirements.]