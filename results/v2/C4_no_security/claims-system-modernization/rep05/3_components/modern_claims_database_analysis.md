## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform. It enables online claim submissions and adjuster workflows while maintaining legacy operations for three years.

## Key Elements
- Claims Web Application (React, Azure Static Web Apps)
- API Gateway (Azure API Management)
- Claims Core Service (.NET 8 / C#, Azure Kubernetes Service)
- Modern Claims Database (Azure SQL Database with Azure SQL Temporal Tables)
- Integration & Sync Engine (Azure Service Bus)
- External Systems: Legacy Mainframe, Corporate Active Directory, Observability Platform

## Relationships
- Claims Web Application -> API Gateway: HTTPS/REST
- API Gateway -> Claims Core Service: gRPC/HTTPS
- Claims Core Service -> Modern Claims Database: Entity Framework Core / TLS
- Integration & Sync Engine -> Modern Claims Database: Read-only Parity Queries / SQL/TLS
- Claims Core Service -> Corporate Active Directory: SAML/OIDC (Single Sign-On)

## Technology Stack
- Azure SQL Database: Chosen for strict ACID guarantees, relational foreign keys, and matching the legacy DB2 schema to satisfy consistency requirements (R-04).
- Azure SQL Temporal Tables: Automatically captures tamper-evident row history for compliance and audit requirements without custom trigger maintenance.
- Entity Framework Core 8: Provides secure ORM-based data persistence and connection pooling.
- Bicep / Terraform: Standardizes infrastructure deployments to mitigate the team's limited cloud experience.
- Azure Monitor: Tracks resource consumption and deadlocks to protect the sub-2-second adjuster SLA (R-05).

## Rationale
This hybrid architecture leverages Azure SQL Database to guarantee transactional consistency and rapid rollbacks during a complex, multi-year legacy migration. Automated CI/CD pipelines and infrastructure-as-code compensate for limited cloud expertise while strictly adhering to performance and security constraints.