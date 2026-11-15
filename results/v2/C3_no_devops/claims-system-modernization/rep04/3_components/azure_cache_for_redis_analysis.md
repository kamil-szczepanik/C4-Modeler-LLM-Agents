## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform. It enables online claims submission and adjuster processing while maintaining data consistency during a multi-year migration.

## Key Elements
- **Customers & Brokers**: External users submitting claims online
- **Claims Adjusters**: Internal users managing claims via the new web application
- **Legacy Mainframe**: On-premise COBOL/DB2 system of record
- **Customer Portal**: React SPA hosted in Azure Static Web Apps
- **Adjuster Web Application**: React SPA + ASP.NET Core Backend-for-Frontend (BFF)
- **Claims Processing Engine**: ASP.NET Core Microservices on Azure Kubernetes Service (AKS)
- **Anti-Corruption Layer (ACL)**: Azure Functions & Azure Service Bus
- **Azure Cache for Redis**: Standard Tier (C1/C2) with Claim State and Reference Data cache components
- **Azure API Management**: Strangler Fig Router
- **Security & Infrastructure**: Azure Active Directory, Azure Key Vault, Azure Private Link, and Azure Monitor Workbooks

## Relationships
- *Customers & Brokers* -> *Customer Portal*: Submits online claims [HTTPS]
- *Claims Adjusters* -> *Adjuster Web Application*: Manages claims [HTTPS]
- *Adjuster Web Application* -> *Azure Cache for Redis (Claim State Cache)*: Queries cached claims to meet sub-2s SLA [TCP/Redis Protocol over TLS 1.2/1.3]
- *Anti-Corruption Layer* -> *Azure Cache for Redis (Claim State Cache)*: Invalidates/updates cache via Pub/Sub on mainframe changes [TCP/Redis Protocol over TLS 1.2/1.3]
- *Claims Processing Engine* -> *Azure Cache for Redis (Reference Data Cache)*: Refreshes lookup data using cache-aside pattern [TCP/Redis Protocol over TLS 1.2/1.3]
- *Anti-Corruption Layer* -> *Legacy Mainframe*: Synchronizes claim data [MQ / Batch protocols]

## Technology Stack
- **Azure Cache for Redis**: Standard Tier for buffering slow mainframe responses and caching reference data
- **Microsoft Entra ID**: Used for secure authentication, RBAC, and least-privilege Redis access instead of static keys
- **Azure Private Link & Private Endpoints**: Isolates Redis from public internet exposure within internal VNets
- **Azure Monitor Workbooks**: Provides out-of-the-box operational dashboards for monitoring cache performance without complex cloud training
- **ASP.NET Core & Azure Functions**: Powers microservices and the anti-corruption layer

## Rationale
This architecture meets strict performance and consistency constraints by leveraging caching to hide mainframe latency while enforcing rigorous hybrid security boundaries. The design ensures seamless fallback capabilities within one day, accommodating the team's limited cloud experience.