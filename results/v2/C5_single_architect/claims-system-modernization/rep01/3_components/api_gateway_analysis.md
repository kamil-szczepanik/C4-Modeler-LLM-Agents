## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It maintains dual processing capabilities to ensure seamless migration of individual claim types without disrupting ongoing operations.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- On-premises Active Directory
- Legacy Mainframe (COBOL/DB2)
- Customer Portal (React SPA on Azure Static Web Apps)
- Adjuster Workspace (Node.js BFF on Azure App Service)
- API Gateway (Azure Front Door / Azure Application Gateway)
- Claims Core Engine (Java Spring Boot on Azure Container Apps)
- Integration Layer (Azure Event Hubs with Apache Camel)
- Migrated Claims Database (Azure Database for PostgreSQL)

## Relationships
- Customer Portal -> API Gateway: Routing requests [HTTPS using OpenID Connect]
- Adjuster Workspace -> API Gateway: Routing requests [HTTPS using OpenID Connect]
- API Gateway -> Authentication & Authorization Component: Validates incoming tokens [HTTPS / OIDC]
- Routing & SSL Termination -> Token Exchange & Transformation: Passes validated requests [Internal HTTP/2]
- Token Exchange & Transformation -> Claims Core Engine: Forwards sanitized API calls [HTTPS / gRPC]
- API Gateway -> Integration Layer: Routes legacy event hooks [HTTPS / AMQP]

## Technology Stack
- Azure Front Door & Application Gateway: Secures ingress and routes traffic across hybrid boundaries.
- Azure Active Directory: Implements centralized Single Sign-On (SSO) to satisfy R-07.
- Azure Container Apps & Java Spring Boot: Hosts the scalable Claims Core Engine.
- Azure Database for PostgreSQL: Acts as the modern system of record for migrated claim types.
- Azure Event Hubs with Apache Camel: Orchestrates reliable event-driven data synchronization.

## Rationale
This hybrid architecture isolates the fragile, expensive-to-change mainframe while safely migrating claim types one by one to Azure. It guarantees strict consistency, secure Active Directory authentication, and sub-second adjuster UI response times despite legacy latency.