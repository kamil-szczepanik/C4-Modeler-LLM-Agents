## Overview
The Patient Portal Service is a microservice component of the Clinic Management System that empowers patients and proxies to manage healthcare interactions. It facilitates self-service appointments, demographic updates, and EMR viewing while ensuring strict security and regulatory compliance.

## Key Elements
- Patients & Proxies: External users accessing the portal.
- API Gateway (Envoy / Kong): Entry point managing rate limiting and routing.
- Patient Portal Service (Node.js / TypeScript, Kubernetes): Core container encompassing internal components.
- Authentication Controller: Manages OAuth2/MFA flows via Identity Provider.
- Demographics Manager & EMR Viewer: Internal components handling profile updates and record rendering via Prisma ORM.
- Proxy Access Controller & Localization Manager: Components supporting delegated access and multilingual rendering.
- PostgreSQL Database & Apache Kafka: Persistence and event streaming layers.
- External Vault / HSM: Key management for encryption.

## Relationships
- Patients/Proxies -> API Gateway: Accesses portal functionality [HTTPS / TLS 1.3]
- API Gateway -> Patient Portal Service: Routes authenticated requests [gRPC over mTLS]
- Patient Portal Service -> Identity Provider: Validates JWT tokens and multi-factor authentication [OAuth2 / OIDC]
- Patient Portal Service -> PostgreSQL Database: Persists patient data and audit logs [TLS 1.3 with AES-256 at rest]
- Patient Portal Service -> Apache Kafka Message Broker: Publishes domain events [Internal TLS]
- Patient Portal Service -> Scheduling Service: Checks appointment resource clashes [gRPC over mTLS]

## Technology Stack
- Node.js & TypeScript: Selected for rapid asynchronous I/O handling in the portal service.
- Prisma ORM: Provides type-safe database access with enforced TLS connections.
- Node-rdkafka: Enables high-throughput asynchronous event publishing to Kafka.
- External Vault / HSM: Ensures automated cryptographic key rotation for data protection.

## Rationale
This architecture uses decoupled microservices and zero-trust Kubernetes network policies to meet high availability (99.99%) and HIPAA/GDPR compliance mandates. It isolates patient-facing workflows while maintaining secure, low-latency interoperability with core clinical systems.