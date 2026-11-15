## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe with a modern Azure cloud platform. Its core purpose is to enable incremental claim type migration and secure claims management while maintaining continuous legacy operations.]

## Key Elements
- Migration Project Managers and Operations Leads
- Migration Dashboard (React, Node.js, Azure Container Apps)
- Rollback Controller Component
- Reconciliation Viewer Component & Data Aggregator
- RBAC & Authorization Middleware
- Audit Logging Service
- Azure SQL Database
- Azure Active Directory (Entra ID)
- Azure Key Vault
- Azure Logic Apps

## Relationships
- Migration Project Managers -> Migration Dashboard: Accesses via Azure API Management [HTTPS / OIDC / OAuth 2.0]
- Rollback Controller -> Claims Processing Service: Triggers feature flag switches [HTTP/REST]
- Reconciliation Viewer & Data Aggregator -> Azure SQL Database: Queries reconciliation metrics and audit logs [TDS / TLS 1.3]
- Migration Dashboard -> Azure Key Vault: Retrieves secrets [Managed Identity / HTTPS]
- Azure Logic Apps -> On-premise Mainframe: Polls legacy status [HTTPS]

## Technology Stack
- React: Frontend UI framework for the Migration Dashboard due to team familiarity and component reusability
- Node.js: Backend runtime for handling API requests, RBAC middleware, and reconciliation aggregation
- Azure Container Apps: Serverless container hosting platform minimizing infrastructure management for a cloud-novice team
- Azure SQL Database: Relational datastore for audit logs and reconciliation metrics, accessed via TDS
- Bicep & GitHub Actions: IaC and GitOps pipeline for repeatable, auditable deployments given low cloud experience

## Rationale
[This hybrid architecture bridges the legacy COBOL/DB2 mainframe and modern cloud services using Azure Container Apps and API Management. It ensures safety-critical governance through RBAC, immutable audit logging, and rapid rollback controls to satisfy strict compliance and low-risk migration constraints.]