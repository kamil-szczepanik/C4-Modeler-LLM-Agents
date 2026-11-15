## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
- **Patron Portal SPA** (React, TypeScript)
- **Staff Portal SPA** (React, TypeScript)
- **API Client Service** (Axios/Fetch wrapper)
- **State Management Store** (Zustand/Redux Toolkit)
- **Session & Localization Manager** (JavaScript/Cookie utility)
- **Error Boundary & Telemetry Reporter** (Sentry/Custom JS)
- **API Gateway** (NGINX/Envoy)
  - **Routing & Reverse Proxy Engine** (Envoy Core)
  - **Authentication & Authorization Filter** (JWT/OAuth2 module)
  - **Rate Limiter** (Token Bucket algorithm)

## Relationships
- *Patron Portal SPA* & *Staff Portal SPA* -> *API Client Service*: Dispatches requests [In-Process]
- *Patron Portal SPA* & *Staff Portal SPA* -> *Session & Localization Manager*: Validates session and applies EU locales [In-Process]
- *Patron Portal SPA* & *Staff Portal SPA* -> *Error Boundary & Telemetry Reporter*: Catches runtime exceptions [In-Process]
- *API Client Service* -> *API Gateway*: Sends API requests [HTTPS/REST/GraphQL]
- *Error Boundary & Telemetry Reporter* -> *API Gateway*: Forwards client telemetry [HTTPS/REST]
- *Web Application* -> *Routing & Reverse Proxy Engine*: Sends API requests [HTTPS/REST/GraphQL]
- *Routing & Reverse Proxy Engine* -> *Authentication & Authorization Filter*: Inspects tokens [In-Process]

## Technology Stack
- **React & TypeScript**: Client-side SPAs for patron and staff interfaces
- **Zustand/Redux Toolkit**: Client-side state and caching
- **JavaScript/Cookie utility**: EU session binding and localization
- **Sentry/Custom JS**: Client-side error telemetry for performance tracking
- **NGINX/Envoy**: API Gateway routing and ingress security
- **Token Bucket algorithm**: Rate-limiting to protect downstream services

## Rationale
The component decomposition cleanly separates patron and staff workflows while centralizing EU session enforcement and telemetry. This ensures strict data residency compliance and protects search performance SLAs (<800 ms).