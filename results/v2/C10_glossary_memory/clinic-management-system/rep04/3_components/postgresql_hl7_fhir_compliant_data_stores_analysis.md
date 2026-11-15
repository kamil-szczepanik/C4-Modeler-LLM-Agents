## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics, ensuring HIPAA and GDPR compliance. It provides secure, high-availability clinical operations, fast EMR retrieval, and robust external interoperability for medical staff, administrators, and patients.

## Key Elements
- **Patient Portal SPA/Mobile** (React/TypeScript): High-performance frontend user interface for patients.
- **Clinician/Admin Workspace SPA** (React/TypeScript): High-performance frontend user interface for clinicians and administrative staff.
- **API Gateway / BFF** (Envoy/Kong): API gateway for reverse proxy, routing, and token exchange.
- **Core Services Container** (Java/Spring Boot): Robust domain logic for core clinical services and electronic medical records.
- **Billing Service Container** (Node.js/TypeScript): Isolated financial and billing processing.
- **Integration Service Container** (Apache Camel / Spring Integration): HL7 FHIR translation adapters for interoperability with external lab and imaging systems.
- **Audit & Compliance Logging Container** (WORM-compliant storage / Spring Integration): Ensures comprehensive service mesh security and regulatory compliance logging.
- **PostgreSQL & HL7 FHIR Compliant Data Stores** (PostgreSQL 15+ with AES-256 at rest): Relational and JSONB persistence partitioned for 10-year retention.
- **Message Broker** (RabbitMQ/Kafka): Asynchronous messaging for resilient insurance claim submissions and decoupled communication.
- **Lab & Imaging Systems** (External system): External systems providing laboratory and imaging data.
- **Insurance Clearinghouse / External Billing Provider** (External system): External system for insurance claims and billing processing.

## Relationships
- Patient / Clinician / Billing Staff / Compliance Officer -> API Gateway / BFF: HTTPS (TLS 1.3, OAuth2/OIDC, MFA)
- API Gateway / BFF -> Patient Portal SPA/Mobile / Clinician/Admin Workspace SPA: HTTPS
- API Gateway / BFF -> Core Services Container / Billing Service Container: gRPC over mTLS
- Core Services Container -> Relational Core Component: JDBC over mTLS
- Core Services Container -> FHIR JSON Document Store Component: gRPC over mTLS / JSONB queries over mTLS
- Billing Service Container -> Message Broker: AMQP
- Billing Service Container -> Insurance Clearinghouse / External Billing Provider: HTTPS / EDI X12
- Integration Service Container -> Lab & Imaging Systems: HL7 FHIR over REST/JSON (TLS 1.3)
- PostgreSQL & HL7 FHIR Compliant Data Stores -> Audit & Compliance Logging Container: pgaudit streaming logs

## Technology Stack
- **Frontend**: React with TypeScript for high-performance responsive web and mobile UIs.
- **Backend Services**: Java/Spring Boot for core domain logic; Node.js/TypeScript for billing processing.
- **Gateway & Integration**: Envoy/Kong API Gateway; Apache Camel and Spring Integration for HL7 FHIR translation.
- **Persistence & Security**: PostgreSQL 15+ utilizing JSONB, GIN indexing, declarative partitioning, AWS KMS / HashiCorp Vault for AES-256 TDE, and `pgaudit` extension.
- **Messaging & Infrastructure**: RabbitMQ/Kafka for async messaging, Kubernetes (CloudNativePG/Patroni) for active-active high availability across `on-prem-k8s` and `eu-central-1`.

## Rationale
This hybrid cloud architecture combines strict microservices isolation, strong mTLS/RBAC security controls, and PostgreSQL partitioning to guarantee 99.99% uptime and HIPAA/GDPR compliance. It balances sub-second EMR search performance with a mandated 10-year data retention schedule across distributed healthcare environments.