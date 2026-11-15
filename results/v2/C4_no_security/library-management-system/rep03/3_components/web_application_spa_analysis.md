## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It strictly enforces EU-only data residency while ensuring high-performance patron searches.

## Key Elements
- **Web Application (SPA):** React and TypeScript frontend hosted on an EU-region CDN.
- **Routing & Shell Component:** Manages client-side routing, role-based access, and offline-recovery states using React Router.
- **Catalog & Search Component:** Implements item search interfaces for physical and digital assets.
- **Circulation & Self-Service Component:** Handles patron checkouts and renewals.
- **API Client Layer:** Axios/GraphQL client with JWT interceptors and Sentry error tracking.
- **Telemetry & Monitoring Component:** Captures metrics for EU-hosted analytics endpoints.
- **API Gateway:** Nginx/Kong gateway managing backend traffic.

## Relationships
- **Library Patrons, Librarians, Library Administrators** -> **Web Application (SPA):** Interacts via HTTPS [HTTPS]
- **Web Application (SPA)** -> **API Gateway:** Communicates via REST/GraphQL over HTTPS [REST/GraphQL over HTTPS]
- **Routing & Shell Component** -> **Catalog & Search Component / Circulation & Self-Service Component:** Renders views based on authenticated roles [In-memory]
- **Feature Components & API Client Layer** -> **Telemetry & Monitoring Component:** Reports exceptions and performance timings [In-memory asynchronous calls]
- **Telemetry & Monitoring Component** -> **EU-hosted Analytics Endpoint:** Transmits payloads strictly within the EU [HTTPS]

## Technology Stack
- **React and TypeScript:** Chosen for building a responsive, maintainable Single Page Application.
- **EU-region CDN:** Deployed to ensure low latency and comply with EU-only data residency constraints.
- **Axios/GraphQL:** Utilized for secure, typed communication with the API Gateway.
- **Sentry:** Integrated for real-user monitoring (RUM) and error tracking to maintain performance SLAs.
- **GitHub Actions:** Implements CI/CD pipelines, automated CDN cache invalidation, and bundle-size budgeting.

## Rationale
This architecture uses a modern React SPA coupled with strict CDN controls and EU-hosted telemetry to meet data residency constraints. Component-level caching and performance budgeting directly support the 99th-percentile search response requirement under 800 ms.