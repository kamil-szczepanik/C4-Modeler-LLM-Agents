## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern cloud-native solution. It enables 24/7 digital claim submissions and high-performance adjuster workflows while maintaining the legacy system as the system of record for three years.

## Key Elements
* End Customers & Brokers (Users)
* Claims Adjusters (Users)
* Customer Portal (React/TypeScript SPA hosted on Azure Static Web Apps)
* Adjuster Web Application (React/TypeScript SPA)
* Claims API Gateway / Backend-for-Frontend (Node.js or .NET Core on Azure Container Apps)
* Integration & Sync Service (Azure Container Apps worker)
* Audit & Event Store (Azure Cosmos DB)
* Operational Datastore (Azure SQL Database / PostgreSQL on Azure)
* Legacy Mainframe System (On-premises COBOL/DB2)
* Corporate Active Directory (External IDP)

## Relationships
* End Customers & Brokers interact with Customer Portal via HTTPS (REST)
* Claims Adjusters interact with Adjuster Web Application via HTTPS (REST)
* Customer Portal and Adjuster Web Application communicate with Claims API Gateway via HTTPS/JSON
* Claims API Gateway communicates with Integration & Sync Service via HTTPS/JSON and Azure Service Bus
* Integration & Sync Service synchronizes data with Legacy Mainframe System via IPsec VPN or Azure ExpressRoute (mTLS / TLS 1.3)
* Identity Provider Proxy authenticates users against Corporate Active Directory using OpenID Connect (OIDC) / OAuth2

## Technology Stack
* Frontend: React with TypeScript, hosted on Azure Static Web Apps for rapid, global content delivery
* Compute & Orchestration: Azure Container Apps with blue-green deployments via Terraform to meet one-day rollback constraints (R-06)
* Messaging & Integration: Azure Service Bus with durable queues and dead-lettering to safely handle the 23:00–05:00 mainframe blackout window
* Data Stores: Azure Cosmos DB (append-only immutability for audit trails) and Azure SQL Database (operational sync-state)
* Security & Auth: Azure Active Directory (OIDC/OAuth2), Azure Key Vault (Managed Identities for secret elimination), and TLS 1.3 / mTLS for transport security

## Rationale
This hybrid architecture isolates the user experience from legacy backend latency via a BFF and caching layer, guaranteeing sub-2s UI responses. Granular claim-type routing and asynchronous Azure Service Bus synchronization ensure zero data loss (R-04) while strictly adhering to quarterly mainframe interface limits and enabling one-day rollbacks (R-06).