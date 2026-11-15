## Overview
- Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
- Operates in a hybrid cloud environment with strict HIPAA/GDPR compliance and 99.99% availability.

## Key Elements
- Users: Clinic Receptionist/Admin, Clinician (Doctor/Nurse), Billing Specialist, Patient, Hospital/Clinic Administrator, External Auditors
- External Systems: External Lab & Imaging Systems, Insurance Claim Processors, Identity Provider (IdP) with local cache proxy
- Containers: Envoy/NGINX API Gateway, Patient Intake Container, Scheduling Engine Container, EMR Workspace Container (Go/gRPC), Billing & Claims Container, Integration & FHIR Mediator (Apache Camel K)
- Infrastructure: Primary Database (PostgreSQL with Citus), Event Broker (Redpanda), Observability Stack (OpenTelemetry, Grafana Mimir/Tempo, Falco)
- EMR Components: gRPC API Handler, EMR Business Logic Engine, PHI Crypto Middleware, Distributed L2 Cache, Audit & Event Emitter

## Relationships
- Envoy/NGINX API Gateway -> EMR Workspace Container: Routes Erom/EMR requests [HTTP/2 / gRPC over mTLS]
- EMR Workspace Container -> Primary Database: Reads and writes EMR data [Encrypted internal TCP]
- EMR Workspace Container -> Redpanda: Publishes EMR events and audit logs [Encrypted internal TCP]
- EMR Workspace Container -> External Lab & Imaging Systems: Exchanges lab and imaging data [HL7 FHIR APIs over HTTPS]
- PHI Crypto Middleware -> Cloud KMS / HSM: Fetches data encryption keys [gRPC over mTLS]
- EMR Business Logic Engine -> Distributed L2 Cache: Reads/writes hot session state [RESP over TLS]

## Technology Stack
- Go & gRPC: Chosen for the EMR Workspace Container to deliver high-performance execution and low latency.
- PostgreSQL with Citus: Selected for relational data storage with horizontal scalability.
- Redpanda: Implemented as the event broker for high-throughput, reliable domain messaging.
- Redis (Redis Enterprise): Used for the Distributed L2 Cache supporting active-active geo-replication.
- Tink Crypto Library & Cloud KMS: Utilized for application-layer AES-256 column-level encryption and envelope encryption.
- OpenTelemetry: Deployed for distributed tracing and performance monitoring.

## Rationale
- The hybrid microservices architecture leverages Go, gRPC, and a distributed L2 cache to consistently achieve sub-second P95 EMR screen loads.
- Comprehensive encryption, immutable audit logging, and strict RBAC/ABAC controls ensure full HIPAA and GDPR compliance across regions.