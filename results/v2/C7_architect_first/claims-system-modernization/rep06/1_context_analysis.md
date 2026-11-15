## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe with a modern cloud platform in Azure West Europe. It maintains hybrid coexistence and data consistency for three years while migrating claim types incrementally.

## Key Elements
- Customers and Brokers: External users submitting claims online.
- Claims Adjusters: Internal users managing claims in the new web application.
- New Claims Platform: Cloud container system hosted on Azure Kubernetes Service (AKS).
- Anti-Corruption Layer (ACL): Buffering proxy service in Azure.
- Legacy Mainframe: On-premises COBOL/DB2 system of record.
- Identity Provider: Active Directory / Azure AD.

## Relationships
- Customers & Brokers to New Claims Platform via HTTPS / OpenID Connect.
- Claims Adjusters to New Claims Platform via HTTPS.
- New Claims Platform to Identity Provider via OpenID Connect / OAuth 2.0.
- New Claims Platform to Legacy Mainframe via mTLS over VPN/ExpressRoute through the Anti-Corruption Layer (ACL).

## Technology Stack
- Azure Kubernetes Service (AKS): Container orchestration for cloud microservices.
- C# / ASP.NET Core: Primary programming framework for cloud services.
- Azure SQL / Cosmos DB: Cloud database persistence with AES-256 encryption.
- Terraform & ArgoCD: Infrastructure as Code and GitOps deployment pipelines.
- Azure Key Vault: Secret management utilizing managed identities.
- OpenTelemetry: Distributed tracing and observability across hybrid boundaries.

## Rationale
The hybrid architecture protects expensive mainframe interfaces via the Anti-Corruption Layer while delivering a modern cloud experience. This approach ensures business continuity, meets strict latency and security mandates, and enables incremental claim migration.