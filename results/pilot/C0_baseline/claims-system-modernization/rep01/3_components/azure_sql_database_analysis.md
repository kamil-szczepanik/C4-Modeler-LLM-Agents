## Overview
[The system is a hybrid cloud Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe with a modern web architecture. Its core purpose is to enable digital claim submissions and adjuster workflows while maintaining seamless data consistency during a multi-year migration.]

## Key Elements
* Azure SQL Database (Primary transactional data store)
* Relational Data Store (Azure SQL Engine with `Core`, `Outbox`, `Audit` schemas)
* Transactional Outbox Table (Domain event management)
* Modular Monolith (Node.js, TypeScript container)
* Azure Key Vault (Customer-Managed Keys storage)

## Relationships
* Modular Monolith -> Azure SQL Database: Persists relational data and domain events [Entity Framework Core, T-SQL over encrypted TDS, Managed Identities]
* Azure SQL Database -> Azure Key Vault: Secures data encryption [Transparent Data Encryption with Customer-Managed Keys]
* Azure SQL Database -> Azure Monitor: Streams audit logs and telemetry [TLS-secured log streaming]

## Technology Stack
* Azure SQL Database: Managed relational storage chosen for built-in high availability and transactional consistency (R-04)
* Entity Framework Core: ORM selected for rapid developer productivity and robust LINQ-to-SQL mapping
* Bicep / Terraform: Infrastructure-as-Code tools used for automated, repeatable cloud deployments
* Microsoft Entra ID: Authentication mechanism ensuring zero reliance on SQL credentials and strict RBAC
* Transparent Data Encryption (TDE): Storage-layer encryption mandated for compliance and PII protection

## Rationale
[This architecture fits the requirements by using managed Azure services to compensate for the team's limited cloud experience while guaranteeing zero data loss (R-04). Furthermore, isolated database schemas and strict fallback patterns ensure that migrated claim types can be rolled back to the mainframe within one day (R-06).]