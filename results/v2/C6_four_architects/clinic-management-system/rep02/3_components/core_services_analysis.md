## Overview
The Clinic Management System is a hybrid-cloud healthcare IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. It ensures high availability (99.99%) and strict HIPAA/GDPR compliance while delivering sub-second EMR performance.

## Key Elements
- **Core Services Container**: NestJS-based backend housing clinical and administrative logic.
- **Patient Management Component**: Handles demographic capture via TypeORM.
- **Scheduling Engine Component**: Manages appointment scheduling and resource clash checks.
- **Billing Service Component**: Processes claims and invoices via HTTP/REST.
- **Audit Logger Component**: Publishes immutable audit trails.
- **Access Control & Policy Enforcer Component**: Validates JWT claims and scopes.
- **FHIR Data Mapper Component**: Translates models into HL7 FHIR standards.
- **Encryption-at-Rest Middleware Component**: Applies AES-256 field-level encryption.
- **Patient Data Repository Component**: Encapsulates data queries and PHI protection.
- **Config & Secret Manager Component**: Fetches dynamic runtime configurations and keys.

## Relationships
- `Scheduling Engine` -> `Cache / State Store`: Read/Write lock states via `TCP/TLS (RESP)`.
- `Billing Service` -> `Insurance Clearinghouses`: Submit claims via `HTTPS/REST`.
- `Audit Logger` -> `Message Broker`: Produce audit events via `AMQP/TLS`.
- `FHIR Data Mapper` -> `Integration Service`: Publish standardized resources via `gRPC/TLS`.
- `Patient Management / Billing` -> `Encryption-at-Rest Middleware`: Encrypt data via `Node.js Crypto Module (AES-256-GCM)`.
- `Patient Data Repository` -> `Data Layer`: Encrypted SQL queries via `TLS (TCP/JDBC)`.
- `Encryption-at-Rest Middleware` -> `Config & Secret Manager`: Retrieve keys via `HTTPS`.
- Internal components -> Access Control / Event Dispatcher: In-process NestJS middleware and `EventEmitter`.

## Technology Stack
- **Backend Framework**: Node.js / NestJS for rapid administrative and billing workflow development.
- **Database & Storage**: PostgreSQL and MinIO/AWS S3 for structured data and file persistence.
- **Caching & State**: Redis Cluster for ultra-low latency scheduling conflict detection.
- **Messaging**: Apache Kafka for asynchronous event distribution and audit logging.
- **Security**: Keycloak for identity management, AES-256-GCM for field-level encryption, and JWT for access control.
- **Interoperability**: Apache Camel and HL7 FHIR APIs for lab and imaging integration.

## Rationale
This architecture uses modular NestJS components with in-process function calls to eliminate network overhead, ensuring P95 EMR screen loads under 1 second. Strict field-level encryption, audit logging, and RBAC mechanisms guarantee full HIPAA and GDPR compliance without compromising the 99.99% active-active availability target.