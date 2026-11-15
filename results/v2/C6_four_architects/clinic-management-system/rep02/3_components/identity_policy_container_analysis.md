## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance and 99.99% high availability while meeting demanding performance and interoperability standards.

## Key Elements
- **Identity & Policy Container**: Keycloak-based authentication and authorization boundary.
- **Authn Engine**: Built-in Keycloak Authentication SPIs handling MFA and OIDC/OAuth2.
- **Policy Enforcement / RBAC Module**: Evaluates fine-grained roles and user permissions.
- **User Federation Service**: Integrates with external IdPs via LDAP/SAML.
- **Local Token Cache**: Infinispan distributed cache for session synchronization.
- **Audit Logging SPI**: Captures security events for compliance tracking.
- **OAuth2 Token Introspection Module**: Handles token revocation and session termination.
- **API Gateway**: Kong or Envoy routing external traffic.
- **Core Services**: Node.js and NestJS backend for patient, appointment, and billing logic.
- **EMR Service**: Java and Spring Boot service for electronic medical records.
- **Data Layer**: PostgreSQL and MinIO/AWS S3 for data persistence.
- **Message Broker**: Apache Kafka or RabbitMQ for asynchronous event streaming.

## Relationships
- **API Gateway** -> **Authn Engine**: Token validation via local Public Key Cryptography (JWT/JWKS over HTTPS).
- **Policy Enforcement Module** -> **Core Services / EMR Service**: Authorization endpoints via gRPC over mTLS.
- **Audit Logging SPI** -> **Message Broker**: Event publishing via AMQP/Kafka Protocol over TLS.
- **Core Services / EMR Service** -> **OAuth2 Token Introspection Module**: Token validation via gRPC over mTLS.
- **Internal Components** -> **Local Token Cache**: Session synchronization via JGroups over TLS.
- **Authn Engine** -> **Data Layer**: Credential and session persistence via JDBC over TLS.

## Technology Stack
- **Keycloak**: Chosen for enterprise IAM, OIDC/OAuth2 compliance, and extensibility.
- **Infinispan**: Provides sub-millisecond distributed caching for active-active availability (R-06).
- **PostgreSQL & MinIO/S3**: Ensures AES-256 encrypted storage at rest (R-05) with 10+ year data retention.
- **Kafka**: Enables reliable asynchronous event streaming for audit logs and messaging.
- **gRPC over mTLS**: Delivers high-performance, secure internal service-to-service communication.

## Rationale
This architecture uses a hybrid cloud deployment with active-active redundancy to guarantee 99.99% availability and meet stringent HIPAA/GDPR security mandates. Decoupled microservices combined with robust caching and gRPC protocols ensure sub-second EMR performance and seamless clinical workflows.