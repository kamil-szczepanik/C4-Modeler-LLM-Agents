## Overview
- Modernizes a regional insurer's claims platform by gradually replacing a 30-year-old mainframe while ensuring zero lost claims.
- Combines an on-premises COBOL/DB2 mainframe with cloud-native Azure services to deliver modern digital claim processing.

## Key Elements
- Policyholders and Brokers (Users)
- Claims Adjusters (Users)
- Customer Portal (React SPA / Azure Container Apps)
- Adjuster Workspace (Node.js/Java / Azure Container Apps)
- Anti-Corruption Layer (ACA Integration Service)
- Azure Service Bus (Azure Service Bus)
- Legacy Mainframe (COBOL/DB2 on-prem)
- Azure Active Directory (Identity Provider)

## Relationships
- Policyholders and Brokers -> Customer Portal: Submits online claims [HTTPS/TLS 1.3]
- Customer Portal -> Azure API Gateway: Routes requests and submits data [HTTPS]
- Customer Portal -> Azure Service Bus: Publishes and subscribes to events [AMQP]
- Customer Portal -> Azure Active Directory: Authenticates users [OIDC/OAuth2 with PKCE]
- Customer Portal Components: Claims UI, Auth Manager, API Client, and State & Storage Components interact internally [Local Storage API / TypeScript]

## Technology Stack
- React/TypeScript: Powers the Customer Portal frontend for high responsiveness and maintainability.
- Azure Container Apps: Hosts containers with managed scaling to accommodate low cloud team experience.
- Azure Service Bus: Enables reliable asynchronous messaging to prevent lost claims during migration.
- Azure Active Directory: Centralizes single sign-on security via OIDC and OAuth2.
- Bicep/Terraform: Automates infrastructure provisioning to enforce immutable deployments.

## Rationale
- The hybrid architecture abstracts expensive mainframe changes through an anti-corruption layer while migrating claim types individually within a 3-year timeline.
- Managed cloud services on Azure reduce operational overhead for a team with limited cloud experience while satisfying strict performance and security constraints.