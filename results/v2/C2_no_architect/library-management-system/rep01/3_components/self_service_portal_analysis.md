## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures EU-only data residency and sub-second search performance.

## Key Elements
- Users: Library Patrons, Librarians / Circulation Staff, Library Administrators
- Containers: Self-Service Portal (Public Trust Zone / DMZ), API Gateway, Search Container (Elasticsearch / OpenSearch), Audit & Compliance Container, Centralized Logging & SIEM Service
- Infrastructure: EU-backed Kubernetes clusters (Frankfurt/Dublin), geo-fenced CDN edge caching

## Relationships
- Library Patrons, Librarians, Library Administrators -> Self-Service Portal: Interact with portal [HTTPS / TLS 1.3]
- Self-Service Portal -> API Gateway: Routes requests [mTLS via SPIFFE/SPIRE]

## Technology Stack
- Authentication & Security: OAuth2/OIDC with PKCE, httpOnly/secure/SameSite=Strict cookies, CSP headers, WCAG 2.1 AA accessibility standards
- Observability & Testing: OpenTelemetry for real-user monitoring, axe-core for automated accessibility regression testing in CI/CD, Centralized Logging & SIEM

## Rationale
This architecture uses EU-backed Kubernetes clusters, strict OIDC session handling, and geo-fenced CDNs to satisfy regional data residency and GDPR compliance. Edge rate-limiting and client-side error boundaries protect against DDoS threats and upstream outages while meeting performance targets.