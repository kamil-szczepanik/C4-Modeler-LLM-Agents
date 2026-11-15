## Overview
The system is a hybrid cloud insurance claims platform that modernizes a 30-year-old COBOL/DB2 mainframe by migrating claim types gradually over three years. It ensures continuous processing and zero data loss while supporting online submissions and adjuster web applications.

## Key Elements
* End Customers and Brokers
* Claims Adjusters and Customer Support Agents
* Operations and Migration Managers
* Azure API Management (API Gateway)
* Customer Portal (React SPA / Azure Static Web Apps)
* Adjuster Workspace (Node.js/Spring Boot BFF + React)
* Migration Control & Routing Engine (Azure Functions & Azure Cosmos DB)
* Claims Processing Core (Azure Container Apps)
* Anti-Corruption Layer & Integration (Azure Service Bus & Apache Camel)
* Reconciliation Worker (Azure Container Apps Background Jobs)
* Audit & Reconciliation Ledger (Azure SQL Ledger)
* Legacy Mainframe System (COBOL / DB2 on-premise)
* Azure Active Directory / Identity Provider
* Azure Key Vault

## Relationships
* End Customers and Brokers interact with the Customer Portal via HTTPS (TLS 1.3).
* Customer Portal and Adjuster Workspace consume services through Azure API Management via OAuth 2.0 / OpenID Connect.
* Migration Control & Routing Engine dynamically directs payloads to Claims Processing Core or the Anti-Corruption Layer.
* Anti-Corruption Layer communicates with the Legacy Mainframe via Enterprise Service Bus / Message Queue using mTLS.
* Reconciliation Worker cross-checks state changes with the Legacy Mainframe during the nightly batch window (23:00-05:00).

## Technology Stack
* Microsoft Azure (West Europe region) and On-Premises hybrid topology for regional infrastructure.
* React for Customer Portal and Adjuster Workspace frontends.
* Node.js / Spring Boot for Backends For Frontends (BFF).
* Azure Container Apps for microservices and background workers.
* Azure Functions and Cosmos DB for the migration routing engine.
* Azure SQL Ledger for tamper-evident audit logs.
* Azure API Management and Azure AD for secure gateway and SSO integration.

## Rationale
The hybrid architecture allows the legacy mainframe to remain the system of record while decoupling new user experiences into Azure. This setup satisfies strict maintainability, consistency, and performance requirements without violating the costly mainframe integration constraints.