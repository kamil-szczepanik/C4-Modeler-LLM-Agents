## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claim processing. It secures sensitive financial data and credentials using Azure Key Vault with zero-trust architecture.

## Key Elements
- Secrets Management Component
- Keys Management Component
- Access Control Component
- Caching & Event Listener Component
- Claims Processing Service
- Migration Dashboard
- Azure SQL Database
- Azure Key Vault Managed HSM

## Relationships
- Claims Processing Service -> Secrets Management Component: Retrieves connection strings via Azure SDK over HTTPS (REST) via Azure Private Endpoint
- Azure SQL Database -> Keys Management Component: Performs Transparent Data Encryption (TDE) operations via Azure internal secure channel
- Claims Processing Service & Migration Dashboard -> Access Control Component: Authenticates using Azure Active Directory (Entra ID) Managed Identities

## Technology Stack
- Azure Key Vault: Centralized secret and credential management to mitigate limited cloud experience
- Azure Active Directory (Entra ID): Zero-trust, credential-free authentication via Managed Identities
- Azure Key Vault Managed HSM: Customer-Managed Keys (CMK) for cryptographic sovereignty over sensitive data
- Azure Private Endpoints: Secures data-in-transit by blocking public internet access
- In-memory short-TTL cache (5-15 minutes): Balances performance (R-05) and security against transient outages

## Rationale
This architecture secures sensitive PII and financial data while protecting operational availability during a 3-year hybrid migration. Fully managed Azure primitives and private networking mitigate the team's limited cloud experience.