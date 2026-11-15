## Overview
The Library Management System provides self-service portals and catalogue/circulation management for academic and public libraries. It strictly enforces EU-only data residency while delivering high-performance cataloguing and search capabilities.

## Key Elements
* **Library Patrons:** Students and public users accessing the system via self-service portals.
* **Librarians / Circulation Staff:** Personnel managing inventory, loans, and daily operations.
* **Library Administrators:** Users overseeing reporting and user management.
* **Web App / Mobile App (SPA/PWA):** React-based frontend served via an EU CDN.
* **API Gateway:** Reverse proxy handling routing and OAuth2 token validation.
* **Core Domain Services:** Catalog & Search Service and Circulation & Patron Service.
* **PostgreSQL & Elasticsearch:** EU-hosted transactional database and search engine.
* **External Systems:** Stripe EU, Keycloak/Auth0 EU tenant, and SendGrid EU.

## Relationships
* **Patrons & Staff** interact with the **Web App** via **HTTPS (REST/GraphQL)** over **TLS 1.3**.
* **API Gateway** communicates with **Core Domain Services** using **gRPC/REST** with **mTLS**.
* **Library Management System** integrates with **Stripe EU**, **Keycloak/Auth0 EU**, and **SendGrid EU** via **HTTPS/REST** restricted to EU endpoints.

## Technology Stack
* **Frontend:** TypeScript, React (PWA/SPA) for responsive patron and staff interfaces.
* **Backend:** Java/Spring Boot or Go for high-throughput Core Domain Services.
* **Search:** Elasticsearch (EU hosted) to meet the 99th-percentile search response time under 800 ms.
* **Database:** PostgreSQL (EU hosted) with AES-256 encryption at rest for transactional data and PII.
* **Security:** OAuth 2.0 / OIDC (Keycloak/Auth0 EU) with PKCE and short-lived JWTs.

## Rationale
This architecture guarantees EU-only data residency compliance for all patron PII and financial transactions through regionally hosted infrastructure and services. Additionally, the separation of the Elasticsearch search container ensures strict adherence to the sub-800ms performance requirement.