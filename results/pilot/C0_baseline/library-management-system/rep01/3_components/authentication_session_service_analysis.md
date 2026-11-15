## Overview
The Authentication & Session Service manages user authentication, role-based access control, and session validation for the Library Management System. It ensures secure, EU-compliant access for academic patrons via institutional single sign-on and for public users via local credentials.

## Key Elements
*   **Authentication & Session Service (Node.js)**: Core container managing user identity and security.
*   **OIDC/SAML Federation Adapter**: Component using Passport.js for institutional SSO.
*   **Local Credential Verifier**: Component using Argon2id for public patron passwords.
*   **Session Manager**: Component using Redis for token state validation and session handling.
*   **RBAC Authorization Engine**: Component using Casbin for fine-grained permission enforcement.
*   **Institutional SSO Providers**: External identity providers.

## Relationships
*   **OIDC/SAML Federation Adapter -> Institutional SSO Providers**: Authenticates via HTTPS using SAML 2.0 and OIDC.
*   **Core Circulation & Catalog Service -> Session Manager**: Validates sessions via gRPC over TLS with mTLS.
*   **Mobile API Gateway -> Session Manager**: Queries session state via gRPC over TLS.

## Technology Stack
*   **Node.js**: Chosen as the runtime for high-throughput asynchronous request handling.
*   **Passport.js**: Utilized for standardizing OIDC and SAML 2.0 federation protocols.
*   **Argon2id**: Selected for secure password hashing with strict work factors.
*   **Redis**: Deployed as an EU-localized cache tier for low-latency session validation.
*   **Casbin**: Embedded as the policy framework for sub-millisecond RBAC evaluation.
*   **gRPC over TLS**: Implemented for zero-trust, high-performance internal service communication.

## Rationale
This architecture guarantees strict EU data residency by localizing session storage and federation to EU infrastructure. It balances high-performance security through gRPC and Redis with flexible access methods for diverse academic and public library users.