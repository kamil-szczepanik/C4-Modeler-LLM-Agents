## Overview
- This hybrid system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern platform.
- It modernizes customer and broker claim submissions and adjuster workflows while keeping the mainframe as the system of record.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Web Application (React/Next.js on Azure App Service)
- Claims API Gateway / Backend-for-Frontend (.NET Core on Azure Container Apps)
- Azure Active Directory

## Relationships
- Customers, Brokers, and Adjusters -> Web Application: Submits and manages claims via HTTPS/TLS 1.3 with OIDC/OAuth2 SSO
- Web Application -> Azure Active Directory: Authenticates users via OIDC/OAuth2
- Web Application -> Claims API Gateway / Backend-for-Frontend: Sends API and UI requests via HTTPS REST/GraphQL

## Technology Stack
- Next.js / React: Selected for Server-Side Rendering to meet the sub-2-second adjuster screen load requirement
- Azure App Service: Provides a managed hosting environment for the frontend web application with minimal cloud experience required
- Microsoft Authentication Library (MSAL) / NextAuth.js: Secures authentication and integrates with enterprise Active Directory
- Zustand / React Query: Manages client state and optimistic UI updates to mask backend mainframe latency

## Rationale
- The hybrid architecture isolates expensive mainframe changes while incrementally migrating claim types over three years.
- Next.js and client-side caching meet strict performance and maintainability goals despite legacy backend latencies.