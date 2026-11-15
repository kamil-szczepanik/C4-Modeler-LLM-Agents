## Overview
The Customer Portal is a React single-page application hosted on Azure Static Web Apps that provides policyholders and brokers with an intuitive, secure interface for online claim submission and tracking. It acts as the primary user-facing entry point within the hybrid Insurance Claims Modernization platform.

## Key Elements
* Customer Portal (React SPA in Azure Static Web Apps)
* Claim Submission Wizard component
* Claim Tracking Dashboard component
* Broker Portfolio Manager component
* Auth & Session Manager component
* Azure Static Web Apps Built-in Auth
* Azure API Management

## Relationships
* Customer Portal -> Azure Static Web Apps Auth: Manages secure session cookies [HTTPS]
* Claim Submission Wizard -> Azure API Management: Submits claim payloads [HTTPS / REST]
* Broker Portfolio Manager -> Azure API Management: Fetches authorized client claims [HTTPS / REST with JWT]
* Auth & Session Manager -> Azure Active Directory: Acquires tokens [OAuth 2.0 / OpenID Connect]

## Technology Stack
* React & TypeScript: Core UI framework for maintainable frontend development
* Azure Static Web Apps: Hosting and built-in authentication routing to minimize operational overhead for a cloud-inexperienced team
* Zod & React Hook Form: Client-side validation ensuring robust draft data integrity
* TanStack Query: Lightweight server-state management avoiding complex store libraries
* IndexedDB: Local browser storage for offline-resilient claim draft persistence

## Rationale
This architecture balances stringent security and consistency requirements (R-04, R-07) with the team's low cloud experience by leveraging managed Azure platform features. A lean SPA design avoids unnecessary infrastructure complexity while delivering sub-two-second performance and robust multi-client support for brokers.