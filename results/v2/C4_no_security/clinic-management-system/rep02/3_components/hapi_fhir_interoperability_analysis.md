## Overview
A hybrid-cloud Clinic Management System designed for medium-sized healthcare facilities to handle patient admissions, scheduling, Electronic Medical Records (EMR), and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and HL7 FHIR interoperability.

## Key Elements
- **Users**: Patients, Clinical Staff, Administrative Staff, Billing & Finance Officers, System/Compliance Administrators
- **External Systems**: Web Browsers, Patient Mobile App, External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Audit & Compliance SIEM
- **Containers & Components**: React SPA, Node.js Mobile BFF, Nginx/Kong API Gateway, Istio/Linkerd Service Mesh, Java/Spring Boot Clinical Services, Python/FastAPI Billing Services, HAPI FHIR Interoperability (Java / HAPI FHIR JPA Server with FHIR REST Facade, Validation Engine, Data Transformation Engine, Consent Enforcement Interceptor, Outbox Pattern Worker), Go Notification Worker, Python Compliance Worker, PostgreSQL, Apache Kafka, Redis, Debezium CDC, S3 Tiered Storage

## Relationships
- **API Gateway -> HAPI FHIR Interoperability**: Routes inbound FHIR requests via `gRPC over mTLS`
- **HAPI FHIR Interoperability -> PostgreSQL**: Queries and persists clinical data via `JDBC over TLS 1.3`
- **HAPI FHIR Interoperability -> Redis**: Caches read-heavy FHIR resources via `RESP over TLS`
- **HAPI FHIR Interoperability -> Apache Kafka**: Publishes event streams using `Kafka Protocol over TLS`
- **HAPI FHIR Interoperability -> External Lab & Imaging Systems**: Exchanges clinical data via `HL7 FHIR / REST`

## Technology Stack
- **Backend Services**: Java (Spring Boot, HAPI FHIR JPA Server), Python (FastAPI), Go for high-performance workers
- **Frontend**: React SPA, Node.js Mobile BFF
- **Data & Caching**: PostgreSQL with AES-256 encryption, Redis for read-through caching
- **Messaging & Streaming**: Apache Kafka with Debezium CDC for event-driven durability
- **Infrastructure & Mesh**: Kubernetes (Hybrid on-prem + eu-central-1), Istio/Linkerd service mesh, Nginx/Kong API Gateway
- **Observability**: OpenTelemetry distributed tracing, Fluentbit for centralized SIEM log shipping

## Rationale
This architecture uses an event-driven, hybrid-cloud microservices design with read-through caching and CDC streaming to guarantee sub-second EMR response times and 99.99% availability. Strict protocol security, Istio circuit breaking, and HAPI FHIR consent interceptors ensure robust HIPAA/GDPR compliance and seamless third-party lab interoperability.