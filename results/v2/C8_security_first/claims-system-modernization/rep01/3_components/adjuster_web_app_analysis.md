## Overview
[The Adjuster Web App is a modern React Single Page Application hosted on Azure Static Web Apps that empowers claims adjusters to efficiently process claims while bridging slow legacy mainframe responses.]

## Key Elements
- Claim Workspace Shell (React, TypeScript)
- BFF Proxy Layer (Azure Static Web Apps Managed Functions)
- Optimized Claim View & Form Engine (React, Formik, Zod)
- Local Draft Cache (IndexedDB, Dexie.js, Web Crypto API)
- Telemetry & RUM Collector (OpenTelemetry, App Insights JS SDK)
- Mainframe Latency Handler (React Hooks, RxJS)

## Relationships
- Claim Workspace Shell -> BFF Proxy Layer: Fetches claims [HTTPS / REST]
- Optimized Claim View -> Local Draft Cache: Auto-saves drafts [IndexedDB]
- Claim Workspace Shell -> Telemetry Collector: Reports performance metrics [OpenTelemetry SDK]
- Optimized Claim View -> Mainframe Latency Handler: Manages async status states [React State / RxJS]

## Technology Stack
- React / TypeScript: Modern UI framework for high-performance frontend components
- Azure Static Web Apps: Serverless hosting with built-in CI/CD and managed functions for BFF
- IndexedDB via Dexie.js: Client-side storage for offline resilience and draft caching
- Web Crypto API: Client-side encryption for sensitive PII and draft data at rest
- OpenTelemetry & App Insights: Real User Monitoring (RUM) to track sub-2s performance requirements

## Rationale
[The component architecture ensures sub-2-second perceived performance against slow legacy backends through optimistic UI updates, local caching, and asynchronous processing. It maintains enterprise security standards by isolating OIDC tokens within a Backend-for-Frontend (BFF) pattern and encrypting sensitive drafts on client devices.]