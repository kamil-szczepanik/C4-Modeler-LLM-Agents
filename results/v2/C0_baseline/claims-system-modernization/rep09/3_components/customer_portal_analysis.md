## Overview
[Insurance Claims Modernization]
Gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform over three years while maintaining legacy operations.

## Key Elements
- Policyholders and Brokers (Users)
- Customer Portal (React, Azure Static Web Apps)
- Backend APIs (.NET, Azure Container Apps)
- Legacy Mainframe (COBOL/DB2, On-Premises)
- Azure API Management (APIM)
- Azure Blob Storage
- Azure Active Directory (Azure AD)
- Azure Application Insights

## Relationships
- Customer Portal -> Azure API Management (APIM): Routes external traffic [HTTPS]
- Customer Portal (Authentication Client) -> Azure AD: Authenticates users [OIDC/OAuth2 via HTTPS]
- Customer Portal (Claim Submission Controller) -> Backend APIs: Submits claim payloads [HTTPS/JSON]
- Customer Portal (Document Upload Manager) -> Azure Blob Storage: Uploads binaries via server-brokered SAS tokens [HTTPS]
- Customer Portal (Claim Tracker Dashboard) -> Backend APIs: Fetches claim status via polling [HTTPS/JSON]

## Technology Stack
- React & React Hook Form with Zod: Frontend UI and multi-step claim validation
- Azure Static Web Apps: Hosting for the React Single Page Application (SPA)
- MSAL.js: Client-side authentication and role-aware session management via Azure AD
- Azure Blob Storage: Secure binary file storage using short-lived SAS tokens
- Azure Application Insights: Real User Monitoring and synthetic transaction monitoring

## Rationale
[This hybrid architecture decouples customer-facing digital channels from the legacy mainframe via API Management, ensuring low-latency adjuster screens and seamless multi-year migration without altering expensive core legacy interfaces.]