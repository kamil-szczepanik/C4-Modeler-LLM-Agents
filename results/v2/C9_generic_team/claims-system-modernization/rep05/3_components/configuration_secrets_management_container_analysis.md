## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It ensures seamless claim processing, zero data loss, and rapid rollback capabilities during migration.

## Key Elements
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- COBOL/DB2 Mainframe (Legacy System of Record)
- Azure API Management / Container Apps (API Gateway)
- Azure App Service / Container Apps (Customer BFF, Adjuster BFF, Modular Monolith)
- Azure Container Apps (Anti-Corruption Layer, Routing, Data Sync, IAM Proxy)
- Azure Service Bus and Redis (Asynchronous Messaging and Caching)
- Azure Key Vault (Configuration & Secrets Management)

## Relationships
- Customers/Brokers interact with Customer BFF via HTTPS/REST
- Adjusters interact with Adjuster BFF via HTTPS/REST
- BFFs communicate with Modular Monolith via internal gRPC/HTTP
- Modular Monolith connects to COBOL/DB2 Mainframe via Anti-Corruption Layer using TCP/MQ/Batch protocols
- Containers retrieve secrets from Azure Key Vault via HTTPS using Managed Identities
- System synchronizes data with Azure Service Bus using AMQP

## Technology Stack
- Azure Container Apps & Azure App Service: Runtime hosting chosen for containerized microservices
- Azure Key Vault: Centralized secret management with strict naming conventions and immutable post-boot values
- Azure Managed Identities: Enforces least-privilege access for containers without shared credentials
- Azure Service Bus & Redis: Asynchronous messaging and caching for performance and consistency
- Active Directory: Single Sign-On integration for secure identity management

## Rationale
The hybrid architecture isolates expensive mainframe dependencies behind an Anti-Corruption Layer while modernizing the user experience in Azure. This setup satisfies strict performance and consistency constraints, enabling one-day rollbacks and supporting a team with limited cloud experience.