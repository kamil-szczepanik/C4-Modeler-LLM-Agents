## Overview
The system gradually replaces a 30-year-old mainframe claims platform with a modern hybrid cloud solution while maintaining business continuity. It provides online claim submission and adjuster workspaces while supporting the step-by-step migration of claim types.

## Key Elements
- Policyholders and Brokers (Users)
- Claims Adjusters (Users)
- Customer Portal (React SPA / Azure Container Apps)
- Adjuster Workspace (Node.js/Java / Azure Container Apps)
- Anti-Corruption Layer (ACA Integration Service)
- Migration Analytics Container (Node.js/Python / Azure Container Apps)
- Azure Service Bus (Event Broker)
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Azure Active Directory (Identity Provider via OIDC/OAuth2)

## Relationships
- Policyholders interact with Customer Portal via HTTPS/TLS 1.3
- Adjusters interact with Adjuster Workspace via HTTPS
- Customer Portal and Adjuster Workspace publish/subscribe to Azure Service Bus via AMQP
- Anti-Corruption Layer integrates Azure Service Bus with On-Premises Mainframe via mutual TLS (mTLS) over Azure ExpressRoute
- All services authenticate against Azure Active Directory via OIDC/OAuth2 and Azure Managed Identities

## Technology Stack
- Azure Container Apps (ACA): Chosen to host microservices given the team's limited cloud experience by abstracting Kubernetes complexity
- React SPA & Azure Static Web Apps: Delivers a responsive, modern frontend for customer claim submissions
- Azure Service Bus: Ensures asynchronous, guaranteed event delivery and prevents claim loss (R-04)
- Azure ExpressRoute & mTLS: Secures hybrid connectivity between Azure and the on-premise mainframe
- Node.js/Java & Python: Power the backend microservices and migration analytics container

## Rationale
This hybrid architecture decouples modern web interfaces from the legacy mainframe using an Anti-Corruption Layer and asynchronous messaging, ensuring zero claim loss. Furthermore, Azure Container Apps and blue-green deployments enable rapid 1-day rollbacks per claim type while working within the team's cloud skill level.