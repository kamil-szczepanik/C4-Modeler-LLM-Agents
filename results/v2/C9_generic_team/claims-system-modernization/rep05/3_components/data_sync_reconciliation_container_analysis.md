## Overview
[A hybrid insurance claims modernization platform that gradually replaces a 30-year-old mainframe system while maintaining continuous operational integrity.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- COBOL/DB2 Mainframe (On-Premises)
- Azure API Management / Container Apps (API Gateway)
- Azure App Service / Container Apps (Customer BFF, Adjuster BFF, Modular Monolith)
- Azure Container Apps (Anti-Corruption Layer, Routing / Feature Flag, Data Sync / Reconciliation, IAM Proxy)
- Azure Service Bus and Redis (Asynchronous Messaging & Caching)
- Azure Key Vault (Configuration & Secrets)
- Azure Application Insights (Observability)

## Relationships
- Customers and Brokers interact with Customer BFF via HTTPS/REST.
- Claims Adjusters interact with Adjuster BFF via HTTPS/REST.
- API Gateway routes external traffic to BFFs using HTTPS.
- BFFs communicate with Modular Monolith and ACL via internal gRPC/HTTPS.
- Data Sync & Reconciliation Container synchronizes data with COBOL/DB2 Mainframe via secure enterprise messaging and DB2 drivers.
- IAM Proxy integrates with Active Directory using OpenID Connect / OAuth2.

## Technology Stack
- Azure Container Apps & App Service: Hosts microservices and containers with managed scaling.
- Azure Service Bus & Redis: Handles asynchronous event-driven messaging and caching to decouple systems.
- Azure Key Vault: Secures centralized secrets and configuration management.
- Azure Application Insights: Provides distributed tracing and telemetry.
- COBOL / DB2 Mainframe: Retained as the legacy system of record.

## Rationale
- Decouples legacy dependencies using an Anti-Corruption Layer and asynchronous messaging to protect the strict batch window.
- Employs a hybrid Azure architecture and managed services to reduce the operational burden on a team with limited cloud experience.