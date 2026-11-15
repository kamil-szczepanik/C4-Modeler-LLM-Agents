## Overview
Modernizes a regional insurer's claims platform via a hybrid architecture while preserving the COBOL/DB2 mainframe system of record. The Claims Web Application delivers a high-performance, secure, and accessible interface for customers, brokers, and adjusters.

## Key Elements
- Claims Web Application (Azure Static Web Apps, React, TypeScript)
- Routing & Shell Component (React Router, WCAG 2.1 AA)
- Authentication Client Component (MSAL.js, memory-only token storage)
- Claim Submission Feature Component (React Hook Form, Zod, local storage persistence)
- Adjuster Workspace Component (TanStack Query for aggressive caching)
- API Client Component (Axios, Application Insights integration)
- API Gateway / BFF (.NET Core)
- External Systems: Mainframe Claims System, Corporate Active Directory (Entra ID), Azure WAF, Azure Monitor / Application Insights

## Relationships
- Customer / Broker / Claims Adjuster -> Claims Web Application: Interacts via [HTTPS / JSON]
- Claims Web Application -> API Gateway / BFF: Authenticates and sends API requests via [HTTPS / OIDC/JWT]
- Claims Web Application components -> Azure Monitor / Application Insights: Telemetry streaming via [HTTPS]

## Technology Stack
- Azure Static Web Apps: Serverless hosting providing global CDN and integrated staging slots for rapid fallback deployments.
- React & TypeScript: Component-based UI framework ensuring type safety and maintainable frontend code.
- TanStack Query: Client-side data caching engine to maintain <2s adjuster screen loads despite slow mainframe responses.
- MSAL.js: Microsoft Authentication Library configured for memory-only token storage to mitigate XSS risks.
- React Hook Form & Zod: Client-side form management and validation.
- Axios: Centralized HTTP client managing API communication and error handling.

## Rationale
This architecture uses client-side caching and resilient form persistence to overcome high mainframe latency and connection drop constraints. Strict security controls, including memory-only token storage and WAF protection, satisfy enterprise compliance standards while accommodating the team's limited cloud experience.