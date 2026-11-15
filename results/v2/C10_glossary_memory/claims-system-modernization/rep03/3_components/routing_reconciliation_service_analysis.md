## Overview
The system is a hybrid cloud insurance claims platform designed to gradually modernize a 30-year-old mainframe system over three years. It ensures zero data loss and rapid fallbacks while the legacy system processes ongoing claims.

## Key Elements
- Customers [person]
- Brokers [person]
- Claims Adjusters [person]
- Customer Portal SPA (Azure Static Web Apps, React/TypeScript) [container]
- API Gateway (Azure API Management) [container]
- Claims Processing Core & BFF (Azure Kubernetes Service) [container]
- Routing & Reconciliation Service (Azure Kubernetes Service + Azure Cosmos DB) [container]
- Legacy Mainframe (COBOL/DB2) [externalSystem]
- Identity Provider (Active Directory / Azure AD) [externalSystem]
- Notification Service (SendGrid/Twilio) [externalSystem]
- Claim Router Component (C#/.NET Core / gRPC) [component]
- Reconciliation Engine Component (C#/.NET Core Worker Service) [component]
- DLQ Manager Component (C#/.NET Core / Azure Service Bus SDK) [component]
- Reconciliation Dashboard API Component (C#/.NET Core / ASP.NET Web API) [component]
- Audit & State Store Component (Azure Cosmos DB, SQL API) [component]

## Relationships
- Customers -> Customer Portal SPA [HTTPS/WSS]
- Brokers -> Customer Portal SPA [HTTPS/WSS]
- Claims Adjusters -> Customer Portal SPA [HTTPS/WSS]
- Customer Portal SPA -> API Gateway [HTTPS REST/GraphQL]
- API Gateway -> Claims Processing Core & BFF [HTTPS / mTLS]
- Claims Processing Core & BFF -> Routing & Reconciliation Service [Internal gRPC/REST]
- Routing & Reconciliation Service -> Legacy Mainframe [Azure Service Bus over Azure ExpressRoute/VPN]
- Customer Portal SPA -> Identity Provider [OpenID Connect / OAuth 2.0]
- Claims Processing Core & BFF -> Notification Service [HTTPS REST API]
- Claim Router Component -> Audit & State Store Component [HTTPS / Cosmos DB SQL API]
- Reconciliation Engine Component -> Audit & State Store Component [HTTPS / Cosmos DB SQL API]
- DLQ Manager Component -> Audit & State Store Component [HTTPS / Cosmos DB SQL API]
- Reconciliation Dashboard API Component -> Audit & State Store Component [HTTPS / Cosmos DB SQL API]

## Technology Stack
- Azure Kubernetes Service (AKS): Hosts backend microservices and containerized components with minimal operational overhead for a cloud-inexperienced team.
- Azure Cosmos DB (SQL API): Persists immutable transaction logs and state data using native SQL APIs to reduce abstraction complexity.
- Azure Service Bus: Manages reliable messaging over Azure ExpressRoute/VPN during strict mainframe batch windows.
- C# / .NET Core: Powers the core components, worker services, and APIs for consistent enterprise development.
- React / TypeScript: Delivers a modern responsive UI within Azure Static Web Apps.

## Rationale
The hybrid architecture securely bridges legacy on-premise COBOL/DB2 mainframes with Azure cloud services using robust routing and reconciliation patterns. This ensures regulatory compliance, zero data loss, and rapid one-day rollbacks per claim type.