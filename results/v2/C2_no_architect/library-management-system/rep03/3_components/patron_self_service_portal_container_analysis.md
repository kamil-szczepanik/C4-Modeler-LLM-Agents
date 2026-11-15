## Overview
The Library Management System provides public and academic libraries with item cataloguing, circulation management, and self-service portals. The architecture enforces strict EU-only data residency and sub-800ms search response times.

## Key Elements
- Library Patrons, Library Staff, Library Administrators
- External Identity Provider (IdP)
- EU Cloud Infrastructure Boundary
- In-Region APM and Log Aggregation Pipeline
- Audit and Compliance Trust Zone
- API Gateway Container (Kubernetes, OAuth2/OIDC, TLS 1.3)
- Patron Self-Service Portal Container (Kubernetes, Web Frontend)
- Staff Circulation & Cataloguing Container (Kubernetes, Microservice)
- Admin & Reporting Container (Kubernetes, Microservice)
- Notification Service Container (Kubernetes, Microservice)

## Relationships
- API Gateway Container -> Patron Self-Service Portal Container: Routes patron requests [mTLS over internal Kubernetes network policies]
- Patron Self-Service Portal Container -> In-Region APM and Log Aggregation Pipeline: Streams encrypted metrics via OpenTelemetry sidecars [OpenTelemetry]

## Technology Stack
- Kubernetes: Orchestrates containers with Horizontal Pod Autoscalers (HPA) for dynamic scaling and rolling updates
- OAuth2/OIDC: Manages authentication via External Identity Provider (IdP)
- TLS 1.3 & mTLS: Encrypts communications externally and across internal Kubernetes network policies
- OpenTelemetry: Handles distributed tracing and metrics streaming with PII scrubbing
- HTTP-only, Secure, SameSite=Strict Cookies: Stores session tokens securely at the BFF layer

## Rationale
This containerized architecture meets strict EU data residency laws and GDPR compliance while using Kubernetes auto-scaling, CDNs, and BFF input validation to guarantee sub-800ms search responses and secure patron self-service workflows.