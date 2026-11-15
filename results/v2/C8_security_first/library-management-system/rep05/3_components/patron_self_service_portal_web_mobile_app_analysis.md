## Overview
[The Patron Self-Service Portal provides 24/7 web and mobile access for library patrons to catalogue search, manage loans, and access digital library cards while enforcing EU data residency. It is engineered to deliver high-performance search responses under 800ms while maintaining strict client-side security.]

## Key Elements
- SPA/Mobile Client Router & UI Layer (React / React Native)
- Authentication Client (OAuth 2.0/OIDC SDK with PKCE, biometric bridge)
- API Client Gateway (TypeScript/Axios with gRPC-web mapping)
- Local Secure Storage & Sync Manager (Encrypted SQLite / IndexedDB)
- External: EU-bound API Gateway, CDN Edge Nodes, Notification Engine

## Relationships
- SPA/Mobile Client uses Authentication Client for OIDC flows [HTTPS]
- SPA/Mobile Client uses API Client Gateway for data retrieval [gRPC, mTLS]
- SPA/Mobile Client uses Local Secure Storage & Sync Manager for offline digital card rendering [Local Encryption]
- API Client Gateway communicates with EU-bound API Gateway [gRPC-Web/HTTPS, mTLS (TLS 1.3)]

## Technology Stack
- React & React Native: Powers cross-platform web and mobile interfaces supporting WCAG 2.1 AA accessibility.
- OAuth 2.0 / OIDC with PKCE & Hardware Enclave: Secures authentication and token handling in volatile memory.
- Encrypted SQLite / IndexedDB: Provides secure local caching for offline cryptographic library cards.
- TypeScript / Axios & gRPC-web: Manages type-safe communication and low-latency API transit.
- Global CDN (EU-restricted): Enforces data residency and rapid static asset delivery.

## Rationale
[This component architecture isolates security and offline sync capabilities while meeting performance targets through optimized gRPC transit and CDN caching. It strictly adheres to EU data residency and accessibility mandates without compromising user experience.]