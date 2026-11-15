## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The frontend architecture delivers a secure, accessible, and high-performance single-page application for patrons and staff.

## Key Elements
- Library Patrons (Students, Public)
- Librarians / Circulation Staff
- Library Administrators
- Frontend Container (React/TypeScript SPA served via CDN)
- Routing & View Layer (React Router)
- State & Offline Manager (Zustand + IndexedDB)
- API Communication Layer (Axios with interceptors and Zod validation)
- Design System & i18n Component (Tailwind CSS / Radix UI + i18next)
- API Gateway (Nginx/Kong)
- EU Identity Provider (IdP)

## Relationships
- Library Patrons -> Frontend Container: Accesses self-service portals [HTTPS]
- Librarians / Circulation Staff -> Frontend Container: Accesses staff portal and circulation tools [HTTPS]
- Library Administrators -> Frontend Container: Accesses administrative portal [HTTPS]
- Frontend Container -> API Gateway: Forwards REST API calls [HTTPS]
- Frontend Container -> EU Identity Provider: Manages authentication flows and token exchange [HTTPS]

## Technology Stack
- React / TypeScript: Powers the interactive single-page application for client-side rendering.
- React Router: Manages client-side navigation and role-based UI hydration.
- Zustand + IndexedDB: Handles volatile session state and offline-resilient non-PII digital catalog caching.
- Tailwind CSS / Radix UI: Enforces WCAG 2.1 AA accessibility, responsive design, and municipal white-labeling.
- i18next: Supports multi-language localization across regional EU jurisdictions.
- Zod: Provides strict runtime input validation mirrored from backend expectations.

## Rationale
This architecture ensures strict EU data residency and privacy compliance by prohibiting local storage of PII and tokens. The component breakdown guarantees WCAG 2.1 AA accessibility and sub-800ms search performance while maintaining robust security against XSS.