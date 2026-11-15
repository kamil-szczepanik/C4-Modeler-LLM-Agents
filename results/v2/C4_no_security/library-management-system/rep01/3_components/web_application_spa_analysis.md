## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures EU-only data residency and meets strict search performance requirements.

## Key Elements
- **Web Application (SPA)**: React / TypeScript frontend
- **Routing & Layout Manager**: React Router client-side routing
- **State Management Store**: Zustand or Redux Toolkit
- **API Client Layer**: Axios-configured HTTP client
- **Feature Modules**: Catalog Discovery, Circulation Desk, and Admin Dashboard components
- **Local Persistence Layer**: IndexedDB via Dexie.js with Web Crypto API encryption
- **API Gateway**: Nginx / Envoy
- **Core Services API**: Node.js / NestJS Modular Monolith

## Relationships
- **Library Patrons, Librarians, Administrators** -> **Web Application (SPA)**: Accesses portals and workflows [HTTPS]
- **Web Application (SPA)** -> **API Gateway**: Sends API requests [HTTPS / JSON]
- **Circulation Desk Component** -> **Local Persistence Layer**: Reads/writes cached transaction queues [IndexedDB]

## Technology Stack
- **React / TypeScript**: Chosen for building a modular, type-safe, and interactive single-page application.
- **IndexedDB & Dexie.js**: Enables robust local persistence for offline circulation resilience.
- **Web Crypto API**: Enforces client-side encryption-at-rest for PII to maintain GDPR compliance.
- **EU-hosted S3-compatible Object Storage**: Hosts static SPA assets to satisfy EU-only data residency constraints.

## Rationale
This architecture uses client-side caching, local persistence, and static asset distribution to achieve sub-800ms search responses and offline resilience for librarians. Furthermore, EU-hosted deployment and client-side encryption strictly enforce regional data residency and GDPR mandates.