## Overview
The Customer Portal is a web-based container that enables online claim submission for customers and brokers while integrating with enterprise security. It decomposes into modular frontend and backend components deployed on Azure to support a hybrid cloud modernization strategy.

## Key Elements
- **Claim Frontend UI**: React single-page application rendering dynamic claim forms.
- **Authentication Middleware**: Node.js module handling OpenID Connect and SSO integration.
- **Claim Submission Controller**: Node.js Backend-for-Frontend managing claim payload validation and routing.
- **Claim Type Configuration Client**: Component fetching dynamic claim-type schemas at runtime.
- **External Dependencies**: Azure API Management (API Gateway), Claims Anti-Corruption Layer, and Insurer's Active Directory.

## Relationships
- **Claim Frontend UI** -> **Authentication Middleware**: Authenticates user session [HTTPS]
- **Claim Frontend UI** -> **Claim Submission Controller**: Submits claim data [HTTPS/JSON]
- **Claim Frontend UI / Claim Submission Controller** -> **Claims Anti-Corruption Layer**: Fetches dynamic claim form schemas and forwards validated claims [HTTPS/REST]
- **API Gateway** -> **Customer Portal**: Routes incoming external traffic [HTTPS]

## Technology Stack
- **React**: Frontend UI framework for dynamic form rendering.
- **Node.js / Express**: Backend-for-Frontend runtime for handling controllers and middleware.
- **Azure App Service**: Hosting platform matching the team's cloud experience level.
- **OpenID Connect / Azure App Service Easy Auth**: Security protocols for Active Directory SSO.

## Rationale
This component architecture separates concerns to maintain high security, support dynamic runtime claim-type toggling, and enable rapid rollbacks. The chosen technologies match the team's skillset while integrating cleanly into the hybrid cloud landscape.