## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within strict EU data residency constraints. The Web Frontend serves as the user-facing interface, communicating securely with downstream microservices via an API Gateway.

## Key Elements
- Web Frontend Container (React, NGINX reverse-proxy)
- Client / User Agent
- API Gateway Container (Envoy / NGINX)
- Identity Provider (IdP)
- Log/Metrics Collector Agent (OTel Collector / Fluentd)

## Relationships
- Client / User Agent -> Web Frontend: Accesses portals and catalog via [HTTPS/REST]
- Web Frontend -> API Gateway Container: Sends frontend requests via [HTTPS/REST]
- Web Frontend -> Identity Provider (IdP): Manages authentication handshakes and session tokens
- Web Frontend -> Log/Metrics Collector Agent: Forwards sanitized UI-level exceptions and telemetry

## Technology Stack
- React / HTML / JavaScript: Core UI framework with component-driven development (Storybook) and custom hooks for data-fetching abstraction.
- NGINX: Runtime reverse-proxy container hosting local static assets, polyfills, and fonts with enforced Content Security Policies.
- Docker: Multi-stage container builds with runtime environment configuration injection.
- Jest and React Testing Library / Playwright or Cypress: Unit, integration, and E2E smoke testing pipelines.
- axe-core: Automated accessibility (a11y) testing for WCAG compliance.

## Rationale
This architecture ensures high-performance sub-800ms search interactions through debounced inputs, client-side caching, and optimistic UI updates while strictly maintaining EU data residency by eliminating external CDNs and third-party telemetry scripts.