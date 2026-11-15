## Overview
The Clinic Management System is a hybrid-cloud clinical IT platform designed to manage patient admissions, EMR, scheduling, and billing for medium-sized hospitals. It ensures high availability (99.99%), AES-256 encryption, and HIPAA/GDPR compliance.

## Key Elements
- **Users**: Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators
- **Containers**: Web Application Gateway (NGINX), Core API Service (Node.js / NestJS), EMR Engine (Java / Spring Boot), Billing Worker (Python / Celery), Audit Logging Sidecar, PostgreSQL Cluster, Redis, Apache Kafka
- **Core API Service Components**: API Gateway Controller Layer, Domain Orchestration Service, Data Access Repository Layer, Security Interceptor, Audit Dispatcher Component, Interoperability Adapter Component, Distributed Locking Component
- **External Systems**: Identity Provider, Third-Party Payment Gateways, External Laboratory & Imaging Systems

## Relationships
- Web Application Gateway -> Core API Service: Routes API requests [gRPC over TLS]
- Core API Service -> EMR Engine: Communicates with EMR service [gRPC over TLS]
- Core API Service -> PostgreSQL Cluster: Persists transactional data [TCP with mTLS]
- Core API Service -> Redis: Caches data and coordinates locks [TCP with mTLS]
- Core API Service -> Apache Kafka: Publishes billing messages [TCP with mTLS]
- Core API Service -> Identity Provider: Authenticates users [OAuth2/JWT]
- Core API Service -> Third-Party Payment Gateways: Processes payments [REST/HTTPS]
- Core API Service -> External Laboratory & Imaging Systems: Integrates clinical data [HL7 FHIR REST APIs]

## Technology Stack
- **Node.js / NestJS**: Powers the Core API Service with modular dependency injection and high performance.
- **Fastify**: Used via adapters in the controller layer for optimized throughput.
- **Prisma ORM**: Provides type-safe query management against the database.
- **Redis**: Coordinates atomic resource clash checks and distributed locking.
- **PostgreSQL**: Stores transactional clinical and demographic data securely.
- **Apache Kafka**: Publishes asynchronous billing and event messages.
- **OpenTelemetry**: Provides distributed tracing across all gRPC and FHIR boundaries.

## Rationale
This architecture uses a modular NestJS framework and active-active scaling to meet sub-second EMR response times and 99.99% uptime constraints. Hybrid deployment, mTLS encryption, and immutable audit dispatchers ensure strict HIPAA and GDPR compliance for sensitive PHI.