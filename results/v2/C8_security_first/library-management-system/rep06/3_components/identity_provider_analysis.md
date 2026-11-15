## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Identity Provider ensures secure, EU-compliant authentication and authorization.

## Key Elements
- **Identity Provider (Keycloak / Java/Quarkus)**: Core container managing authentication, authorization, and sessions.
- **Authentication Engine**: Handles OIDC/OAuth2 protocols and PKCE.
- **User Management & RBAC Service**: Manages profiles and maps roles to JWT claims.
- **Session & Token Management Service**: Manages active user sessions and token revocation.
- **Adaptive MFA & Policy Engine**: Evaluates risk signals for step-up authentication.
- **Federation & JIT Provisioning Component**: Manages external IdPs (Google, Shibboleth SAML).
- **UI & Localization Component**: Renders multi-language login and consent pages.
- **HashiCorp Vault**: Stores cryptographic key material.
- **PostgreSQL Database**: Persists identity state.

## Relationships
- Patron Portal / Librarian Dashboard to Authentication Engine via HTTPS (OIDC Authorization Code Flow with PKCE)
- Session & Token Management Service to HashiCorp Vault via HTTPS/REST (Transit Secrets Engine)
- Identity Provider containers to PostgreSQL Database via JDBC (TLS)
- Inter-node session replication via Infinispan (ENCRYPT_TCP)

## Technology Stack
- **Keycloak (Java/Quarkus)**: Chosen for robust OIDC support, extensibility, and enterprise federation features.
- **HashiCorp Vault**: Selected for secure, centralized cryptographic key management and rotation.
- **Infinispan**: Used for distributed session clustering and replication across Keycloak replicas.
- **PostgreSQL**: Chosen for reliable, ACID-compliant relational data storage within the EU boundary.
- **OAuth 2.0 / OIDC / SAML 2.0**: Protocols enforcing open standards for federation and token exchange.

## Rationale
This architecture ensures strict EU data residency and low-latency token validation by keeping all identity services and data strictly localized. Clustered Keycloak containers with Infinispan provide high availability and fault tolerance for user sessions.