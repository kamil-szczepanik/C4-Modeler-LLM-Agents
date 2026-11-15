## Overview
[The Online Bookstore Admin SPA is a React-based single-page application hosted on Amazon S3 and CloudFront for administrative staff. Its core purpose is to provide secure management of book catalogues, customer orders, and compliance operations.]

## Key Elements
- Admin Staff
- Admin SPA (React, Vite, Amazon S3, CloudFront)
- Authentication Component (TypeScript, React Context)
- Authorization & RBAC Guard Component (TypeScript, React Router)
- Catalog Management Component (React, TanStack Query)
- Order & Support Dashboard Component (React, AG-Grid)
- Audit & Telemetry Logger Component (TypeScript)
- Catalog API Service & Order API Service
- AWS API Gateway & AWS WAF
- Amazon Cognito
- AWS Distro for OpenTelemetry (ADOT Sidecar)

## Relationships
- Admin Staff -> Admin SPA: Interacts via browser [HTTPS]
- Admin SPA -> Amazon Cognito: Authenticates admin users [HTTPS/OIDC]
- Authorization Guard -> Authentication Component: Validates user claims [React Context]
- Catalog Management -> Catalog API Service: Invokes queries and mutations [TypeScript Calls]
- Order Dashboard -> Order API Service: Manages order operations [TypeScript Calls]
- Catalog Management & Order Dashboard -> Audit & Telemetry Logger: Dispatches action events [TypeScript Calls]
- Catalog & Order API Services -> AWS API Gateway: Transmits authenticated payloads [HTTPS, JSON, JWT Bearer Token]
- Admin SPA -> AWS Distro for OpenTelemetry (ADOT Sidecar): Exports performance metrics and errors [OTLP/HTTP, HTTPS]

## Technology Stack
- React with Vite: Fast frontend bundling and component architecture
- TypeScript: Type safety across UI and API layers
- TanStack Query: Caching and state management for catalogue listings
- AG-Grid: High-performance data tables for order management
- Amazon S3 & CloudFront: Static asset hosting and global content delivery
- Amazon Cognito: Managed OIDC identity provider for authentication

## Rationale
[This component architecture enforces strict RBAC and domain separation to meet OWASP security and GDPR compliance requirements. Static hosting via CloudFront guarantees high performance and low latency globally.]