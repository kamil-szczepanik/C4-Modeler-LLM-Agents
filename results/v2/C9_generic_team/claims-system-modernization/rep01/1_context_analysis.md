## Overview
[System: Hybrid Insurance Claims Modernization Platform]
[Purpose: Gradually replaces a legacy mainframe claims system with a modern cloud platform while ensuring uninterrupted legacy processing.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Modern Cloud Platform (Azure West Europe)
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Centralized API Gateway / Integration Hub
- Azure Service Bus (Messaging)
- Azure Key Vault (Secrets Management)

## Relationships
- Customers & Brokers interact with Modern Cloud Platform via HTTPS for online claim submission
- Claims Adjusters interact with Modern Cloud Platform via HTTPS for claim handling
- Modern Cloud Platform integrates with On-Premises Mainframe via Centralized API Gateway using REST/JSON protocols
- Modern Cloud Platform securely retrieves secrets from Azure Key Vault via Managed Identity
- Asynchronous events flow through Azure Service Bus for claims ingestion and state synchronization

## Technology Stack
- Azure App Service: Hosts the modern web application for adjusters and customers, reducing operational overhead for a cloud-inexperienced team
- Azure Service Bus: Provides idempotent, reliable messaging to prevent duplicate claim processing
- Azure Key Vault: Centralizes secret and configuration management to mitigate security risks in a hybrid setup
- Infrastructure-as-Code (Bicep/Terraform): Ensures repeatable deployments and minimizes human configuration errors
- Anti-Corruption Layer (ACL) & CQRS: Decouples cloud data structures from legacy schemas and masks slow mainframe response times

## Rationale
- The hybrid architecture successfully maintains the legacy mainframe as the system of record while incrementally migrating claim types.
- Decoupling patterns and managed Azure services mitigate the team's low cloud experience and adhere to strict legacy interface change constraints.