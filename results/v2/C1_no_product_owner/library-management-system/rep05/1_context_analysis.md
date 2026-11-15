## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and sub-800ms 99th-percentile search performance.

## Key Elements
- **Library Management System**: Core software system handling cataloging, circulation, search, and self-service.
- **Patron**: End-user interacting via self-service portals.
- **Librarian / Staff**: Internal users managing inventory and circulation desk operations.
- **Authentication Provider**: External SaaS/IDP managing OIDC/OAuth2 federation, MFA for staff, and cryptographically signed JWTs.
- **External Payment Gateway**: Handles fines and fees processing via tokenization and secure iframes.
- **National Library Registry**: External authority for ISBN and metadata syncing with local fallback mechanisms.
- **Notification Service**: Manages transactional emails and SMS via REST/HTTPS.

## Relationships
- **Patron** and **Librarian** use **Library Management System** via HTTPS for portals and cataloging.
- **Library Management System** integrates with **Authentication Provider** via OIDC/HTTPS for identity federation.
- **Library Management System** integrates with **External Payment Gateway** and **Notification Service** via REST/HTTPS with mTLS and TLS 1.3.
- **Library Management System** synchronizes with **National Library Registry** with local fallback capabilities.

## Technology Stack
- **EU Cloud Infrastructure**: Deployed exclusively in EU regions (Frankfurt/Ireland) with strict IaC region-locking.
- **Caching & Search**: Distributed Redis caching and internal search index to satisfy <800ms search SLA (R-05) with read-replicas.
- **Security & Encryption**: AES-256 for data at rest, mTLS and TLS 1.3 for data in transit, HMAC-SHA256 for webhook verification, and stateless JWT validation.
- **Observability & Privacy**: Centralized logging with automated PII/GDPR scrubbing and distributed tracing.

## Rationale
This architecture ensures strict compliance with EU-only data residency and privacy mandates while maintaining robust fault-tolerance against external system failures. Furthermore, stateless token validation and distributed caching guarantee that performance requirements (R-05) are met during peak academic traffic.