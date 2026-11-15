## Overview
The Library Management System provides cataloguing, circulation, and self-service portals for public and academic libraries. It strictly adheres to EU-only data residency constraints for GDPR compliance while maintaining high-performance search capabilities.

## Key Elements
- **Library Patrons (Members):** Access self-service portals to search catalogues and manage loans.
- **Librarians / Library Staff:** Utilize circulation and cataloguing tools (R-01) for inventory management.
- **Library Administrators:** Handle reporting and user management.
- **Inter-Library Loan (ILL) Partners:** External library systems for resource sharing.
- **Payment Gateways & Notification Services:** External SaaS for processing fines and alerts.
- **Library Management System (Core):** Central processing unit for core business logic.

## Relationships
- Patrons, Staff, and Admins interact via HTTPS with **TLS 1.3**.
- Core system integrates with ILL Partners via **NCIP/ISO 18626 APIs** using **mTLS**.
- External SaaS integrations communicate via secure webhooks protected by **mTLS**.

## Technology Stack
- **Search & Caching:** Elasticsearch or Redis to ensure 99th-percentile search response times under 800 ms (R-05).
- **Security & IAM:** OAuth 2.0 / OpenID Connect (OIDC) with Multi-Factor Authentication (MFA) and Role-Based Access Control (RBAC).
- **Encryption:** AES-256 for data at rest.
- **Integration Patterns:** Asynchronous message queues and webhooks for ILL partners.

## Rationale
This architecture ensures strict compliance with EU-only data residency and GDPR mandates through isolated trust boundaries and encrypted data handling. Concurrently, it delivers high-performance search capabilities and fault-tolerant third-party integrations to support reliable library operations.