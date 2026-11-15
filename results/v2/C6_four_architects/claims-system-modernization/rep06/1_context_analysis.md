## Overview
The system is a hybrid cloud Modern Claims Platform that gradually replaces a legacy COBOL/DB2 mainframe claims system over a 3-year period. Its core purpose is to enable online claim submission and adjuster workflows while maintaining strict data consistency and synchronization with the mainframe.

## Key Elements
- Customers and Brokers (External Actors)
- Claims Adjusters (Internal Actors)
- Modern Claims Platform (System-of-Interest, Azure-hosted)
- Legacy Mainframe (External System of Record, COBOL/DB2, on-premise)
- Anti-Corruption Layer (ACL) (Container within Modern Claims Platform)
- Active Directory / Azure AD (External Identity Provider)
- Azure Service Bus and Azure Logic Apps (Integration Containers)
- Notification Service, Payment Gateway, Document Management System, Audit & Compliance System (External Systems)

## Relationships
- Customers/Brokers to Modern Claims Platform via HTTPS (REST/JSON)
- Adjusters to Modern Claims Platform via HTTPS (REST/JSON) for sub-2s response times
- Modern Claims Platform to Active Directory via HTTPS (OIDC/OAuth 2.0) for SSO
- Modern Claims Platform to Legacy Mainframe via Azure Service Bus and Azure Logic Apps (asynchronous messaging)
- Modern Claims Platform to Notification Service, Payment Gateway, Document Management System, and Audit & Compliance System via HTTPS (REST)

## Technology Stack
- Azure App Service / Azure SPA: Hosts the portal and adjuster workbench for low-overhead cloud deployment.
- Azure Service Bus / Azure Logic Apps: Manages asynchronous decoupling to protect the mainframe batch window (23:00-05:00).
- Anti-Corruption Layer (ACL): Isolates the modern domain model from legacy COBOL/DB2 schemas to absorb quarterly mainframe changes.
- Azure AD / Entra ID with Azure AD Connect: Implements secure SSO with minimal cloud experience.

## Rationale
This hybrid architecture isolates the fragile legacy mainframe behind an Anti-Corruption Layer and asynchronous message bus, satisfying strict change and batch constraints. It decouples modern user experiences from mainframe latency while preserving the 3-year migration path and enabling rapid rollbacks.