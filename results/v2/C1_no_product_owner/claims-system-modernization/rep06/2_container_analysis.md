## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure cloud platform while maintaining hybrid operations. It ensures zero data loss, sub-2 second adjuster response times, and a 1-day claim-type rollback capability.

## Key Elements
* **Web Portal (SPA):** React/TypeScript hosted in Azure Static Web Apps for online claims submission.
* **Adjuster Workspace (Web App):** Node.js/React BFF hosted in Azure App Service.
* **Claims Core API (Application):** Spring Boot microservices running on Azure Kubernetes Service (AKS).
* **Integration & Sync Engine:** Fully managed Azure Event Hubs (Kafka interface) with transactional outbox.
* **Identity & Access Proxy:** Azure API Management with OAuth2/OIDC, federating with on-premise Active Directory.
* **Claims Read Model & Cache:** Azure Cosmos DB (SQL API) in West Europe with managed identities.
* **Security & Infrastructure:** Azure Key Vault with CSI secret store drivers, Azure Monitor, and Azure ExpressRoute.

## Relationships
* Web Portal & Adjuster Workspace $\rightarrow$ Identity Proxy via HTTPS/OIDC
* Adjuster Workspace $\rightarrow$ Claims Core API via gRPC/HTTPS
* Adjuster Workspace $\rightarrow$ Claims Read Model via HTTPS/SQL API
* Claims Core API $\rightarrow$ Integration Engine via Kafka native protocol over mTLS
* Integration Engine $\rightarrow$ On-Premise Mainframe via Azure ExpressRoute

## Technology Stack
* **Frontend:** React/TypeScript (Azure Static Web Apps) for responsive user interfaces.
* **Backend:** Node.js/React (Azure App Service) for decoupled BFF logic; Spring Boot Java (AKS) for core domain logic.
* **Messaging & Integration:** Azure Event Hubs (Kafka protocol) for asynchronous, reliable event streaming.
* **Storage & Caching:** Azure Cosmos DB (SQL API) for low-latency materialized views and sub-2s reads.
* **Security & Auth:** Azure Key Vault, Managed Identities, and Azure API Management for centralized credentials and Zero-Trust access.

## Rationale
This hybrid architecture isolates the expensive, slow legacy mainframe while using modern Azure cloud services to meet strict performance and maintainability goals. Managed cloud components minimize operational friction for a team with low cloud experience.