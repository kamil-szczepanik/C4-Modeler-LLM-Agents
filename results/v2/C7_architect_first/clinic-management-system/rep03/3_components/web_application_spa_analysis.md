## Overview
The Web Application (SPA) container serves as the primary frontend interface for the Clinic Management System, delivering role-based clinical and administrative workflows to healthcare staff and patients. It ensures high-performance access and strict HIPAA/GDPR compliance across hybrid cloud and on-premise deployments.

## Key Elements
- Routing & State Management Component (React Router, Zustand, Zod)
- RBAC Router Guard Component
- Authentication Interceptor Component (OAuth2/OIDC)
- Session Lifecycle Manager Component
- Clinical Workspace Component
- API Client Component (Axios, OpenTelemetry)
- Infrastructure & Delivery: AWS S3, Amazon CloudFront (`eu-central-1`), on-premise Nginx caching proxies

## Relationships
- Users -> Web Application (SPA): Access via HTTPS/TLS terminated at the API Gateway [HTTPS / TLS]
- Web Application (SPA) -> API Gateway: Sends requests to backend services [HTTPS / REST / JSON]
- Authentication Interceptor Component -> Identity Provider (IdP): Token exchange and MFA triggers [OAuth2 / OIDC]
- Delivery CDN / Proxies -> Web Application (SPA): Serves immutable Vite static assets with nonces-based CSP [HTTPS]

## Technology Stack
- React 18 & TypeScript: Core UI framework and type safety for reliable frontend execution
- Vite: High-performance build tool enabling aggressive code-splitting and asset optimization
- Zustand & React Router: In-memory session state management and client-side routing
- Zod: Runtime claim validation for RBAC router guards
- Axios & OpenTelemetry: Standardized API client wrapping requests and capturing browser tracing for P95 < 1s metrics

## Rationale
This architecture uses memory-only state management, strict nonces-based Content Security Policies, and prohibits local PHI caching to satisfy strict HIPAA and GDPR security mandates. Role-based dynamic rendering and aggressive asset optimization ensure clinician efficiency and meet the sub-second performance requirements under a hybrid high-availability model.