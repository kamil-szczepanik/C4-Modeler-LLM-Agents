## Overview
A modern cloud-based web application container provides online claim submission and adjuster management for an insurance claims modernization initiative. It replaces a legacy mainframe frontend while maintaining strict security and performance SLAs.

## Key Elements
- **Public Portal UI (React):** Handles customer and broker claim submissions.
- **Internal Workspace UI (React):** Manages adjuster workflows and multi-client broker dashboards.
- **Authentication Interceptor (TypeScript/MSAL.js):** Handles OIDC/OAuth2 integration with Active Directory.
- **BFF Client SDK (TypeScript):** Encapsulates API requests to backend services.
- **Optimistic State Manager (React/Zustand):** Manages local state mutations and IndexedDB storage.

## Relationships
- **Adjuster Workspace UI** -> **BFF Client SDK:** Invokes claims operations [HTTPS/REST]
- **Customer Portal UI** -> **BFF Client SDK:** Submits new claims [HTTPS/REST]
- **Authentication Interceptor** -> **Insurer Active Directory:** Validates tokens [OIDC/HTTPS]
- **Optimistic State Manager** -> **BFF Client SDK:** Synchronizes background requests [HTTPS/REST]

## Technology Stack
- **Azure Static Web Apps:** Hosts separate public and internal frontends for trust boundary isolation.
- **React & Zustand:** Powers component UI rendering and local state management.
- **Web Crypto API (AES-GCM):** Encrypts sensitive PII at rest in browser IndexedDB.
- **W3C Trace Context & OpenTelemetry:** Enables distributed tracing and real user monitoring (RUM).

## Rationale
Separating the public and internal frontends minimizes the attack surface and protects sensitive adjuster tools. Client-side optimistic UI updates and local encryption ensure sub-2s performance and secure offline resilience despite slow legacy mainframe dependencies.