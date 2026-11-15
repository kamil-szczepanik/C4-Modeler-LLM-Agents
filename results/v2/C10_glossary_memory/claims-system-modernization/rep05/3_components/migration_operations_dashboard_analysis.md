## Overview
- This system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform using a hybrid cloud architecture.
- It provides a modern web interface for customers, brokers, and adjusters while maintaining business continuity through a gradual, claim-type-by-claim-type migration.

## Key Elements
- End Customers and Brokers
- Claims Adjusters
- Migration Operations Managers
- Modern Claims Platform
- Customer Web Portal (SPA/React)
- Adjuster Web Application (Modular Monolith/.NET)
- Migration Operations Dashboard (Web App/.NET)
- Claims Core API Service (Modular Monolith/.NET)
- Claim Router & Integration Worker (.NET Worker Service)
- Azure Service Bus (Azure Messaging Service)
- Legacy Mainframe System
- Corporate Active Directory / Entra ID

## Relationships
- End Customers and Brokers -> Customer Web Portal [HTTPS/REST]
- Claims Adjusters -> Adjuster Web Application [HTTPS/REST]
- Migration Operations Managers -> Migration Operations Dashboard [HTTPS/REST]
- Customer Web Portal -> Corporate Active Directory / Entra ID [OIDC/SAML]
- Adjuster Web Application -> Corporate Active Directory / Entra ID [OIDC/SAML]
- Migration Operations Dashboard -> Corporate Active Directory / Entra ID [OIDC/SAML]
- Migration Operations Dashboard -> Claims Core API Service [HTTPS/REST, TLS 1.3, JWT]
- Claims Core API Service -> Azure Service Bus [AMQP]
- Claim Router & Integration Worker -> Legacy Mainframe System [mTLS/VPN and signed JWT]

## Technology Stack
- Azure App Service: Hosts web applications in `azure-westeurope` to support the team's familiarity level.
- ASP.NET Core (.NET): Used for backend services and the Migration Operations Dashboard to maintain architectural consistency.
- Azure Service Bus: Manages messaging, backpressure, and dead-letter queues.
- Azure Active Directory / Entra ID: Provides Single Sign-On, MFA, and RBAC enforcement.
- Azure Monitor and Application Insights: Handles centralized logging, telemetry, and alerting.

## Rationale
- The hybrid architecture keeps the legacy mainframe as the system of record to minimize expensive legacy modifications.
- The modular services and dedicated migration dashboard ensure strict consistency, auditability, and the ability to roll back claim types within one day.