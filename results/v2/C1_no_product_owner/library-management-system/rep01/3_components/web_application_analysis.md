## Overview
The Web Application is a React and TypeScript Single Page Application served via AWS CloudFront Frankfurt to provide public and academic library self-service portals. It ensures EU-only data residency while supporting high-performance catalog searches and circulation management.

## Key Elements
- Router & Layout Component (React Router)
- Authentication & Session Manager (OAuth2/OIDC, HttpOnly cookies)
- Catalogue & Search UI Module (TanStack Query / React Query)
- Circulation & Self-Service Portal Module (TanStack Query)
- API Client (Axios / Fetch with Zod validation)
- Performance Monitoring and Real User Monitoring (OpenTelemetry, AWS CloudWatch Synthetics)
- AWS CloudFront Frankfurt (CDN edge)

## Relationships
- AWS CloudFront Frankfurt -> Web Application: Serves static assets and application [HTTPS / TLS 1.3]
- Router & Layout Component -> UI Modules: Renders patron and staff views [React Context/Props]
- UI Modules -> API Client: Sends validated payloads [TypeScript function calls]
- API Client -> API Gateway: Communicates with backend [HTTPS / REST, Frankfurt endpoints]

## Technology Stack
- React & TypeScript: Core UI framework for type safety and component reusability
- TanStack Query: Client-side caching and request deduplication to achieve <800ms search response (R-05)
- Zod: Client-side input validation for security and data integrity
- AWS CloudFront Frankfurt: Edge delivery ensuring EU-only data residency compliance
- OpenTelemetry: Real User Monitoring and Core Web Vitals tracking

## Rationale
This architecture uses React, TypeScript, and TanStack Query to optimize performance and meet the strict <800ms search requirement (R-05). Deploying via AWS CloudFront Frankfurt strictly enforces EU-only data residency while maintaining low-latency global edge delivery.