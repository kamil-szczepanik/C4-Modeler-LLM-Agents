## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform. It enables digital claim submissions and fast adjuster processing while ensuring continuous legacy synchronization.

## Key Elements
- **Users**: Policyholders and Brokers, Claims Adjusters
- **External Systems**: On-Premises Active Directory, Legacy Mainframe COBOL/DB2 System
- **Frontends**: React Single-Page Application (SPA) hosted in Azure Blob Storage/CDN, Customer BFF, Adjuster BFF
- **Backend & Integration Containers**: Node.js/TypeScript Modular Monolith, Azure API Management Gateway, Azure Service Bus, Integration Worker with Anti-Corruption Layer (ACL), Redis Cache
- **Data & Security**: Azure SQL Database (Transactional Outbox), Azure Monitor, Application Insights

## Relationships
- Policyholders/Brokers and Claims Adjusters interact with the React SPA via HTTPS.
- Azure API Management routes client requests to Customer and Adjuster BFFs using OAuth2/OIDC via Active Directory.
- Modular Monolith communicates asynchronously via Azure Service Bus and caches read-models in Redis.
- Integration Worker synchronizes data with the on-premises COBOL/DB2 mainframe using mTLS and file/batch payloads.

## Technology Stack
- **Frontend**: React, Azure Blob Storage, CDN for low-latency static asset delivery
- **Backend/API**: Node.js, TypeScript, Azure API Management (OAuth2/OIDC)
- **Messaging & Caching**: Azure Service Bus (event distribution), Redis Cache (read-model projection store)
- **Database**: Azure SQL Database with Transactional Outbox pattern for guaranteed consistency
- **Infrastructure & Security**: Azure Container Apps/AKS, Terraform (Infrastructure as Code), AES-256 and TLS 1.3 encryption

## Rationale
This hybrid architecture isolates the legacy mainframe from high-frequency web traffic while using an Anti-Corruption Layer and transactional outboxes to guarantee zero data loss. Caching and asynchronous processing meet strict performance SLAs without requiring expensive, frequent changes to the legacy system.