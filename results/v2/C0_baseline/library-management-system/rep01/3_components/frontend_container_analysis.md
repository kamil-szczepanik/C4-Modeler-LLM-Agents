## Overview
- Single Page Application (SPA) providing self-service and administrative UIs for the Library Management System.
- Hosted on an EU Content Delivery Network (CDN) to ensure low-latency access and strict compliance with EU-only data residency constraints.

## Key Elements
- **Frontend Container**: React, TypeScript SPA hosted on an EU CDN.
- **Routing & Auth Module**: React Router, OIDC Client handling navigation and authentication.
- **Catalog UI Component**: Renders item searches and filtering.
- **Circulation UI Component**: Manages self-service checkouts, renewals, and admin workflows.
- **API Client Service**: Axios/Fetch wrapper injecting correlation IDs and observability hooks.
- **External Systems**: External Identity Provider, API Gateway, Sentry, EU CDN.

## Relationships
- Library Patrons, Librarians, Library Administrators -> Frontend Container: Accesses portals [HTTPS over TLS 1.3]
- Routing & Auth Module -> External Identity Provider: Authenticates users [Authorization Code Flow with PKCE, OIDC]
- Catalog UI & Circulation UI -> API Client Service: Dispatches UI actions [Internal TypeScript calls]
- API Client Service -> API Gateway: Sends backend requests [HTTPS / REST APIs]
- Frontend Container -> EU CDN: Serves static assets [HTTPS, Subresource Integrity (SRI)]

## Technology Stack
- React & TypeScript: Core UI framework for type safety and component reusability.
- EU CDN: Ensures static asset caching, edge security headers, and EU data residency.
- OIDC Client: Secure authentication integration using Authorization Code Flow with PKCE.
- Axios/Fetch: Network communication handling API requests and correlation ID injection.

## Rationale
- Hosting the SPA on an EU CDN guarantees compliance with EU-only data residency constraints.
- Optimized components and client-side caching ensure search response performance remains under 800 ms.