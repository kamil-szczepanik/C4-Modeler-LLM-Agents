## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern hybrid cloud platform. It enables online claims processing while maintaining business continuity with the on-premise system of record.

## Key Elements
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- Legacy Mainframe (On-premise System of Record)
- Active Directory (Identity Provider)
- Claims Web Application (Azure Static Web Apps / React)
- API Gateway & BFF (Azure Container Apps / Node.js or .NET)
- Integration & Anti-Corruption Layer (Azure Functions & Service Bus)
- New Claims Database (Azure SQL Database)
- Azure Application Insights (Observability)
- Azure Key Vault (Secret Management)

## Relationships
- Customers/Brokers & Adjusters interact with Claims Web Application via HTTPS/JSON
- Claims Web Application communicates with API Gateway & BFF via HTTPS/JSON
- API Gateway & BFF authenticates users via Azure Active Directory using OpenID Connect/OAuth2
- API Gateway & BFF communicates with Integration & ACL and New Claims Database via mTLS and HTTPS/JSON
- Integration & ACL connects to Legacy Mainframe via secure VPN/ExpressRoute with on-premise API Security Gateway
- Containers and services forward telemetry to Azure Application Insights via OpenTelemetry headers

## Technology Stack
- Azure Container Apps: Hosts containerized services, providing KEDA scaling while abstracting Kubernetes complexity for a team with limited cloud experience
- Azure Static Web Apps: Hosts the React-based frontend for fast UI delivery
- Azure Functions & Service Bus: Powers the Anti-Corruption Layer with dead-letter queues and circuit-breakers to guarantee zero data loss (R-04)
- Azure SQL Database: Stores migrated claim types with Transparent Data Encryption
- Azure Key Vault: Manages runtime secrets using managed identities
- Azure Application Insights: Provides centralized distributed tracing across the hybrid boundary

## Rationale
This hybrid architecture decouples modern cloud-native user interfaces from legacy mainframe latencies, ensuring sub-2-second screen loads. It safely isolates claim migrations through an Anti-Corruption Layer, enabling rapid 1-day rollbacks and strict data consistency without extending the batch window.