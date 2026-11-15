## Overview
The Consent & Audit Service is an internal Java Spring Boot component within the Cross-Border Telehealth Platform responsible for managing patient data-sharing consents and generating immutable audit logs. It enforces strict regional data residency and compliance for EU and US patients.

## Key Elements
- **Consent Controller**: Spring MVC component handling fine-grained REST/gRPC consent management endpoints.
- **Compliance Enforcement Engine**: Java domain logic paired with local OPA policy bundles for evaluating cross-region data access.
- **Consent Token Issuer**: Nimbus JOSE+JWT component generating cryptographically signed, short-lived JWT consent assertions.
- **Audit Logger**: Asynchronous Spring Cloud Stream listener capturing immutable audit trails for AI recommendations and access requests.
- **Data Retention Manager**: Spring Batch component enforcing jurisdictional data purging and residency policies.

## Relationships
- `Consent Controller` & `Compliance Enforcement Engine` -> `Google Cloud SQL & GCS`: Regional data access via Spring Data JPA using secure local drivers.
- `Audit Logger` -> `Google Cloud SQL`: Append-only audit logging via secure local drivers with `INSERT`-only database privileges.
- `Compliance Enforcement Engine` -> `Consent Token Issuer`: Internal handoff of validated consent state for token generation.
- `Consent Token Issuer` -> `API Gateway / BFF`: Issues signed consent assertions via gRPC over TLS.

## Technology Stack
- **Java 17 / Spring Boot**: Core framework chosen for enterprise readiness and robust security libraries.
- **Open Policy Agent (OPA)**: Sidecar architecture for decentralized, region-autonomous policy enforcement.
- **Nimbus JOSE+JWT**: Library for issuing asymmetric (RS256/ES256) signed JWTs.
- **Google Cloud SQL (PostgreSQL) & Memorystore (Redis)**: Regional data stores with append-only constraints and distributed token revocation checks.
- **GCP KMS**: Regional key rings providing customer-managed encryption keys (CMEK) for data isolation.

## Rationale
This component architecture enforces strict GDPR and HIPAA boundaries by isolating regional execution and data persistence within GCP `europe-west3` and `us-central1`. Cryptographic consent tokens and append-only audit logs guarantee traceability and immutability without cross-region dependencies.