## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to deliver secure, highly available, and interoperable clinical IT workflows while strictly adhering to HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patients, Clinicians, Administrative Staff, Billing Officers, Regulatory Auditors
- **External Systems**: Enterprise Identity Provider, External Lab/Imaging Systems, Payment Gateway, Insurance Clearinghouse, Audit Archive
- **Containers**: API Gateway (Kong/Nginx), Frontend Container (Next.js/Node.js), Clinical Core Container (Java Spring Boot), Scheduling & Resource Engine (Python/Go with Redis), Interoperability Service (Apache Camel / HAPI FHIR), Billing & Claims Worker (.NET Core with RabbitMQ)
- **Clinical Core Components**: Patient Registry Component, EMR Management Component, Clinical Persistence Facade, CDS Integration Component, Search & Indexing Sub-component

## Relationships
- **API Gateway -> Clinical Core Container**: Routes clinical requests [mTLS / gRPC / HTTP/2 over TLS]
- **EMR Management Component -> PostgreSQL**: Executes transactional reads/writes [JDBC over SSL with HikariCP]
- **Clinical Core Container -> Audit Archive**: Streams cryptographically signed audit logs [Secure TCP]
- **EMR Management Component -> CDS Integration Component**: Dispatches async event hooks [In-process Spring Events]
- **Patient Registry Component -> PostgreSQL**: Executes similarity queries using `pg_trgm` [JDBC over SSL]

## Technology Stack
- **Java Spring Boot**: Powers the Clinical Core Container for robust, enterprise-grade backend services.
- **Spring Security & Spring AOP**: Enforces method-level RBAC/ABAC and generates immutable audit trails for compliance.
- **PostgreSQL**: Stores relational data encrypted with AES-256 at rest, utilizing HikariCP and the `pg_trgm` extension for fast fuzzy searches.
- **Spring WebFlux & Resilience4j**: Implements non-blocking, asynchronous outbound integrations for Clinical Decision Support (CDS).
- **HashiCorp Vault**: Manages and rotates application secrets via Kubernetes projected service account volumes.

## Rationale
This architecture uses a hybrid cloud deployment with active-active Kubernetes clusters to guarantee 99.99% availability and meet stringent HIPAA/GDPR data retention mandates. Decomposing the Clinical Core Container with asynchronous components and localized connection pooling ensures sub-second EMR screen loads (P95 < 1s) without compromising security or scalability.