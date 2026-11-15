## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform. The system ensures continuous claim processing while migrating claim types over a three-year period.

## Key Elements
- Customer, Broker, Claims Adjuster
- On-premise COBOL/DB2 Legacy Mainframe
- Azure API Management
- Claims Processing Service (Java, Spring Boot, Azure Container Apps)
- Migration Dashboard (React, Node.js, Azure Container Apps)
- Azure SQL Database (Serverless tier avoided; Provisioned Tier, Gen5 hardware, `azure-westeurope`)
- Internal Database Schemas: Claim Operational Store, Migration State & Routing Registry, Audit & Reconciliation Log
- Azure Service Bus
- Azure Logic Apps / Functions
- Azure Key Vault
- Azure Active Directory (Entra ID)
- Azure Application Insights

## Relationships
- Claims Processing Service -> Azure SQL Database: CRUD operations and high-frequency lookups using Tabular Data Stream (TDS) over TLS 1.3 via Azure Private Link
- Azure SQL Database -> Azure Key Vault: Retrieval of Customer-Managed Keys for Transparent Data Encryption (TDE) via HTTPS (REST) over VNet service endpoint
- Azure SQL Database -> Azure Application Insights: Streaming audit logs and performance metrics using native diagnostic settings
- Users -> Azure API Management: API requests via HTTPS (REST) / OpenID Connect

## Technology Stack
- Azure SQL Database: ACID-compliant persistence, data consistency, and sub-2-second adjuster screen loads
- Provisioned Tier Compute (Gen5 hardware): Prevents cold-start latencies associated with serverless architectures
- Microsoft Entra ID: Single Sign-On and Role-Based Access Control (RBAC), disabling local SQL authentication
- Transparent Data Encryption (TDE) with Customer-Managed Keys: Data protection at rest via Azure Key Vault
- Flyway / Liquibase: Automated schema migration management for hybrid coexistence

## Rationale
The hybrid architecture maintains the legacy mainframe as the system of record while incrementally offloading claim types to an Azure-hosted platform, strictly satisfying the three-year coexistence constraint. Using a provisioned Azure SQL Database with private endpoints guarantees low-latency performance, robust security, and rapid one-day rollback capabilities.