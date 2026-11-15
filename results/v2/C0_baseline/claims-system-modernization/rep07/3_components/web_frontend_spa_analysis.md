## Overview
[The system is a modern hybrid insurance claims platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous operations. The core purpose is to enable online claim submissions, adjuster workflows, and granular claim-type migrations without business disruption.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Migration Product Owners
- Web Frontend (SPA) (Azure Static Web Apps, React)
- Claims API Gateway (Azure API Management)
- Core Claims Service (Azure Container Apps)
- Mainframe Anti-Corruption Layer (ACL) (Azure Event Hubs / Kafka)
- Integration & Transformation Worker (Azure Container Apps)
- Operational Observability & Dead-Letter Container (Azure Container Apps, Azure Monitor)

## Relationships
- End Customers & Brokers -> Web Frontend (SPA): Submit and manage claims [HTTPS / REST / WebSockets]
- Claims Adjusters -> Web Frontend (SPA): Manage claims and adjusters [HTTPS / REST / WebSockets]
- Migration Product Owners -> Web Frontend (SPA): Monitor migration and rollbacks [HTTPS / REST / WebSockets]
- Web Frontend (SPA) -> Claims API Gateway: Sends API requests [HTTPS / REST]
- Claims API Gateway -> Core Claims Service: Routes service requests [HTTPS / gRPC]
- Core Claims Service -> Mainframe Anti-Corruption Layer (ACL): Publishes domain events [AMQP / Kafka Protocol]
- Mainframe Anti-Corruption Layer (ACL) -> Legacy Mainframe: Synchronizes state [DB2 Direct / Batch / SNA]

## Technology Stack
- Azure Static Web Apps: Hosts the React SPA with global CDN distribution to suit the team's limited cloud experience.
- React with MSAL.react: Implements OIDC/OAuth2 authentication via Authorization Code Flow with PKCE for Azure AD integration.
- TanStack Query: Provides local state caching to meet sub-2s performance requirements despite slow mainframe responses.
- IndexedDB with Web Crypto API (AES-GCM): Secures offline claim drafts locally on the client.
- Azure Application Insights: Tracks client-side performance and telemetry with automated PII scrubbing.

## Rationale
[This hybrid architecture isolates expensive mainframe interactions while modernizing front-end and integration layers incrementally. It satisfies strict operational constraints, ensures zero-loss migration consistency, and accommodates the team's limited cloud experience through managed Azure services.]