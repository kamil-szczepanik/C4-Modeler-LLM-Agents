## Overview
[Modernizes the legacy insurance claims system by gradually migrating claim types to a hybrid cloud platform. The Customer Portal enables online claim submission and tracking while the mainframe remains the system of record.]

## Key Elements
* Customer/Broker: External human users initiating and tracking claims
* Customer Portal: React Single Page Application hosted in Azure Static Web Apps
* Authentication Wrapper: MSAL.js component handling OIDC/OAuth2 SSO
* Claim Submission Form: React component managing multi-step claim wizards
* Document Uploader: React component interacting with Azure Blob Storage
* Claim Tracker View: React component using HTTP Polling
* Claim Routing & Feature Service: Backend API in Azure Container Apps
* Azure Blob Storage: Object storage for attachments with server-side malware scanning

## Relationships
* Customer/Broker -> Customer Portal: Submits claims and tracks status [HTTPS over Internet]
* Authentication Wrapper -> Azure Active Directory: Authenticates users [OIDC over HTTPS]
* Claim Submission Form -> Claim Routing & Feature Service: Submits claim data [HTTP/REST over HTTPS]
* Document Uploader -> Azure Blob Storage: Uploads attachments [HTTPS PUT via short-lived SAS tokens]
* Claim Tracker View -> Claim Routing & Feature Service: Polls claim status [HTTP Polling over HTTPS]

## Technology Stack
* React SPA: Client-side framework chosen for rich UI interactivity
* Azure Static Web Apps: Serverless hosting for global CDN delivery and low operational overhead
* MSAL.js: Standard library for secure Azure AD integration and in-memory token storage
* Azure Blob Storage: Scalable cloud storage with SAS tokens to offload app-tier bandwidth
* HTTP Polling: Replaced WebSockets to reduce persistent connection operational complexity

## Rationale
[This architecture uses managed serverless services like Azure Static Web Apps to accommodate the team's limited cloud experience while ensuring high security, performance, and maintainability. It successfully decouples the frontend customer experience from the legacy mainframe.]