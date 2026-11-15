## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The architecture utilizes an edge API gateway to secure, prioritize, and route traffic to internal containerized services.

## Key Elements
- **Users**: Library Patrons, Library Staff/Cataloguers, Library Administrators
- **Edge Component**: API Gateway / Ingress (Envoy Proxy)
- **Downstream Containers**: Patron BFF Container, Staff Workflow Container, Catalogue & Search Service Container, Circulation & Loan Service Container, Notification Dispatcher Container
- **Data Stores**: PostgreSQL, Redis

## Relationships
- Library Patrons, Library Staff/Cataloguers, Library Administrators -> API Gateway / Ingress [HTTPS / REST / JSON]
- API Gateway / Ingress -> Patron BFF Container [mTLS / HTTP/2]
- API Gateway / Ingress -> Staff Workflow Container [mTLS / HTTP/2]
- API Gateway / Ingress -> Catalogue & Search Service Container [mTLS / gRPC]

## Technology Stack
- **API Gateway**: Envoy Proxy deployed via Kubernetes Ingress Controller for native mTLS, WAF, JWT validation, and tiered rate-limiting.
- **Internal Protocols**: mTLS over HTTP/2 and gRPC to ensure secure, low-latency zero-trust communication.
- **Observability**: Prometheus scraping and OpenTelemetry for distributed tracing and audit logging.

## Rationale
Envoy provides robust native support for advanced mTLS, distributed tracing, and Lua/WASM-based rate-limiting required for EU data compliance. Direct gRPC routing through the gateway ensures 99th-percentile search responses remain under the required 800ms threshold.