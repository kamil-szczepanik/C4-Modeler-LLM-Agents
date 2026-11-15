## Overview
[Modernizes a regional insurer's claims platform by gradually migrating functionality from a 30-year-old mainframe to an Azure-based cloud architecture. Ensures zero data loss and sub-second performance while maintaining legacy system integration.]

## Key Elements
- Customers and Brokers (External Actors)
- Claims Adjusters (Internal Actors)
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Active Directory (Identity Provider)
- Backend-for-Frontend (BFF) (Azure Container Apps)
- Modular Monolith (Azure Container Apps)
- Anti-Corruption Layer (ACL) (Azure Container Apps)
- Azure Service Bus, Azure Cosmos DB / Redis, Azure Key Vault

## Relationships
- Customers and Brokers -> Backend-for-Frontend (BFF): Submit claims online [HTTPS/REST]
- Claims Adjusters -> Backend-for-Frontend (BFF): Claim handling and processing [HTTPS/REST]
- Backend-for-Frontend (BFF) -> Modular Monolith: Application logic communication [Internal HTTPS/REST]
- Backend-for-Frontend (BFF) -> Azure Key Vault: Secure secret retrieval [HTTPS]

## Technology Stack
- Azure Container Apps: Simplifies cloud management for a team with limited cloud experience
- Azure Redis Cache: Manages session state and aggressive caching to meet sub-2s response requirements
- OpenAPI/Swagger: Standardizes API contracts and schema validation at the BFF boundary
- W3C Trace Context headers: Enables distributed tracing across the hybrid Azure and on-prem boundary

## Rationale
[This hybrid architecture balances the stability and long-term retention of the legacy mainframe with the agility of modern cloud services. It safely isolates complex migration logic behind containerized components, protecting data consistency and user performance.]