## Overview
The Patient & Scheduling Service manages patient registrations, profile data, and real-time appointment scheduling for the Clinic Management System. It ensures secure, high-availability operations across hybrid cloud environments while maintaining strict healthcare compliance.

## Key Elements
- **PatientController & SchedulingController**: REST and gRPC entry points for client and API Gateway traffic.
- **PatientDomainService**: Manages demographic capture, RBAC/ABAC authorization, and GDPR data masking.
- **SchedulingEngine**: Executes real-time resource clash checks and asynchronous booking workflows.
- **AuditInterceptor**: Generates fail-secure, immutable audit trails for compliance.
- **EventDispatcher**: Emits domain events using the Transactional Outbox Pattern over Kafka.
- **AvailabilityCacheManager**: Caches anonymous slot metadata via encrypted Redis.
- **DataRepository**: Interfaces with PostgreSQL using TypeORM and AES-256 encryption.

## Relationships
- `API Gateway` -> `PatientController & SchedulingController` [gRPC / mTLS]
- `SchedulingEngine` -> `AvailabilityCacheManager` [Redis over TLS]
- `SchedulingEngine` & `PatientDomainService` -> `DataRepository` [TCP/SQL over TLS]
- `EventDispatcher` -> `Kafka Message Broker` [Kafka over TLS 1.3 with SASL/SCRAM]
- `AuditInterceptor` -> `HashiCorp Vault` [HTTPS]

## Technology Stack
- **NestJS (TypeScript)**: Provides modular architecture and dependency injection.
- **PostgreSQL & TypeORM**: Relational data storage supporting AES-256 encryption at rest.
- **Redis**: Low-latency caching for non-sensitive slot metadata with encryption in transit.
- **Kafka**: Asynchronous event streaming utilizing the Transactional Outbox Pattern.
- **HashiCorp Vault**: Secret management and dynamic credential issuance.

## Rationale
This architecture uses modular NestJS components combined with a Transactional Outbox Pattern to guarantee data consistency and 99.99% availability across hybrid Kubernetes and cloud regions. Strict payload minimization and encryption ensure full HIPAA and GDPR compliance without sacrificing sub-second performance.