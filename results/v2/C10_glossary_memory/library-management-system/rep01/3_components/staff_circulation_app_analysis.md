## Overview
The Staff Circulation App is a secure web and mobile container that empowers librarians to manage patron checkouts, returns, and catalog lookups while enforcing strict EU data residency. It integrates tightly with core backend services and identity providers to deliver rapid, low-latency circulation workflows at library front desks.

## Key Elements
- Librarian / Staff
- Staff Circulation App (Web/Mobile Container)
- Circulation Dashboard Component
- Patron Lookup & Verification Component
- Loan Management UI Component
- Fine-Grained Override Management Feature
- Authentication & Session Manager
- Offline Sync & Caching Service
- Audit & Telemetry Dispatcher
- API Gateway / BFF
- EU Identity Provider (IdP)
- EU Monitoring & APM Provider
- EU Compliance & Audit Logging Service

## Relationships
- Librarian / Staff -> Anycast CDN / DDoS Protection Service (EU-PoPs) via TLS 1.3, HTTPS
- Staff Circulation App -> API Gateway / BFF via HTTPS/REST
- Authentication & Session Manager -> EU Identity Provider (IdP) via OIDC/OAuth2
- Audit & Telemetry Dispatcher -> API Gateway / BFF via HTTPS/REST
- Patron Lookup & Verification Component -> Offline Sync & Caching Service via Encrypted local storage read/write (AES-GCM)

## Technology Stack
- React SPA / TypeScript: Chosen for building a responsive, modular single-page application for circulation staff.
- IndexedDB & Web Crypto API: Used for secure, encrypted offline-tolerant caching of patron PII and records.
- OIDC/OAuth2: Enforces secure multi-factor authentication and token-based session management via the EU Identity Provider (IdP).
- TLS 1.3: Mandated for all transport security and API communications to protect sensitive user data.

## Rationale
This architecture ensures high-performance circulation workflows capable of handling rapid counter transactions and network partitions without violating EU data privacy mandates. Strong client-side encryption and rigorous backend token validation mitigate security risks inherent in mobile or shared library hardware.