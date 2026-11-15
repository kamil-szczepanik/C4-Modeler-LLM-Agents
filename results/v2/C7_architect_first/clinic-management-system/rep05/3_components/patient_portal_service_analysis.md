## Overview
The Patient Portal Service is a container within the Clinic Management System that handles patient-facing workflows, self-service onboarding, appointment interactions, and secure communication. It ensures strict HIPAA/GDPR compliance and high availability across a hybrid cloud architecture.

## Key Elements
- **Portal Controller / Router**: NestJS/Express.js router handling incoming gRPC and HTTP requests.
- **Patient Profile & Auth Manager**: Enforces MFA, OIDC JWT validation, RBAC/ABAC, and proxy access.
- **Appointment View Component**: Manages appointment history and slot selection.
- **Consent & Preference Handler**: Captures and verifies GDPR/HIPAA compliance flags with cryptographic audit trails.
- **Notification & Engagement Manager**: Triggers SMS/email alerts via external gateways with stripped PHI/PII.
- **Data Access Repository**: Manages encrypted database persistence.
- **Event Publisher**: Emits domain events to Apache Kafka.

## Relationships
- API Gateway -> Portal Controller / Router: Routes incoming requests [gRPC / Internal Mesh with mTLS]
- Portal Controller / Router -> Patient Profile & Auth Manager: Forwards authentication and demographic interactions [In-memory / Function Call]
- Appointment View Component -> Data Access Repository: Queries and updates appointment data [TypeScript/ORM via TCP/TLS]
- Event Publisher -> Apache Kafka: Publishes domain events [TCP / TLS]
- Notification & Engagement Manager -> External Notification Gateway: Sends alerts [HTTPS / REST]

## Technology Stack
- **Node.js / TypeScript**: Core runtime and language for the Patient Portal Service, chosen for asynchronous throughput.
- **NestJS**: Framework providing modular architecture for internal components.
- **PostgreSQL**: Primary data store with AES-256 encryption at rest and column-level PII protection.
- **Apache Kafka**: Event broker for asynchronous, decoupled event-driven communication.
- **HashiCorp Vault**: Dynamic secret management for database credentials and external API keys.
- **Envoy**: Sidecar proxy managing mTLS and distributed tracing.

## Rationale
This architecture guarantees 99.99% uptime and strict HIPAA/GDPR compliance through containerized modularity, active-active hybrid deployment readiness, and zero-trust security controls. Decoupling notification and event processing via Kafka ensures system resilience and low-latency performance.