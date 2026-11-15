## Overview
A modern cloud-native platform gradually replaces a 30-year-old mainframe insurance claims system. It runs in a hybrid environment combining on-premise legacy systems with Azure West Europe.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Web Frontend (React, Azure App Service)
- BFF / API Gateway (Azure API Management, Node.js, Java Spring Boot)
- Claims Processing Service (Java Spring Boot, JPA, Azure Container Apps)
- Integration & ACL (Azure Service Bus, Custom Routing & Circuit-Breaker Worker)
- Azure Redis Cache (Azure Redis Cache)
- Azure SQL Database (Azure SQL Database)
- Insurer's Active Directory
- Legacy Mainframe System (COBOL/DB2)

## Relationships
- Customers & Brokers -> Web Frontend: Online claim submission [HTTPS / TLS 1.3]
- Claims Adjusters -> Web Frontend: Handles claims via web application [HTTPS / TLS 1.3]
- Web Frontend -> BFF / API Gateway: Routes API requests [HTTPS / REST]
- BFF / API Gateway -> Claims Processing Service: Orchestrates business logic [gRPC / HTTPS]
- Claims Processing Service -> Azure SQL Database: Persists migrated claims data [JDBC / TLS]
- Claims Processing Service -> Azure Redis Cache: Reads/writes cached claim states and reference data [Redis Protocol / TCP 6380, SSL]
- Integration & ACL -> Legacy Mainframe System: Synchronizes claims data [Batch / MQ]
- Web Frontend -> Insurer's Active Directory: Single Sign-On authentication [OpenID Connect / OAuth 2.0]

## Technology Stack
- Azure App Service: Hosts React frontend for rapid deployment with minimal cloud experience.
- Azure Container Apps: Runs Java Spring Boot microservices for scalable claim processing.
- Azure Service Bus: Asynchronously decouples migration messaging and event handling.
- Azure Redis Cache (Standard Tier C1): Provides sub-second caching for adjuster screens (NFR-05).
- Azure SQL Database: Stores relational claim data for migrated claim types.
- Microsoft Entra ID (Azure AD): Enforces single sign-on security (R-07).

## Rationale
The hybrid architecture isolates the fragile COBOL/DB2 mainframe while migrating claim types incrementally to Azure. This ensures business continuity, meets stringent latency and consistency requirements, and respects the team's limited cloud experience.