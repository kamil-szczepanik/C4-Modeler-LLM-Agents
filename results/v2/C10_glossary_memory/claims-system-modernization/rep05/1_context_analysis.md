## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by introducing a cloud-based web application for customers and adjusters. It ensures business continuity through a 3-year hybrid architecture that incrementally migrates claim types while synchronizing data with the on-premises legacy system.]

## Key Elements
- End Customers and Brokers (Web users)
- Claims Adjusters (Internal web users)
- Modern Claims Platform (Azure West Europe, PaaS)
- Legacy Mainframe System (On-premises DB2/COBOL system of record)
- Corporate Active Directory / Entra ID (Identity Provider)
- Integration Middleware / API Gateway (Azure Service Bus / Azure Functions)

## Relationships
- End Customers and Brokers interact with Modern Claims Platform via HTTPS/REST for claim submission (R-01)
- Claims Adjusters interact with Modern Claims Platform via HTTPS/REST for claim handling (R-02)
- Modern Claims Platform authenticates users against Corporate Active Directory via OIDC/SAML (R-07)
- Modern Claims Platform synchronizes data with Legacy Mainframe via secure message queues and APIs over hybrid IPsec VPN/ExpressRoute with mTLS
- Modern Claims Platform accesses secrets securely via Azure Key Vault using Azure Managed Identities

## Technology Stack
- Microsoft Azure West Europe: Managed cloud platform chosen to offset the team's low cloud experience and reduce operational overhead
- Azure App Service & Azure Functions: Serverless and PaaS containers for hosting UI and integration logic to guarantee sub-2s adjuster response times (R-05)
- Azure Service Bus: Asynchronous messaging to respect the rigid 23:00-05:00 nightly batch window and ensure lossless consistency (R-04)
- Azure SQL Database: Managed database with AES-256 encryption for cached claims data and state management
- Azure Key Vault & Managed Identities: Centralized credential management preventing hardcoded secrets across the hybrid boundary

## Rationale
[This hybrid architecture decouples the modern user interface from legacy mainframe latency, satisfying performance and security requirements. It enables risk-free incremental migration and rapid 1-day rollbacks through isolated routing logic and managed asynchronous integration.]