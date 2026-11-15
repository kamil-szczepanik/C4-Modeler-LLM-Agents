## Overview
The Insurance Claims Modernization platform gradually replaces a legacy mainframe system while ensuring zero data loss and maintaining high availability. It uses a hybrid architecture spanning an on-premises mainframe and Azure West Europe.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2)
- Active Directory
- Claims Web Application (React, Azure Static Web Apps)
- API Gateway / BFF (Azure Container Apps, .NET Core)
- Migration Router / Anti-Corruption Layer (Azure Container Apps, .NET Core)
- Mainframe Integration Adapter (Azure Container Apps, .NET Core)
- Azure Service Bus (Messaging Container)
- Azure Cache for Redis (Caching Container)
- Database (Azure SQL Managed Instance: Claim Entity Store, Migration Sync Tracker, Audit Log Store, Outbox Store)

## Relationships
- Customers & Brokers -> Claims Web Application: Submits claims via [HTTPS]
- Claims Adjusters -> Claims Web Application: Manages claims via [HTTPS]
- Claims Web Application -> API Gateway / BFF: Routes API calls via [HTTPS/REST]
- API Gateway / BFF -> Migration Router / Anti-Corruption Layer: Directs claim operations via [gRPC/Internal]
- Migration Router / Anti-Corruption Layer -> Mainframe Integration Adapter: Syncs legacy claims via [AMQP/REST]
- Mainframe Integration Adapter -> Legacy Mainframe: Interfaces with COBOL/DB2 via [SNA/TN3270/Batch]
- Migration Router / Anti-Corruption Layer -> Database: Interacts for persistence via [TDS]
- Database (Outbox Publisher) -> Azure Service Bus: Dispatches events via [AMQP]
- Active Directory -> Claims Web Application: Authenticates users via [OAuth2/OIDC/SAML]

## Technology Stack
- Azure SQL Managed Instance: Provides strong ACID guarantees and transactional consistency (R-04) via [TDS].
- Azure Container Apps (.NET Core): Hosts microservices and anti-corruption layers with managed scaling.
- Azure Static Web Apps (React): Delivers high-performance adjuster screens under 2s latency (R-05).
- Azure Service Bus: Handles reliable asynchronous messaging via [AMQP].
- Azure Cache for Redis: Caches data to mitigate mainframe response delays.

## Rationale
This hybrid architecture isolates expensive mainframe changes while modernizing adjuster workflows through Azure cloud services. It guarantees transactional consistency and rapid fallback capabilities required during the phased migration.