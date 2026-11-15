## Overview
The Library Management System provides self-service portals and circulation management for public and academic libraries. The architecture prioritizes EU data residency and sub-800ms search performance.

## Key Elements
- Library Patrons and Library Staff
- Patron Web/Mobile App (React / React Native container)
- API Gateway (Kong / Nginx)
- Authentication & Session Manager component (OAuth2/OIDC)
- Catalogue Search UI component
- Loan & Account Manager component
- Payment & Fines Module component
- Onboarding & Feature Flag Manager component

## Relationships
- Library Patrons -> Patron Web/Mobile App: Accesses application via secure channels [HTTPS / mTLS]
- Patron Web/Mobile App -> API Gateway: Routes requests and data [HTTPS / REST, WebSockets]
- Payment & Fines Module -> EU Payment Gateway: Processes financial transactions [HTTPS]
- Patron Web/Mobile App components -> EU-Resident Log & Audit Sink: Sends telemetry and error data [HTTPS]

## Technology Stack
- React / React Native: Powers the cross-platform frontend prioritizing WCAG 2.1 AA accessibility.
- IndexedDB / AsyncStorage: Provides local state persistence for offline resilience.
- OpenTelemetry RUM SDK: Captures client-side rendering metrics to track the <800ms search requirement (R-05).
- Expo EAS: Enables Over-The-Air (OTA) mobile updates.
- axe-core: Integrates automated accessibility regression testing into the CI/CD pipeline.

## Rationale
The React/React Native stack with local caching ensures sub-800ms search performance and offline resilience for mobile users. Component decomposition and strict EU-hosted endpoints guarantee full compliance with EU data residency requirements.