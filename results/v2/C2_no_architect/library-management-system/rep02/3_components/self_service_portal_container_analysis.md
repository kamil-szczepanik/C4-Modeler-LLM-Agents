## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Patrons
- Self-Service Portal Container (Kubernetes, EU-hosted)
- External Identity Provider (SSO)
- External Payment Gateway
- Notification Container
- Analytics/Reporting Container

## Relationships
- Library Patrons -> Self-Service Portal Container: Accesses self-service portal [HTTPS (TLS 1.3)]
- Self-Service Portal Container -> External Identity Provider: Authenticates patrons [OIDC with PKCE]
- Self-Service Portal Container -> External Payment Gateway: Processes fines [HTTPS]
- Self-Service Portal Container -> Notification Container: Triggers notifications [mTLS (Service Mesh / SPIFFE/SPIRE)]
- Self-Service Portal Container -> Analytics/Reporting Container: Sends usage metrics [mTLS (Service Mesh / SPIFFE/SPIRE)]

## Technology Stack
- Kubernetes: Hosts containerized services with Horizontal Pod Autoscaling for bursty search traffic.
- Envoy: Implements ingress-level rate limiting and DDoS protection.
- OpenTelemetry: Provides distributed tracing across services.
- AES-256: Secures data at rest for local persistent volumes and caches.
- TLS 1.3: Secures inbound patron traffic.

## Rationale
Decoupling search components within Kubernetes ensures sub-800ms search response times under heavy loads. Offloading payment processing to an external gateway minimizes PCI-DSS scope while maintaining strict EU data residency compliance.