## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a legacy 30-year-old mainframe claims system with a modern cloud-native solution. It ensures seamless hybrid operations, zero claim loss, and strict consistency during the 3-year migration window.

## Key Elements
- Customers & Brokers, Claims Adjusters, Finance Operations & Compliance Auditors
- Legacy Mainframe System, Azure Active Directory / Entra ID, Azure API Gateway
- Customer Portal & Adjuster Web Apps (Azure Static Web Apps)
- Claim Management API, Claim Router / ACL, Audit & Reconciliation Service (Azure Container Apps, .NET 8)
- Reconciliation Engine, Audit Logger, Discrepancy API, Discrepancy Manager Components (.NET 8)
- Azure SQL Database (with SQL Ledger), Azure Service Bus, Azure Key Vault, Azure App Configuration

## Relationships
- Customer Portal & Adjuster Web Apps -> Claim Management API via HTTPS / REST
- Claim Management API -> Azure Service Bus via AMQP
- Claim Router / ACL -> Legacy Mainframe System via custom legacy protocols (mTLS)
- Reconciliation Engine -> Azure SQL Database and Legacy Mainframe extracts via HTTPS
- Discrepancy API -> Finance Operations Dashboard via HTTPS (OAuth2 / OIDC)
- Audit & Reconciliation Service -> Azure SQL Database via Entity Framework Core (Managed Identities)

## Technology Stack
- Azure Container Apps (.NET 8): Container hosting for scalability and low cloud complexity.
- Azure SQL Database (SQL Ledger): Tamper-resistant storage for immutable audit logs and consistency tracking.
- Hangfire / .NET Hosted Services: Scheduled background execution for reconciliation jobs.
- MediatR: CQRS pattern implementation for discrepancy resolution workflows.
- Azure Active Directory / Entra ID: Single Sign-On and Role-Based Access Control (`Claims.Finance.Auditor`).

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while using cloud-native .NET services to guarantee zero data loss and enable rapid one-day rollback capabilities. Containerized microservices on Azure provide the required scalability and security controls while accommodating the team's cloud experience level.