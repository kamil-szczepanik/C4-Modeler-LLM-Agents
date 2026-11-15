## Overview
The system gradually replaces a 30-year-old mainframe claims system with a modern hybrid platform while maintaining legacy processing. It modernizes online claim submission and adjuster workflows via a scalable cloud architecture on Azure.

## Key Elements
* Customer / Broker: External actors submitting claims via web interface
* Claims Adjuster: Internal user managing claims in the new web application
* Azure Static Web Apps: Static web hosting component serving the React SPA
* Azure App Service: Node.js/Express Backend-for-Frontend (BFF) component
* Azure API Management: API Gateway and integration container
* Azure Container Apps: Claims Core Service container running Java / Spring Boot
* Azure Cosmos DB & Redis: Data and caching container
* Azure Service Bus: Mainframe adapter container with Dead Letter Queues
* Azure Active Directory: Identity provider for Single Sign-On (SSO)
* Mainframe COBOL/DB2: On-premises legacy system of record

## Relationships
* Customer / Broker -> Azure Static Web Apps: Submits claims [HTTPS]
* Claims Adjuster -> Azure Static Web Apps: Manages claims [HTTPS]
* Azure Static Web Apps -> Azure App Service (BFF): Forwards API requests [HTTPS / REST]
* Azure App Service -> Azure API Management: Orchestrates backend calls [HTTPS / REST]
* Azure API Management -> Azure Container Apps: Invokes microservices [gRPC / HTTPS]
* Azure App Service -> Azure Active Directory: Validates OAuth2 SSO tokens [OpenID Connect]

## Technology Stack
* React 18 & TypeScript: Frontend SPA framework for responsive user interfaces
* Node.js 20 LTS & Express: Backend-for-Frontend orchestration layer
* Azure Static Web Apps: Global CDN and static asset hosting
* Azure App Service: Managed platform for the Node.js BFF container
* Azure API Management: Secure API routing and governance
* Azure Container Apps: Serverless container runtime for microservices
* Azure Cosmos DB & Redis: Distributed persistence and high-speed caching
* Azure Service Bus: Reliable asynchronous messaging with the mainframe

## Rationale
The hybrid architecture decouples the legacy mainframe using an API Gateway and asynchronous messaging to prevent breaking batch windows. Decoupling the React frontend from the Node.js BFF ensures independent scaling, sub-2-second adjuster response times, and supports rapid one-day rollbacks.