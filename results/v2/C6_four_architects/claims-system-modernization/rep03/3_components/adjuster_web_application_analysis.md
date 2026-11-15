## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based platform while maintaining uninterrupted legacy claims processing. It provides secure online claim submissions and adjuster interfaces while ensuring strict data consistency and zero-downtime migration of individual claim types.]

## Key Elements
[Claims Adjuster, Adjuster Web Application (React / TypeScript on Azure Static Web Apps), Authentication Module (MSAL.js), Routing & Layout Component (React Router), Claims Dashboard Component, Claim Details Workspace Component, Client-Side Cache Component (TanStack Query), BFF Client SDK / API Service Layer, API Gateway / BFF (Azure API Management and Node.js)]

## Relationships
[Claims Adjuster interacts with Routing & Layout Component and Claims Dashboard/Workspace via UI. Routing & Layout Component renders dashboard and workspace via In-Memory. Claim Details Workspace queries Client-Side Cache Component via In-Memory. BFF Client SDK uses Client-Side Cache Component via In-Memory. Adjuster Web Application sends requests to API Gateway / BFF via HTTPS. Adjuster Web Application sends telemetry to Observability & Audit Container via OpenTelemetry/HTTPS.]

## Technology Stack
[React / TypeScript for modern, responsive UI development. Azure Static Web Apps for cost-effective, cloud-ready frontend hosting. MSAL.js for Active Directory Single Sign-On integration (R-07). TanStack Query for client-side caching to meet sub-2-second performance goals despite slow mainframe responses (R-05). React Router for modular single-page application navigation.]

## Rationale
[This component architecture directly satisfies performance requirements by implementing aggressive client-side caching to overcome legacy mainframe latency. It aligns with the team's cloud skill set by utilizing managed Azure static hosting and standard React technologies.]