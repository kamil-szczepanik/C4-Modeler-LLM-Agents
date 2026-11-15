## Overview
The Staff Dashboard is a React-based single-page application enabling library staff to manage circulation, cataloguing, and system administration. It provides a secure, high-performance interface enforcing strict EU-only data residency.

## Key Elements
- Staff Dashboard (React / TypeScript SPA)
- Authentication & Session Component (React Context / OIDC Client)
- Circulation Workspace (React Module with IndexedDB and Web Crypto API)
- Cataloguing & Inventory Module (React Module)
- Administration & Audit Panel (React Module with Chart.js reporting widget)
- API Client Layer (Axios / Fetch + TypeScript Interceptors)
- Quick Actions Hotkey Manager (Global React Context)

## Relationships
- Library Staff -> Staff Dashboard: Interacts via web browser [HTTPS (TLS 1.3)]
- Staff Dashboard -> API Gateway: Sends API requests and OIDC tokens [HTTPS (TLS 1.3)]
- Staff Dashboard -> S3 + CloudFront: Static asset hosting and content delivery [HTTPS (TLS 1.3)]

## Technology Stack
- React / TypeScript: Core framework for modular SPA architecture
- AWS S3 + CloudFront: Immutable, containerized CDN hosting ensuring EU-only data residency
- IndexedDB + Web Crypto API: Client-side offline buffering with encrypted local storage for circulation PII
- Chart.js: Lightweight visualization for operational reporting widgets
- HTTP-only Secure Cookies: Secure token storage preventing XSS vulnerabilities

## Rationale
Modular component decomposition separates high-frequency circulation tasks from heavy cataloguing workflows to maintain strict performance. Client-side encryption and strict token lifecycle management secure sensitive patron data while supporting offline resilience.