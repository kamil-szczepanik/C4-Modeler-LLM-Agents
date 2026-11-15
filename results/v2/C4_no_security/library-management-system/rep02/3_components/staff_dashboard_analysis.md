## Overview
The Staff Dashboard is an Angular-based internal Single Page Application providing high-efficiency circulation and cataloging operations for library staff. It ensures secure, high-performance interactions with core library backend services while maintaining strict compliance with EU data residency regulations.

## Key Elements
- Staff Dashboard (Angular SPA): Primary frontend container for library staff operations
- Circulation Management Module: Handles high-speed check-ins, check-outs, and patron lookups via reactive forms
- Cataloging & Inventory Module: Manages physical and digital item inventories with bulk-editing and validation checks (R-01)
- API Client Service: Encapsulates HTTP communication, JWT management, error boundaries, and interceptors
- Security & Session Manager: Enforces auto-lockouts, rapid re-authentication, and encrypted local storage
- Telemetry Service: Captures Real User Monitoring (RUM) metrics using the OpenTelemetry browser SDK

## Relationships
- Circulation Management Module & Cataloging Module -> Security & Session Manager [TypeScript / Direct Method Calls]
- Circulation Management & Cataloging Modules -> API Client Service [TypeScript / Direct Method Calls]
- API Client Service -> API Gateway [HTTPS / REST / mTLS]
- API Client Service -> Telemetry Service [OpenTelemetry SDK / HTTPS]

## Technology Stack
- Angular: Modular SPA framework chosen for robust reactive form handling and data-dense UI capabilities
- TypeScript: Strongly typed language ensuring maintainability and minimizing operational input errors
- RxJS: Reactive state management for handling high-volume circulation workflows without blocking the UI thread
- OpenTelemetry Browser SDK: Captures client-side RUM metrics to monitor the <800ms search NFR
- TLS 1.3 & CSP Headers: Enforced at the CDN edge for secure, encrypted transit and XSS mitigation

## Rationale
This component architecture optimizes front-desk task-switching latency to meet strict search performance requirements while implementing robust security and session controls for shared terminals. The modular design isolates circulation, cataloging, and telemetry concerns, ensuring operational resilience and EU compliance.