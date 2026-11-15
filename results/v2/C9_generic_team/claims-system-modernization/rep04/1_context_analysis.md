## Overview
The system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-hosted platform using a Strangler Fig migration pattern. It maintains continuous claim processing while migrating claim types one by one over a 3-year hybrid transition period.

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Azure Claims Modernization Platform (Target System)
- Active Directory (Identity Provider)
- Azure Service Bus (Messaging Backbone)
- Anti-Corruption Layer (ACL) and Switchboard

## Relationships
- Customers and Brokers submit claims online via HTTPS to the Azure platform.
- Claims Adjusters interact with claims via a web application integrated with Azure Active Directory (SSO).
- Azure Claims Platform communicates with the on-premises mainframe via the Anti-Corruption Layer using asynchronous messaging.
- Integration Gateway routes traffic dynamically between Azure services and the legacy mainframe.

## Technology Stack
- Microsoft Azure West Europe: Primary cloud region for the modern platform due to scalable infrastructure.
- Azure Service Bus: Asynchronous messaging backbone to decouple services and handle latency.
- Anti-Corruption Layer (ACL): Custom software component to isolate legacy DB2/COBOL schemas.
- OpenAPI: Contract-first API design standard for versioned and validated service integrations.
- Infrastructure as Code (IaC): Automated deployment toolchain to ensure environment parity.

## Rationale
The hybrid architecture accommodates limited cloud experience and strict legacy constraints by decoupling the modern Azure UI from slow mainframe responses. This setup guarantees data consistency and fast rollbacks without requiring frequent, expensive mainframe modifications.