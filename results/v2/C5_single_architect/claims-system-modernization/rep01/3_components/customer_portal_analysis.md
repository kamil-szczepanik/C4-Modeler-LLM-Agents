## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises COBOL/DB2 mainframe with a modern hybrid cloud platform on Azure West Europe. It enables online claim submission and adjuster processing while maintaining consistency and zero data loss during the 3-year migration.

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- On-premises Active Directory and Legacy Mainframe (COBOL/DB2)
- Azure Front Door / App Gateway (API Gateway)
- Customer Portal (React SPA on Azure Static Web Apps)
- Adjuster Workspace (Node.js Backend-for-Frontend on Azure App Service)
- Claims Core Engine (Java Spring Boot on Azure Container Apps)
- Integration Layer (Azure Event Hubs with Apache Camel)
- Azure Database for PostgreSQL (Migrated Claims Database)
- Customer Portal Components: Authentication Module (MSAL.js), Claim Submission Form (Formik/Yup), Claim Status Tracker, API Client Layer (Axios)

## Relationships
- Customers & Brokers -> Customer Portal: Submitting claims online via HTTPS
- Customer Portal -> API Gateway: Routing requests via HTTPS using OpenID Connect
- Customer Portal -> Azure Active Directory: Single sign-on authentication via OIDC/OAuth2 (MSAL.js)
- Claim Status Tracker -> API Gateway: Polling for updates via HTTPS/REST

## Technology Stack
- React 18 with TypeScript: Chosen for type safety and ease of use given the team's limited cloud experience
- Tailwind CSS: Used for rapid and consistent UI styling
- Axios: Utilized in the API Client Layer for managing HTTP requests and interceptors
- Azure Static Web Apps: Hosts and globally distributes the React SPA static assets
- Azure Active Directory (MSAL.js): Implements SSO to meet security requirements

## Rationale
This architecture decouples the modern cloud-native interface from the rigid legacy mainframe using an API gateway and integration layer, allowing gradual claim type migration without breaking batch windows. The simplified REST polling approach fits the team's skill set while securely meeting performance, security, and maintainability requirements.