## Overview
[The system modernizes a 30-year-old regional insurer mainframe by gradually migrating claims processing to a hybrid cloud platform. It ensures business continuity through a dual-system architecture where legacy and modern workflows coexist safely.]

## Key Elements
- Azure SQL Database (CQRS read-model storage for sub-2s adjuster views)
- Claims Read-Model Store (Relational tables with isolated schemas by claim type)
- Claims Core Engine (Java / Spring Boot / Azure Container Apps write model)
- Adjuster Workspace (Angular / Azure App Service UI)
- Azure Private Endpoints & Microsoft Entra ID (Security and network boundaries)

## Relationships
- Claims Core Engine -> Claims Read-Model Store: Writes projector updates [JDBC / TLS 1.3 over Private Endpoint]
- Adjuster Workspace -> Claims Read-Model Store: Executes low-latency read queries [ADO.NET / TLS 1.3 over Private Endpoint]
- Azure SQL Database -> Azure Key Vault: Manages encryption keys [HTTPS / REST over Private Endpoint]

## Technology Stack
- Azure SQL Database Serverless: Cost-effective scaling and high availability with geo-replication
- Flyway / Liquibase: Version-controlled, automated schema migrations for low-cloud-experience team
- Microsoft Entra ID: Single sign-on and exclusive database authentication eliminating credential sprawl
- Transparent Data Encryption (TDE): Data at rest protection using Customer-Managed Keys

## Rationale
- The hybrid cloud architecture allows gradual, risk-managed claim type migration without modifying the expensive legacy mainframe. Azure SQL Database with a CQRS pattern guarantees sub-2 second UI loads while meeting strict security and rollback requirements.