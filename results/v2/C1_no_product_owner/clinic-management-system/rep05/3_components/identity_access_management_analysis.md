## Overview
The Clinic Management System is a hybrid cloud clinical IT platform providing patient management, scheduling, EMR, and billing while ensuring HIPAA and GDPR compliance. It delivers high-availability (99.99%) medical workflows across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Authentication Engine**: Keycloak Auth SPI managing MFA, credentials, and IdP federation.
- **Token Service**: Keycloak Token Endpoint issuing short-lived signed JWTs with OIDC Backchannel Logout.
- **Authorization & RBAC Provider**: Keycloak Authorization Services evaluating clinical roles.
- **Session & User Store Cache**: Embedded Infinispan with cross-site replication and JDBC-PING.
- **Audit Event Dispatcher**: Keycloak Event Listener SPI streaming masked security events.
- **External Systems**: Identity Provider (IdP), SIEM & Audit Platform, Enterprise KMS, API Gateway, Core Services.

## Relationships
- *Authentication Engine* -> *Identity Provider (IdP)*: Federates authentication via OIDC/SAML
- *Core Services* -> *Authorization & RBAC Provider*: Verifies permissions via gRPC over mTLS
- *Audit Event Dispatcher* -> *SIEM & Audit Platform*: Streams audit trails via Syslog over TLS / Kafka
- *Token Service* -> *API Gateway & Core Services*: Validates short-lived JWTs via OAuth2/OIDC

## Technology Stack
- **Keycloak & SPI**: Core IAM platform for extensible auth, token issuance, and event auditing.
- **Infinispan**: Distributed caching for cross-site session replication in hybrid infrastructure.
- **Kafka / Syslog over TLS**: Resilient asynchronous messaging for secure audit event streaming.
- **Enterprise KMS**: Envelope encryption for master keys, session data, and token signing.
- **gRPC over mTLS**: Secure, performant internal inter-component communication.

## Rationale
This architecture achieves 99.99% uptime via active-active hybrid deployments with Infinispan caching and circuit breakers. It strictly enforces HIPAA/GDPR compliance through mTLS, AES-256 encryption, PHI audit sanitization, and FIDO2/WebAuthn multi-factor authentication.