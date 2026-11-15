## Overview
Modernizes a regional insurer's legacy mainframe by introducing a cloud-based web platform for online claim submissions and adjuster processing. It enables gradual claim type migration while maintaining system reliability and low latency.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **Systems**: Customer Portal, Adjuster Web App, Claims API Gateway, Claims Core Services, Notification Service, Feature/Routing Service, Integration ACL Worker, Legacy Mainframe System, Active Directory (IdP)
- **Containers**: Customer Portal SPA (React, TypeScript, Azure Static Web Apps), Azure Blob Storage, Azure SQL Database, Azure Service Bus

## Relationships
- Customers/Brokers -> Customer Portal: Interacts with and manages claims [HTTPS / REST]
- Customer Portal -> Claims API Gateway: Sends API requests [HTTPS / REST (TLS 1.3, OAuth 2.0 / OIDC)]
- Customer Portal -> Azure Blob Storage: Uploads documents securely via presigned URLs [HTTPS]

## Technology Stack
- **Azure Static Web Apps**: Hosts the React/TypeScript Single Page Application for fast global distribution and CI/CD integration.
- **Azure Blob Storage**: Stores uploaded claim documents via secure, short-lived presigned URLs to offload binary payloads from the API gateway.
- **OAuth 2.0 / OIDC with PKCE**: Secures browser-based authentication without storing client secrets in the public SPA.
- **Azure App Configuration**: Implements feature flagging for rapid fallback capabilities.

## Rationale
This hybrid architecture isolates the legacy mainframe from direct web traffic while providing a modern, scalable cloud interface. Using managed Azure services minimizes the operational burden for a team with low cloud experience.