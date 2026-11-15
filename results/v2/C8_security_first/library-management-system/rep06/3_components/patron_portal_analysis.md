## Overview
The Patron Portal is a secure self-service web interface enabling library patrons to catalogue items, manage accounts, and handle circulation tasks. It ensures high performance and strictly adheres to EU-only data residency requirements.

## Key Elements
*   Library Patrons (Users)
*   Patron Portal Container (Next.js)
*   UI Presentation Layer (React / Tailwind CSS)
*   BFF / Route Handler Layer (Next.js Node.js runtime)
*   API Gateway (Kong / Envoy)
*   EU Payment Gateway
*   EU-region CDN & Kubernetes Cluster

## Relationships
*   Library Patrons -> Patron Portal: Accesses self-service features [HTTPS / TLS 1.3]
*   UI Presentation Layer -> BFF Layer: Internal React Server Actions [Direct IPC]
*   BFF Layer -> API Gateway: Proxied requests with injected OIDC tokens [HTTPS / TLS 1.3]
*   API Gateway -> EU Payment Gateway: Processes fine payments [HTTPS]
*   EU CDN -> Patron Portal Container: Serves cached static assets and edge traffic [HTTPS]

## Technology Stack
*   Next.js (React/Tailwind CSS): Powers server-rendered UI and BFF components for performance and WCAG 2.1 AA accessibility.
*   OAuth 2.0 / OIDC: Manages secure authentication with tokens stored exclusively in BFF server memory.
*   Kubernetes & EU CDN: Deploys container workloads locally to enforce EU data residency and <800ms search SLAs.
*   TLS 1.3: Secures all data in transit across system boundaries.

## Rationale
This architecture uses a Backend-for-Frontend (BFF) pattern to isolate sensitive session tokens and enforce strict security controls without degrading user experience. Deploying within an EU-region container cluster and CDN guarantees compliance with regional data residency constraints while meeting high-performance response SLAs.