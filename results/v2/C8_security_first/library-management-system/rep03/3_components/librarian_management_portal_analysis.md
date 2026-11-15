## Overview
- **System**: Library Management System for public and academic libraries.
- **Core Purpose**: Provide catalogue, circulation, and self-service capabilities with strict EU data residency.

## Key Elements
- **Users**: Patrons, Librarians, Library Administrators
- **Containers**: Librarian Management Portal (React/TypeScript SPA), API Gateway (Kong / Envoy), Search Microservice, Circulation & Catalogue Microservice
- **Components**: Authentication & Session Manager, Cataloguing & Inventory UI Module, Circulation Desk Module, Audit Logging Service, Accessibility Wrapper & Design System, Batch Processing State Controller

## Relationships
- Librarians -> Librarian Management Portal: HTTPS (TLS 1.3)
- Librarian Management Portal -> API Gateway: HTTPS
- Circulation Desk Module -> API Gateway: REST/JSON over HTTPS with offline queueing fallback
- Batch Processing State Controller -> API Gateway: REST/JSON over HTTPS for chunked uploads

## Technology Stack
- **Frontend Framework**: React with TypeScript for the SPA container
- **Routing & State**: React Router for SPA routing; Zustand for state management
- **Networking**: Axios with strict interceptors for JWT injection
- **Infrastructure**: EU-hosted CDN backed by immutable object storage for static assets
- **Security Protocols**: TLS 1.3, OIDC/MFA federation via Academic Identity Providers, Content Security Policy (CSP)

## Rationale
- The architecture uses decoupled microservices and an optimized SPA container to guarantee rapid circulation workflows and low-latency search (<800ms).
- Security controls, backend audit trails, and EU-hosted infrastructure ensure strict regulatory compliance and data residency requirements.