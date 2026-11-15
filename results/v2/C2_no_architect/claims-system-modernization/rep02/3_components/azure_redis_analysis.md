## Overview
This hybrid architecture gradually replaces a 30-year-old mainframe insurance claims system with a modern cloud platform in Azure West Europe while maintaining the on-premises COBOL/DB2 system of record. It ensures zero data loss, strict security compliance, and sub-2-second UI response times for claims adjusters during the multi-year migration.

## Key Elements
* Policyholders and Brokers (Users)
* Claims Adjusters (Users)
* Compliance and Audit Officers (Users)
* COBOL/DB2 Mainframe (External System)
* Azure Active Directory / Entra ID (External System)
* API Gateway (Azure API Gateway)
* Claims Web App (Azure AKS, ASP.NET Core / React)
* Integration Service (Azure AKS, .NET)
* Claim Reconciliation Service (Azure AKS, .NET)
* Azure Redis (Azure Cache for Redis)
* Azure Service Bus (Azure Service Bus)

## Relationships
* Policyholders and Brokers -> API Gateway: Online claim submission [HTTPS]
* Claims Adjusters -> Claims Web App: Handle claims in web application [HTTPS]
* Claims Web App -> Azure API Gateway: API requests [HTTPS/JSON]
* Claims Web App -> Azure Redis: UI acceleration, session management, and reference data caching [TLS 1.2 / TCP]
* Integration Service -> COBOL/DB2 Mainframe: Hybrid data exchange [SNA/MQ/JDBC]
* Claim Reconciliation Service -> COBOL/DB2 Mainframe: Consistency checks [SNA/MQ/JDBC]
* Claims Web App -> Azure Service Bus: Asynchronous messaging [AMQP]

## Technology Stack
* Hybrid Cloud (Azure West Europe & On-Premises Mainframe): Balances cloud agility with legacy system constraints.
* Azure Kubernetes Service (AKS): Container orchestration for modern microservices (.NET / React).
* Azure Cache for Redis (Standard/Premium): In-memory caching for UI acceleration, session management, and reference data.
* Azure Service Bus: Reliable asynchronous messaging to guarantee consistency without data loss.
* Microsoft Entra ID & Azure Key Vault: Single sign-on and secure secrets management.

## Rationale
The hybrid approach allows incremental migration of claim types without disrupting the core mainframe system of record. Azure Redis and AKS microservices ensure high-performance UI rendering and secure session handling, meeting strict performance and security requirements.