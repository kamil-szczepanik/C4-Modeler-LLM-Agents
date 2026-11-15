## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a hybrid cloud platform on Azure West Europe. It ensures seamless claim processing, zero data loss, and rapid rollback capabilities while the legacy system remains the system of record.

## Key Elements
- Customers & Brokers, Claims Adjusters, Customer Support Agents
- Azure API Management (Strangler Fig Router)
- Customer Portal (React SPA in Azure Static Web Apps)
- Adjuster Web Application (React SPA + ASP.NET Core BFF)
- Claims Processing Engine (ASP.NET Core Microservices on Azure Kubernetes Service)
- Anti-Corruption Layer (Azure Functions & Azure Service Bus)
- Azure Cache for Redis
- Legacy Mainframe (COBOL/DB2, On-Premises)
- Azure Active Directory & Key Vault

## Relationships
- Users access portals via HTTPS/REST through Azure API Management.
- Azure API Management routes traffic to the React SPAs, BFF, and Legacy Mainframe via site-to-site VPN/ExpressRoute using mTLS and TLS 1.3.
- Adjuster BFF queries Azure Cache for Redis to serve claims within the <2s SLA.
- Claims Processing Engine and Anti-Corruption Layer use Azure Service Bus topics for event-driven messaging.
- Anti-Corruption Layer synchronizes data with the Legacy Mainframe via restricted batch/interface protocols.

## Technology Stack
- Azure API Management: Manages routing and Strangler Fig pattern for incremental claim migration.
- Azure Kubernetes Service (AKS): Hosts scalable Claims Processing Engine microservices.
- Azure Functions & Azure Service Bus: Powers the Anti-Corruption Layer to insulate against legacy schema changes.
- Azure Cache for Redis: Buffers slow mainframe responses to meet performance SLAs.
- Azure Active Directory & OAuth 2.0 / OpenID Connect: Centralizes single sign-on and RBAC.

## Rationale
The hybrid architecture uses an Anti-Corruption Layer and Strangler Fig router to isolate the new cloud platform from expensive mainframe dependencies. This design guarantees zero lost claims, supports one-day rollbacks, and fits the team's cloud skill set.