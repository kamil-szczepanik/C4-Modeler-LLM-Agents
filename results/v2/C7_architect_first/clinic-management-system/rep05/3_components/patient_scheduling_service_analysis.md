## Overview
The Patient & Scheduling Service is a Node.js/TypeScript microservice within the Clinic Management System responsible for patient registration, electronic medical records, and appointment scheduling. It ensures HIPAA/GDPR compliance and 99.99% availability across a hybrid cloud infrastructure.

## Key Elements
- **API Gateway**: Kong / Nginx / Envoy sidecar handling incoming client traffic
- **Patient & Scheduling Service**: Node.js / TypeScript container for core workflows
- **Patient Controller & Scheduling Controller**: NestJS controllers handling gRPC endpoints
- **Appointment Engine & Conflict Resolution Service**: Domain services managing resource checks and slot alternatives
- **Data Access Repository & Outbox Dispatcher**: TypeORM/Prisma persistence layer with transactional outbox pattern
- **Event Publisher**: KafkaJS component publishing domain events via TCP/TLS
- **PostgreSQL Databases**: Primary database with PgBouncer connection pooling and read replicas
- **Apache Kafka Event Broker**: Distributed event streaming platform

## Relationships
- API Gateway -> Patient & Scheduling Service: Routes requests via gRPC / Internal Mesh with mTLS
- Scheduling Controller -> Appointment Engine: Invokes business logic via direct method calls
- Appointment Engine -> Conflict Resolution Service: Triggers slot-finding logic upon clash detection
- Data Access Repository -> PostgreSQL Databases: Reads and writes data via TCP / TLS with pessimistic locking
- Data Access Repository -> Outbox Dispatcher: Persists domain events atomically
- Event Publisher -> Apache Kafka Event Broker: Publishes domain events via TCP / TLS

## Technology Stack
- **Node.js / TypeScript**: Core runtime and language for fast API handling and type safety
- **NestJS**: Framework for structured controllers and dependency injection
- **PostgreSQL**: Relational database chosen for ACID compliance and audit trail support
- **Apache Kafka**: Event broker selected for asynchronous, reliable microservice communication
- **HashiCorp Vault**: Secret management for dynamic credential and JWT key injection
- **Istio Service Mesh**: Enforces mTLS and secure cross-region routing

## Rationale
This architecture uses active-active Kubernetes deployments and a transactional outbox pattern to guarantee high availability and prevent split-brain data states. It incorporates strict encryption, data residency policies, and ABAC authorization to fulfill stringent HIPAA and GDPR compliance requirements.