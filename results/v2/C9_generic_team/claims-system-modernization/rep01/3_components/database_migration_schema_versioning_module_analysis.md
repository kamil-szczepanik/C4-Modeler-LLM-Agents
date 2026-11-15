## Overview
The architecture implements a hybrid cloud modernization platform for regional insurance claims, gradually replacing a 30-year-old on-premises mainframe. It ensures seamless data consistency, rapid rollbacks, and zero-downtime schema evolution for migrating claim types.

## Key Elements
- **Users:** Customers, Brokers, and Claims Adjusters
- **Mainframe System:** On-Premises COBOL/DB2 Mainframe (System of Record)
- **Cloud Infrastructure:** Azure West Europe Region
- **Integration & Messaging:** Azure Service Bus, Azure Key Vault, Azure App Configuration
- **Core Application Modules:** API Gateway, Claim Ingestion & Validation Module (.NET Core), Anti-Corruption Layer (.NET Core), Read-Model Cache, Data Synchronization Worker (.NET Background Worker)
- **Operational & Data Modules:** Centralized Observability & Audit Logging Module (Azure Monitor / Application Insights), Database Migration & Schema Versioning Module (Flyway)

## Relationships
- **Customers & Brokers** submit claims via HTTPS to the Azure-hosted API Gateway
- **Claims Adjusters** access the Azure-hosted Web Application via HTTPS with Azure Active Directory SSO
- **Data Synchronization Worker** communicates with the On-Premises COBOL/DB2 Mainframe via secure VPN/ExpressRoute using TCP/IP protocols
- **Application Modules** securely retrieve secrets from Azure Key Vault via HTTPS and fetch dynamic configurations from Azure App Configuration
- **Database Migration Module** executes schema versioning via JDBC against the target relational database

## Technology Stack
- **Backend Services:** .NET Core / Modular Monolith for high-performance claim ingestion and domain logic
- **Database Migrations:** Flyway with pure SQL declarative scripts for transparent, reproducible schema evolution
- **Cloud Platform:** Microsoft Azure (Azure West Europe) providing regional hosting and managed services
- **Caching & Read Models:** Azure Cache / In-Memory Database to ensure adjuster screens load in under 2 seconds
- **Security & Identity:** Azure Active Directory for Single Sign-On (SSO) integration

## Rationale
The hybrid architecture keeps the stable COBOL/DB2 mainframe as the system of record while decoupling new claim types via Azure-hosted .NET services. Using Flyway with an Expand/Contract pattern guarantees strict consistency, fast one-day rollbacks, and zero downtime for the regional insurer.