## Overview
[The system modernizes a 30-year-old mainframe claims system through a hybrid cloud platform while ensuring uninterrupted legacy batch processing. It provides secure online claim submissions and high-performance adjuster workflows.]

## Key Elements
- Router / Navigation Component (React Router)
- Authentication Wrapper (MSAL.js)
- Claim Submission Feature Module (React Hook Form / Zod)
- Adjuster Workbench Module (TanStack Query)
- Feature Flag / Claim Type Resolver
- API Client Layer
- Audit & Telemetry Interceptor (OpenTelemetry JS / App Insights SDK)
- State Management Store (Zustand)

## Relationships
- Authentication Wrapper -> API Gateway / Edge: Validates and sends tokens [HTTPS (OIDC/Bearer)]
- Claim Submission & Adjuster Workbench -> API Gateway / Edge: Fetches and mutates claim data [HTTPS (REST)]
- API Client Layer -> API Gateway / Edge: Proxies all REST requests [HTTPS (REST)]
- API Client Layer -> Audit & Telemetry Interceptor: Emits telemetry events [In-memory / SDK]
- Authentication Wrapper & Feature Modules -> State Management Store: Manages session and UI state [In-memory]

## Technology Stack
- React on Azure Static Web Apps: Modern, lightweight frontend hosting
- TanStack Query: Local caching and optimistic updates to meet sub-2s UI latency (R-05)
- Zustand: Lightweight cross-component UI state management
- OpenTelemetry JS / Application Insights SDK: End-to-end traceability and audit compliance (R-04)
- MSAL.js: Secure Azure Active Directory Single Sign-On integration (R-07)

## Rationale
[This architecture successfully satisfies the hybrid constraints by decoupling the modern React frontend from the legacy mainframe via an API gateway. It ensures high performance and incremental claim migration capabilities while maintaining strict consistency and traceability.]