## Overview
[The Customer/Broker Portal provides a modern, secure web interface for online claim submissions, document uploads, and real-time status tracking. It integrates into a hybrid architecture to streamline user interactions while maintaining legacy mainframe connectivity.]

## Key Elements
- SPA Frontend (TypeScript / React on Azure Static Web Apps)
- Portal BFF (Node.js / Express on Azure Container Apps)
- Document Uploader (Node.js component)
- Azure API Management (API Gateway)
- Azure Blob Storage
- Active Directory / Entra ID

## Relationships
- SPA Frontend -> Portal BFF: Authenticated API calls [HTTPS / REST, JSON]
- Portal BFF -> Backend-for-Frontend (System Container): Forwards domain commands [HTTPS / gRPC]
- Document Uploader -> Azure Blob Storage: Direct secure binary streaming [HTTPS / SAS]
- Active Directory / Entra ID -> SPA Frontend: User authentication [OAuth 2.0 / OpenID Connect]

## Technology Stack
- TypeScript / React: Chosen for responsive, mobile-friendly UI development.
- Node.js / Express: Lightweight backend for handling API routing and session management.
- Azure Static Web Apps: Native CDN distribution and atomic deployments for frontend hosting.
- Azure Container Apps: Containerized execution for the BFF without complex Kubernetes overhead.
- Azure Blob Storage: Secure binary object storage for claim attachments using SAS tokens.

## Rationale
[This architecture balances stringent security controls and performance targets with the team's limited cloud experience by utilizing managed Azure services. It offloads static content and file processing to specialized cloud primitives while keeping the core ingestion secure and maintainable.]