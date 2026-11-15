## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system ensures EU-only data residency and sub-800ms search responses.

## Key Elements
- Library Patrons, Staff, and Administrators
- Web Application Frontend Container (React/TypeScript SPA)
- Search & Discovery Module, Circulation Management Module, Admin Configuration Dashboard
- Mobile API Gateway (Node.js/Express)
- Authentication & Session Service (Node.js)
- External CDN with EU-restricted edge nodes

## Relationships
- Library Patrons & Staff -> Web Application Frontend: HTTPS/REST, WebSockets [HTTPS, WebSockets]
- Library Administrators -> Web Application Frontend: HTTPS/REST [HTTPS, REST]
- Web Application Frontend -> Mobile API Gateway: API requests [HTTPS/REST]
- Web Application Frontend -> Authentication & Session Service: Session management with HTTP-only cookies [HTTPS]

## Technology Stack
- React/TypeScript: UI component implementation with React Query for state management
- Vite: Rapid SPA bundling and asset compilation
- Nginx Alpine / S3-compatible EU storage: Static asset hosting and deployment
- OpenTelemetry JS SDK: Real User Monitoring and distributed tracing
- Axios: HTTP client with custom interceptors for correlation IDs

## Rationale
- Modular React components and feature-driven directory patterns optimize initial load times and maintain sub-800ms search SLAs.
- Geo-distributed CDNs with EU-restricted edge nodes and strict CSP security policies enforce regional data residency and stringent security requirements.