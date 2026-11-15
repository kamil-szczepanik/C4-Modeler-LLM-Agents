## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It guarantees sub-800ms search performance while enforcing strict EU-only data residency.

## Key Elements
* Library Patrons, Library Staff, Library Administrators
* API Gateway Container
* Patron Self-Service Portal Container
* Staff Circulation & Cataloguing Container
* Admin & Reporting Container
* Notification Service Container
* External Identity Provider (IdP)
* EU Cloud Infrastructure Boundary
* In-Region APM and Log Aggregation Pipeline
* Audit and Compliance Trust Zone

## Relationships
* Library Patrons and Staff communicate via HTTPS (TLS 1.3) to the API Gateway Container.
* API Gateway Container validates OAuth2/OIDC tokens via External Identity Provider (IdP).
* Inter-container communication uses mTLS over internal Kubernetes network policies.
* OpenTelemetry sidecars stream encrypted metrics to the In-Region APM and Log Aggregation Pipeline.

## Technology Stack
* Kubernetes: Deploys all containers with strict node affinity rules for EU-only data residency.
* OAuth2/OIDC: Secures ingress authentication and user session management.
* TLS 1.3 and mTLS: Encrypts external traffic and zero-trust inter-container communication.
* AES-256: Enforces data-at-rest encryption across all persistent volumes.
* OpenTelemetry: Powers distributed tracing to track 99th-percentile search latencies.

## Rationale
The containerized microservices architecture isolates sensitive administrative functions and scales user-facing portals to meet performance SLAs. Strict regional deployment and encryption natively satisfy EU data residency and privacy mandates.