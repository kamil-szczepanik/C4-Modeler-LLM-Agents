## Overview
This system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system while maintaining business continuity. It provides a secure, cloud-hosted web application and audit dashboard alongside the legacy system during a three-year hybrid migration phase.

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Compliance Officers / Auditors
- Claims Team Leads
- Legacy Mainframe System of Record (COBOL/DB2, On-Premises)
- Insurer Active Directory / Entra ID
- API Gateway (Azure Front Door / Azure API Management)
- Claims Web Application (React / Azure App Service)
- Audit & Reporting Dashboard (React / Azure App Service)
- Reporting API Component (.NET 8 Web API / Azure App Service)
- Dashboard UI Component (React / TypeScript)
- Audit Trail Logger Component (.NET 8 / Azure Functions)
- Alerting & Notification Component (.NET background worker / Azure Functions)
- Export Worker Component (.NET 8 Isolated Worker / Azure Function)
- Claims Core Service (Node.js/TypeScript on Azure Container Apps)
- Integration/Sync Service & Read-Model Sync Worker (Azure Service Bus, Azure Functions / .NET)
- Read-Model DB (Azure Cosmos DB)
- Azure Blob Storage (WORM-enabled)
- Enterprise Notification System

## Relationships
- Dashboard UI -> Reporting API: Queries audit logs and KPI metrics [HTTPS / REST, JWT Bearer]
- Reporting API -> Read-Model DB: Reads denormalized audit and reporting views [TCP / TLS]
- Reporting API -> Enterprise Notification System: Dispatches threshold alerts [HTTPS / REST]
- Export Worker -> Azure Blob Storage: Writes immutable reports and generates SAS download links [HTTPS, Azure SDK]
- Audit & Reporting Dashboard -> Identity Provider (Entra ID): Single Sign-On (SSO) [OpenID Connect / OAuth 2.0]

## Technology Stack
- Azure App Service: Hosts React frontend and .NET 8 Web API for managed scalability and zero-downtime blue/green deployments.
- Azure Functions (.NET 8): Powers asynchronous export and alerting workers with low infrastructure overhead.
- Azure Cosmos DB: Stores denormalized read-models for low-latency reporting queries.
- Azure Blob Storage: Provides WORM-compliant immutable storage for audit logs and report exports.
- Azure Service Bus: Manages asynchronous message queuing and export job distribution.
- React / TypeScript: Renders responsive adjuster and compliance user interfaces.
- Bicep / Terraform: Automates infrastructure provisioning to mitigate team cloud-inexperience risks.

## Rationale
The hybrid architecture isolates expensive mainframe modifications while leveraging managed Azure PaaS services to ensure fast screen loads and strict data consistency. This approach minimizes operational risk for an inexperienced cloud team while guaranteeing regulatory compliance, audit immutability, and seamless claim migration.