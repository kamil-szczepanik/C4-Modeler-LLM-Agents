## Overview
[The Customer Portal provides a modern React-based web interface for customers and brokers to submit insurance claims online. It integrates with Azure services and legacy systems via an API gateway.]

## Key Elements
- [Customer Portal (React SPA)]
- [Authentication Controller (TypeScript / MSAL.js)]
- [Claim Submission Wizard (React Component / Formik)]
- [Document Uploader Component (React)]
- [API Client Service (Axios / Fetch)]
- [Azure Static Web Apps / CDN]
- [Azure Active Directory]
- [Azure Blob Storage]

## Relationships
- [Customers & Brokers -> Customer Portal: Interacts for online submissions [HTTPS/REST]]
- [Authentication Controller -> Azure Active Directory: Authenticates users and acquires tokens [OpenID Connect / OAuth 2.0]]
- [Claim Submission Wizard -> API Client Service: Submits claim payloads [HTTPS/REST]]
- [Claim Submission Wizard -> Document Uploader Component: Initiates file attachments [HTTPS]]
- [Document Uploader Component -> Azure Blob Storage: Uploads binaries directly [HTTPS/PUT via Pre-signed URLs]]
- [Customer Portal -> Azure Static Web Apps / CDN: Serves static frontend assets [HTTPS]]

## Technology Stack
- [React & TypeScript: Frontend UI components and type safety]
- [MSAL.js: In-memory token management with Auth Code Flow + PKCE]
- [Azure Static Web Apps & CDN: Stateless static hosting and global delivery]
- [Azure Blob Storage: Secure binary file attachments using pre-signed URLs]
- [Terraform / Bicep: Infrastructure as Code for environment provisioning and CORS rules]

## Rationale
[This architecture secures client-side interactions and protects backend gateways by offloading large file uploads directly to storage. It accommodates low cloud experience through standardized static hosting and managed infrastructure templates.]