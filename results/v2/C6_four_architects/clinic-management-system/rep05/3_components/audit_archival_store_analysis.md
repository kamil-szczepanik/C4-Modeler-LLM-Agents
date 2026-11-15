## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities with strict HIPAA/GDPR compliance. It utilizes a hybrid cloud architecture designed for 99.99% availability and a 10-year data retention mandate.

## Key Elements
- **Users**: Patient, Clinician/Staff, Billing Administrator
- **External Systems**: Identity Provider (Keycloak), Insurance Gateway, External Lab & Imaging Systems, National Health Registry, SMS/Notification Gateway
- **Containers**: API Gateway (Nginx / Kong), Patient & Scheduling Service, EMR Service, Billing Service, FHIR Interoperability Service, Background Worker, Distributed Cache (Redis Enterprise), Message Broker (Apache Kafka), Primary Database (PostgreSQL), Audit & Archival Store, Internal Service Mesh (Istio / Envoy)
- **Audit & Archival Store Components**: Ingestion API Gateway, Encryption & Hashing Engine, Tiering & Lifecycle Manager, Compliance Query Interface, Integrity Verifier, Audit Export & Redaction Service

## Relationships
- **Background Worker -> Audit & Archival Store**: Writes cold audit data via `HTTPS`
- **Ingestion API Gateway -> Encryption & Hashing Engine**: Passes logs for encryption via `In-memory / Internal IPC`
- **Encryption & Hashing Engine -> Audit & Archival Store**: Persists immutable objects via `HTTPS / S3 API`
- **Tiering & Lifecycle Manager -> Audit & Archival Store**: Applies lifecycle rules via `S3 Lifecycle API`
- **Integrity Verifier -> Audit & Archival Store**: Validates checksums via `HTTPS / S3 API`
- **Compliance Query Interface -> Audit Export & Redaction Service**: Delegates exports via `Internal gRPC`
- **Audit Export & Redaction Service -> Audit & Archival Store**: Retrieves archival subsets via `HTTPS / S3 API`

## Technology Stack
- **Languages & Frameworks**: Java/Spring Boot (Services), Node.js/TypeScript (Billing), Python/FastAPI (FHIR/Export Services)
- **Storage & Caching**: PostgreSQL with PgBouncer, Redis Enterprise, AWS S3 / On-Prem Object Storage with WORM Object Lock
- **Messaging & Infrastructure**: Apache Kafka, Istio/Envoy, Nginx/Kong, Keycloak, Prometheus/Grafana Promtail

## Rationale
This hybrid architecture uses active-active multi-region deployment and WORM-enabled object storage to guarantee 99.99% uptime and strict 10-year tamper-proof compliance. Microservices separation and FHIR integration ensure interoperability and low-latency EMR performance.