## Overview
The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe claims system with a modern cloud architecture. It enables online claim submissions, web-based adjuster handling, and incremental claim type migration while maintaining the legacy mainframe as the system of record.

## Key Elements
* Users: Customers, Brokers, and Claims Adjusters
* API Gateway: Azure Hosted API Gateway
* Core Modules: Claim Ingestion & Validation Module, Anti-Corruption Layer (ACL), and Feature Flag Management Module built on .NET Core / Modular Monolith
* Data & Cache: Read-Model Cache (Azure Cache / In-Memory Database), Data Synchronization Worker (.NET Background Worker), and Database Migration & Schema Versioning Module (Flyway / Entity Framework)
* Observability & Compliance: Centralized Observability & Audit Logging Module (Azure Monitor / Application Insights)
* External Systems: On-Premises COBOL/DB2 Mainframe, Azure Service Bus, Azure Key Vault, Azure App Configuration, and Azure Blob Storage

## Relationships
* Customers and Brokers submit claims via HTTPS to the Azure Hosted API Gateway.
* The API Gateway routes requests to the Claim Ingestion & Validation Module using gRPC/HTTPS.
* The Anti-Corruption Layer (ACL) communicates with the On-Premises COBOL/DB2 Mainframe via TCP/IP or secure MQ protocols.
* The Data Synchronization Worker syncs data between the modern platform and the on-premises mainframe database.
* All .NET Core modules stream telemetry and audit logs to Azure Monitor / Application Insights using W3C Trace Context and HTTPS.

## Technology Stack
* Cloud Platform: Hybrid deployment utilizing Azure West Europe and On-Premises Mainframe infrastructure, selected to meet regional residency and legacy integration constraints.
* Backend Compute: .NET Core / Modular Monolith, chosen for modularity and strong enterprise ecosystem support.
* Messaging & Integration: Azure Service Bus, providing reliable asynchronous messaging for claim state changes.
* Observability: Azure Monitor, Application Insights, and Log Analytics with JSON-based structured logging, ensuring compliance-ready audit trails despite limited team cloud experience.
* Security & Configuration: Azure Key Vault and Azure App Configuration with Active Directory SSO, fulfilling security and feature-flag migration needs.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind an Anti-Corruption Layer while enabling incremental cloud migration of claim types. It guarantees transactional consistency and fast adjuster response times without extending the strict nightly batch window or exceeding the team's cloud expertise.