## Overview
[The Staff Management Console is a React-based SPA serving library staff and administrators to manage cataloging and circulation workflows securely and efficiently.]

## Key Elements
- Staff Management Console (React/Nginx Container)
- Dashboard Router & State Manager (React Router / Redux Toolkit)
- Cataloguing & Circulation Module (React Components)
- Audit Action Interceptor (TypeScript Axios Middleware)
- Search Query Client (TanStack React Query)
- Auth & Session Guardian Module (React Context / Axios Interceptor)
- Bulk Operations Orchestrator (React State Machine)
- API Gateway (Kong/Envoy), Search Engine (ElasticSearch), EU Identity Provider

## Relationships
- Librarians/Administrators -> Staff Management Console: Accesses UI via HTTPS
- Staff Management Console -> API Gateway: Routes requests using HTTPS/REST
- Auth & Session Guardian -> API Gateway: Performs silent token refresh via HTTPS/REST
- Cataloguing Module -> API Gateway: Streams batched payloads using HTTPS/REST

## Technology Stack
- React & TypeScript: Component-level architecture for type safety and maintainability
- Nginx: High-performance web server container with container hardening
- TanStack React Query: Optimizes search rendering to meet the <800ms performance target
- HttpOnly, SameSite=Strict Cookies: Secure token storage preventing XSS and CSRF

## Rationale
[This architecture enforces strict EU data residency and security standards while providing high-performance search and bulk workflows. It ensures operational efficiency for library staff without compromising compliance or data integrity.]