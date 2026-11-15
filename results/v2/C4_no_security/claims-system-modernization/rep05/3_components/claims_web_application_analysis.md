## Overview
[The Claims Web Application provides a modern React-based user interface hosted on Azure Static Web Apps to gradually replace a legacy mainframe claims system. It ensures high performance, offline capabilities, and seamless hybrid integration for customers, brokers, and adjusters.]

## Key Elements
- Claims Web Application (React, Azure Static Web Apps)
- Claim Intake Wizard (React Component Bundle)
- Adjuster Workspace (React Component Bundle)
- Broker Portal Module (React Component Bundle)
- Authentication Component (MSAL / Azure AD Wrapper)
- API Client (Axios / Fetch Wrapper)
- Offline State Manager (IndexedDB Wrapper)
- Sync Status Monitor (WebSocket / Polling Client)
- Telemetry & Feature Flag Provider (App Insights & Azure App Config SDK)
- Client-Side Error Boundaries (React Error Boundary)

## Relationships
- End Customers & Brokers -> Claims Web Application: Submit claims and manage portfolios [HTTPS]
- Claims Adjusters -> Claims Web Application: Handle claims and monitor sync status [HTTPS]
- Claims Web Application -> API Gateway: Communicates via API client [REST/HTTPS]
- Claim Intake Wizard -> Offline State Manager: Persists drafts [IndexedDB/Local Storage]
- Adjuster Workspace -> Sync Status Monitor: Displays backend replication state [Internal State]
- Telemetry & Feature Flag Provider -> Azure App Configuration: Fetches runtime feature flags [HTTPS]

## Technology Stack
- React: Core UI framework for high-performance single-page application development
- Azure Static Web Apps: Globally distributed hosting optimized for frontend static assets
- IndexedDB: Browser-based storage for local offline draft persistence
- MSAL / Azure AD: Security protocol handling OIDC/OAuth2 single sign-on
- Application Insights & Azure App Config SDK: Real-user monitoring and dynamic feature flagging

## Rationale
[This component-level architecture isolates browser-based logic to bypass mainframe latency constraints while using feature flags and sync monitoring to guarantee a safe, one-day fallback. It successfully bridges low cloud team experience with robust offline and security requirements.]