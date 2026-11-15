## Overview
The Staff Dashboard is a multi-persona Single Page Application (SPA) providing clinic staff, providers, billers, and administrators with secure access to patient admissions, EMRs, and scheduling. It enforces strict HIPAA and GDPR compliance while maintaining sub-second performance and high availability.

## Key Elements
* Staff Dashboard (SPA): Nginx-hosted frontend using role-based UI composition
* Auth & RBAC Module: Handles JWT evaluation and role-based views
* EMR View Engine: Implements local caching and virtualized rendering for medical records
* Scheduling & Intake Controller: Manages appointment grids and patient registration
* Local Session State Manager: Volatile in-memory storage for unsaved form drafts
* WebSocket Reconnection Manager: Handles network drops and state re-sync
* API Client Layer: Communicates securely with backend systems

## Relationships
* Clinic Staff, Providers, Billing Specialists, System Administrators -> Staff Dashboard (SPA): Manages operations, records, and billing [HTTPS / WebSockets]
* Staff Dashboard (SPA) -> API Gateway (Kong / Envoy): Sends API requests and data syncs [HTTPS / WSS]
* Scheduling & Intake Controller -> Local Session State Manager: Preserves ephemeral drafts [In-Memory RAM]

## Technology Stack
* Nginx: Web server with strict Content Security Policy (CSP) headers for secure SPA delivery
* JavaScript / TypeScript: Frontend language powering component modularity
* WebSockets (WSS): Real-time communication for live scheduling grids
* HTTPS / TLS: Encrypted transport protocol for all API communications

## Rationale
This architecture balances rapid, sub-second EMR performance for clinical safety with stringent server-side security to meet HIPAA and GDPR constraints. Volatile in-memory state management ensures network resilience without violating patient data protection policies.