## Overview
The system gradually replaces a 30-year-old on-premise mainframe claims system with a modern hybrid cloud platform on Azure while maintaining uninterrupted legacy processing. It ensures zero claim loss, high availability for online submissions, and strict adherence to legacy technical constraints.

## Key Elements
* Customers & Brokers (External Actors)
* Claims Adjusters (Internal Actors)
* Insurance Claims Modernization Platform (Azure PaaS Containers)
* Legacy Mainframe System (On-Premises COBOL/DB2 System of Record)
* Azure Active Directory / Entra ID (Identity Provider)
* Azure API Gateway with Rate Limiter (Hybrid Boundary Protector)

## Relationships
* Customers/Brokers & Adjusters to Modern Platform: HTTPS (TLS 1.3), REST/GraphQL, OAuth 2.0 / OIDC
* Modern Platform to Azure Entra ID: OIDC / Graph API for Single Sign-On and MFA
* Modern Platform to Legacy Mainframe: Azure ExpressRoute/VPN, mTLS, synchronous REST or asynchronous queues respecting quarterly change limits

## Technology Stack
* Cloud Provider: Azure (West Europe region) to host the modern container platform
* Compute & Storage: Azure App Service, Azure SQL, and Managed Redis (PaaS) chosen to simplify operations for a team with limited cloud experience
* Security & Integration: Azure API Gateway with OpenAPI validation, Checkov/TfSec for IaC scanning, and Azure Sentinel for audit logging
* Observability: Azure Application Insights and distributed tracing with correlation IDs to monitor performance

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind an Azure API Gateway and asynchronous queues, protecting the legacy system from daytime traffic spikes and batch window limits. Fully managed PaaS services and robust feature flags satisfy the requirement for low cloud experience while guaranteeing a one-day fallback to the mainframe.