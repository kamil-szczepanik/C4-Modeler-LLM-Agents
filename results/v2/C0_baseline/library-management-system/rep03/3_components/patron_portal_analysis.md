## Overview
- Patron Portal for the Library Management System providing self-service search, account management, and digital content access.
- Enables public and academic library patrons to autonomously manage accounts and discover items with EU-only data residency.

## Key Elements
- Search & Discovery Component (React / TypeScript)
- Account & Fines Component (React / TypeScript)
- Digital Content Reader Component (React / TypeScript)
- Accessibility & Localization Layer (React Context)
- API Client Service (Axios / TypeScript with RUM telemetry)
- Health Check & Feature Flag Service (React / TypeScript)
- CDN Deployment (AWS S3 + CloudFront)

## Relationships
- Library Patrons -> Patron Portal: Interacts via web browser [HTTPS (TLS 1.3)]
- Patron Portal -> API Gateway: Sends API requests and receives HTTP-only cookies [HTTPS (TLS 1.3)]
- API Client Service -> Centralized Observability & SIEM Platform: Sends scrubbed performance and error metrics [HTTPS (TLS 1.3)]
- Health Check & Feature Flag Service -> API Gateway: Polls lightweight dependency status endpoints [HTTPS (TLS 1.3)]

## Technology Stack
- React / TypeScript SPA: Chosen for responsive, modern client-side self-service user experiences.
- Axios / TypeScript: Centralizes communication, error handling, and RUM telemetry integration.
- AWS S3 + CloudFront: Delivers static assets globally with strict cache-control and automated invalidation.
- HTTP-only Secure SameSite=Strict Cookies: Managed via API Gateway to prevent token theft and XSS vulnerabilities.
- WCAG 2.1 AA Compliance: Implemented via React Context to meet universal public and academic accessibility mandates.

## Rationale
- This architecture guarantees high-performance client-side rendering supporting sub-800ms search requirements while maintaining strict EU data residency. 
- Centralized security patterns and robust observability ensure patron privacy, regulatory compliance, and seamless operational reliability.