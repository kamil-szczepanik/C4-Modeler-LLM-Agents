## Overview
The Staff Management Console is a secure web administrative interface for the Library Management System, enabling staff to catalogue items, manage circulation, and oversee operations. It enforces strict EU-only data residency while maintaining low-latency performance for critical workflows.

## Key Elements
* **Console Router / UI Shell**: TypeScript / React Single Page Application with TanStack Query state management and 15-minute inactivity timeout.
* **Auth & RBAC Client**: Manages OIDC/OAuth2 authentication, MFA, and role-based access control for Librarians and Administrators.
* **Catalogue & Inventory Controller**: TypeScript BFF microservice handling item management and schema validation via Zod.
* **Circulation Desk Interface**: TypeScript BFF microservice optimized for low-latency check-outs and graceful degradation.
* **EU-bound API Gateway**: Routes traffic and validates short-lived JWTs.
* **Search & Catalogue Service & Circulation & Loan Engine**: Backend core services.

## Relationships
* EU-bound API Gateway -> Staff Management Console: Routes traffic [REST/HTTPS]
* Console Router -> Auth & RBAC Client: Verifies permissions [In-memory]
* Console Router -> Catalogue & Inventory Controller / Circulation Desk Interface: Communicates [HTTP/JSON over HTTPS]
* Catalogue & Inventory Controller -> Search & Catalogue Service: Communicates internally [gRPC, mTLS (TLS 1.3)]
* Circulation Desk Interface -> Circulation & Loan Engine: Communicates internally [gRPC, mTLS (TLS 1.3)]

## Technology Stack
* **TypeScript / React**: Powers the frontend UI shell for rapid dashboard rendering and role-based adaptability.
* **Node.js / TypeScript BFFs**: Isolates the SPA from gRPC complexity, enforcing Zod validation and HTTP-only cookie token storage.
* **gRPC with mTLS (TLS 1.3)**: Ensures secure, high-performance internal communication between BFFs and backend engines.
* **Kubernetes (EU-hosted) & Edge CDN**: Guarantees strict EU-only data residency and zero-downtime canary deployments via Istio.
* **Redis**: Provides distributed rate limiting and response caching to absorb peak traffic.

## Rationale
The BFF pattern and gRPC protocols secure administrative boundaries while isolating core check-outs to meet sub-800ms performance SLAs. Containerized EU deployment and robust audit logging satisfy regional compliance and data residency constraints.