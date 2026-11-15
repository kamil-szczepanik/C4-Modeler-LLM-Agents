## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system strictly enforces EU data residency and high-performance search capabilities.

## Key Elements
- Library Patrons & Staff
- Web Application (SPA) (React)
- Router Component (React Router)
- State Management & Data Fetching Component (TanStack Query / Zustand)
- UI Component Library (Tailwind CSS / Radix UI)
- UI RBAC & Claims Adapter
- Offline Persistence & Queue Component (IndexedDB / Workbox)
- API Gateway (Nginx / Kong)
- CDN / Edge Layer
- Centralized Observability Platform

## Relationships
- Library Patrons & Staff -> Router Component: Navigates views [HTTPS]
- State Management -> API Gateway: Sends API requests [HTTPS/REST with TLS 1.3]
- State Management -> Offline Persistence Component: Persists drafts and queued mutations [Local IndexedDB]
- UI RBAC & Claims Adapter -> API Gateway: Validates session state via HttpOnly cookies [HTTPS/REST]

## Technology Stack
- React: Powers the frontend SPA for fast patron and staff self-service.
- TanStack Query / Zustand: Handles caching, optimistic UI updates, and data synchronization.
- Tailwind CSS / Radix UI: Ensures accessible, responsive design meeting WCAG 2.1 AA.
- IndexedDB / Workbox: Enables offline persistence and mutation queuing during network drops.
- Web Crypto API: Provides client-side encryption for sensitive data at rest in IndexedDB.
- OpenTelemetry JS: Streams Real User Monitoring (RUM) and error telemetry to the observability platform.

## Rationale
This architecture ensures secure client-side performance and strict EU-only data residency via geo-distributed CDN edge deployment. The use of HttpOnly cookies, idempotency headers, and encrypted offline storage guarantees robust security and operational resilience.