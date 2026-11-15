## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern cloud-native architecture. It processes claims consistently while maintaining hybrid operations with the legacy system of record.

## Key Elements
- Claims Web Application (Azure Static Web Apps / React SPA)
- Claims Dashboard Component
- Claim Form & Validation Component
- API Client Service
- Auth & RBAC Routing Component
- API Gateway & BFF (Azure Container Apps / Node.js or .NET)
- Integration & Anti-Corruption Layer (Azure Functions & Service Bus)
- New Claims Database (Azure SQL Database)
- Telemetry & Security (Azure Application Insights Browser SDK, Azure Key Vault)

## Relationships
- Customers, Brokers, Claims Adjusters -> Claims Web Application: Interacts via HTTPS/JSON
- Claims Web Application -> API Gateway & BFF: Communicates via HTTPS/JSON
- Claims Web Application -> Azure Application Insights: Forwards telemetry via OpenTelemetry headers
- Auth & RBAC Routing Component -> API Gateway & BFF: Validates session state and fetches permissions via HTTPS/JSON

## Technology Stack
- Azure Static Web Apps: Hosts React SPA with global CDN distribution and automated CI/CD pipelines
- React & React Router: Delivers fast client-side rendering and navigation
- Zustand: Manages lightweight, short-lived memory state securely in-browser
- Axios: Handles asynchronous HTTP/JSON communication with the BFF
- Azure Application Insights Browser SDK: Enables Real User Monitoring (RUM) and error tracking

## Rationale
This architecture ensures adjuster screens load in under 2 seconds through local state caching and optimistic UI updates despite slow mainframe responses. It isolates the untrusted client-side SPA from sensitive tokens and business logic using a BFF pattern, meeting strict security and hybrid migration constraints.