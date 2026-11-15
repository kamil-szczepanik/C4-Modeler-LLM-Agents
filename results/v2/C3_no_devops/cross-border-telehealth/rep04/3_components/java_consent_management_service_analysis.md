## Overview
The Java Consent Management Service is a secure, Spring Boot-based component that enforces granular, jurisdiction-aware consent policies and tamper-evident audit trails for cross-border health data sharing. It ensures GDPR and HIPAA compliance by validating PASETO tokens and broadcasting instant (<1s) revocation events via GCP Cloud Pub/Sub.

## Key Elements
- Consent Controller / API Component (Spring MVC / gRPC)
- Consent Policy Engine Component (Spring Domain Logic)
- Audit & Cryptographic Proof Component (Spring Data JPA & Google Tink)
- Consent Rule Repository Component (Spring Cache / Redis)
- GCP Cloud SQL (PostgreSQL)
- GCP Cloud Pub/Sub
- GCP Cloud KMS

## Relationships
- Kong API Gateway/BFF -> Java Consent Management Service.Consent Controller: Validates tokens and consents [gRPC / Anthos Service Mesh (mTLS)]
- Consent Policy Engine -> GCP Cloud KMS: Signs and verifies cryptographic PASETO tokens [gRPC / IAM]
- Consent Policy Engine -> GCP Cloud Pub/Sub: Broadcasts instant revocation events [gRPC / Pub/Sub Protocol]
- Audit & Cryptographic Proof Component -> GCP Cloud SQL (PostgreSQL): Stores encrypted audit metadata and consent records [PostgreSQL Protocol with CMEK]

## Technology Stack
- Java & Spring Boot: Core runtime and framework for robust enterprise microservices.
- Spring MVC / gRPC: High-performance API exposure and inter-service communication.
- Google Tink & GCP Cloud KMS: Cryptographic operations, token signing, and key management.
- GCP Cloud SQL (PostgreSQL): Secure relational data storage with row-level security.
- GCP Cloud Pub/Sub: Asynchronous messaging for instant event broadcasting.
- Redis / Memorystore: In-memory caching for sub-millisecond policy evaluations.

## Rationale
This architecture guarantees strict regional data residency and rapid (<1s) consent revocation required by EU GDPR and US HIPAA mandates. The combination of in-memory caching and event-driven Pub/Sub ensures low-latency performance without compromising security or regulatory accountability.