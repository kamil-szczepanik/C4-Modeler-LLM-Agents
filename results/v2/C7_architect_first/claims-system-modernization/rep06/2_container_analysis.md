## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid platform. It processes online claims and adjuster workflows while maintaining transactional consistency and supporting claim-by-claim migration.

## Key Elements
- **Web Portal (SPA)**: React/TypeScript application hosted in Azure Static Web Apps for customers and brokers.
- **Adjuster Workspace**: Web application handling adjuster claims processing.
- **API Gateway / Router**: YARP reverse proxy managing feature flags, routing, rate-limiting, and circuit breakers.
- **Claims Core Service**: Spring Boot application running on Azure Container Apps (ACA) using domain-driven modular monolith packages.
- **Integration & Sync Engine**: Apache Kafka / Azure Service Bus connected via Anti-Corruption Layer (ACL).
- **Database Container**: Azure SQL Database isolated from the legacy mainframe.
- **Audit & Activity Trail Service**: Dedicated service tracking user actions across workflows.

## Relationships
- **Web Portal** and **Adjuster Workspace** interact with the **API Gateway / Router** via TLS 1.3 using OAuth 2.0 / OpenID Connect (OIDC) through Azure Active Directory (Entra ID).
- **API Gateway / Router** routes traffic to the **Claims Core Service** or **Legacy Mainframe** based on feature flags.
- **Claims Core Service** connects to **Azure SQL Database** using Azure Managed Identity with Transparent Data Encryption (TDE).
- **Integration & Sync Engine** communicates with the on-premise **Legacy Mainframe** over mTLS and IPsec VPN/ExpressRoute encryption.

## Technology Stack
- **Azure Container Apps (ACA)**: Abstracts Kubernetes complexity to lower operational burden for a cloud-novice team.
- **Spring Boot (Java)**: Provides enterprise libraries for transactional consistency.
- **Azure SQL Database**: Ensures data isolation and modern persistence for migrated claims.
- **Azure Static Web Apps**: Hosts the React/TypeScript customer and broker portal.
- **Apache Kafka / Azure Service Bus**: Ensures message durability and zero data loss in hybrid event streams.
- **Azure Key Vault**: Secures customer-managed keys for database encryption.

## Rationale
This hybrid architecture uses Azure Container Apps and managed services to minimize operational risk for a cloud-inexperienced team. It employs an API Gateway with feature flags and an Anti-Corruption Layer to guarantee zero data loss, strict security boundaries, and rapid one-day claim-type rollbacks.