## Overview
[The system modernizes a regional insurer's 30-year-old claims platform by gradually migrating claim types to a hybrid cloud architecture while the COBOL/DB2 mainframe remains the system of record.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- New Claims Platform (Azure West Europe PaaS)
- Legacy Mainframe (On-premise COBOL/DB2)
- Anti-Corruption Layer / Enterprise Messaging Queue
- Active Directory / Identity Provider
- Reconciliation Service & Audit System

## Relationships
- End Customers & Brokers -> New Claims Platform (HTTPS via Web/Mobile UI)
- Claims Adjusters -> New Claims Platform (HTTPS)
- New Claims Platform <-> Legacy Mainframe (Asynchronous messaging via ESB/MQ acting as Anti-Corruption Layer)
- Active Directory <-> New Claims Platform (OpenID Connect / SAML over HTTPS for SSO)

## Technology Stack
- Azure App Service & SQL Database: Managed PaaS to reduce cloud management overhead for an inexperienced team
- Enterprise Messaging Queue with Dead-Letter Queues (DLQs): Asynchronous buffering to respect the 23:00-05:00 batch window and protect mainframe connection pools
- OpenID Connect / SAML: Protocol for single sign-on integration with Active Directory
- Infrastructure as Code (IaC): Automates Azure resource provisioning and deployment repeatability

## Rationale
[This hybrid architecture decouples the modern cloud frontend from the fragile legacy mainframe via an asynchronous Anti-Corruption Layer, ensuring zero data loss and strict maintainability during the 3-year migration. It isolates expensive mainframe changes while empowering adjusters with a sub-second web experience.]