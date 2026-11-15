## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old on-premise mainframe with a secure hybrid cloud platform in Azure West Europe. It ensures non-repudiation, strict regulatory compliance, and immutable audit trails across legacy and modern workflows.]

## Key Elements
- Finance & Compliance Auditors [person]
- Audit & Compliance Service [container, Azure Function]
- Audit Event Consumer [.NET Isolated Azure Function Trigger]
- Compliance Rules Engine [C# Domain Component]
- Audit Query API [ASP.NET Core Functions HTTP Trigger]
- Compliance Report Generator [.NET Timer Trigger Azure Function]
- Audit Data Store [Azure SQL Database Ledger with Read Replica]
- Azure Service Bus [externalSystem]
- Insurer Active Directory [externalSystem]
- Azure Monitor / Application Insights [externalSystem]

## Relationships
- Finance & Compliance Auditors -> Audit Query API (HTTPS / JSON, Role-Based Access Control)
- Audit Event Consumer -> Azure Service Bus (AMQP)
- Audit Event Consumer -> Audit Data Store (TDS / TCP via Entity Framework Core)
- Compliance Rules Engine -> Audit Data Store (TDS / TCP via Entity Framework Core)
- Compliance Report Generator -> Audit Data Store Ledger Read Replica (TDS / TCP)
- Audit Query API -> Audit Data Store Ledger Read Replica (TDS / TCP)
- Audit & Compliance Service -> Insurer Active Directory (OIDC / OAuth2 via Azure Entra ID, Azure Managed Identity)
- Audit & Compliance Service -> Azure Monitor / Application Insights (HTTPS)

## Technology Stack
- Azure Functions (.NET Isolated): Serverless execution model aligning with team's managed-service preference.
- Azure SQL Database Ledger: Tamper-evident, cryptographically secure append-only audit tables using familiar relational tooling to reduce operational overhead.
- Azure Entra ID & Managed Identities: Secure single sign-on and secret-free authentication.
- Entity Framework Core: Standardized relational data access with read-replica connection routing.

## Rationale
[This architecture fits requirements by establishing tamper-evident, automated compliance tracking using managed Azure components that simplify auditing for regional regulators. Using SQL Ledger and read replicas prevents performance degradation while securing hybrid data consistency under strict migration constraints.]