## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It ensures zero data loss, sub-2-second adjuster screen loads, and seamless incremental migration of claim types.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Azure Static Web Apps (React Claims Web Application)
- Azure Container Apps (.NET Core API Gateway / BFF, Migration Router / Anti-Corruption Layer, Mainframe Integration Adapter)
- Azure Service Bus
- Azure SQL Managed Instance
- Azure Cache for Redis (Redis Cache Engine, Distributed Output Cache Provider, Claim State Cache Manager)
- Legacy Mainframe (COBOL/DB2)
- Active Directory

## Relationships
- Customers & Brokers -> Claims Web Application: HTTPS / TLS 1.3
- Claims Adjusters -> Claims Web Application: HTTPS / TLS 1.3 with Active Directory SSO (OAuth 2.0 / OIDC)
- Claims Web Application -> API Gateway / BFF: HTTPS / REST API
- API Gateway / BFF -> Azure Cache for Redis: RESP over TCP/TLS for sub-2s screen loads
- API Gateway / BFF -> Migration Router / Anti-Corruption Layer: gRPC / Internal TLS
- Migration Router / Anti-Corruption Layer -> Azure SQL Managed Instance: TDS / TCP/TLS
- Migration Router / Anti-Corruption Layer -> Azure Service Bus: AMQP / TLS
- Migration Router / Anti-Corruption Layer -> Azure Cache for Redis: RESP over TCP/TLS for cache invalidation
- Mainframe Integration Adapter -> Legacy Mainframe: SNA / MQ / TCP

## Technology Stack
- Frontend: React on Azure Static Web Apps for modern, responsive user interfaces.
- Backend Services: .NET Core on Azure Container Apps for containerized microservices reducing operational complexity.
- Database: Azure SQL Managed Instance for transactional data storage and consistency.
- Messaging & Caching: Azure Service Bus for asynchronous messaging and Azure Cache for Redis for performance optimization.
- Identity: Active Directory via OAuth 2.0/OIDC for secure single sign-on.

## Rationale
This hybrid architecture isolates the legacy COBOL/DB2 mainframe while introducing modern Azure cloud containers to incrementally migrate claims. It meets strict performance and consistency constraints through strategic caching, managed cloud services, and an anti-corruption layer.