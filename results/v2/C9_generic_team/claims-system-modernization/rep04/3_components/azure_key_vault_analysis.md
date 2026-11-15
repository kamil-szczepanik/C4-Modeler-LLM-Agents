## Overview
[The system is an Insurance Claims Modernization platform that gradually replaces a legacy mainframe with a hybrid cloud architecture using Azure Container Apps. Its core purpose is to modernize claim submissions and adjuster workflows while maintaining seamless data consistency with the legacy system.]

## Key Elements
* Azure Key Vault: Centralized secrets management service
* Backend-for-Frontend (BFF): Azure Container App handling client routing
* Modular Monolith: Azure Container App containing core business logic
* Anti-Corruption Layer (ACL): Azure Container App integrating with the mainframe
* Managed Identities: Azure IAM mechanism for secure authentication

## Relationships
* Backend-for-Frontend (BFF) -> Azure Key Vault: Retrieves secrets securely [HTTPS via Managed Identity]
* Modular Monolith -> Azure Key Vault: Retrieves secrets securely [HTTPS via Managed Identity]
* Anti-Corruption Layer (ACL) -> Azure Key Vault: Retrieves secrets securely [HTTPS via Managed Identity]

## Technology Stack
* Azure Key Vault: Centralized, secure storage for database strings and API credentials
* Azure Managed Identities: Eliminates hardcoded credentials and client secret rotation overhead
* Terraform / Bicep: Infrastructure-as-Code for reproducible vault provisioning and pipeline deployment
* Internal Configuration Wrapper: Standardized library handling in-memory secret caching, fail-fast validation, and local development fallbacks
* Azure Monitor: Diagnostic logging and auditing for access tracking and compliance

## Rationale
[This architecture secures sensitive insurance claims data and meets compliance standards while mitigating the team's limited cloud experience through automated IaC and standardized wrappers. Caching and Managed Identities ensure high performance, preventing latency on adjuster screens and supporting strict migration constraints.]