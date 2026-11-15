## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. The system ensures high availability, 10-year data retention, and strict HIPAA and GDPR compliance across hybrid cloud infrastructure.

## Key Elements
- Patients, Clinicians/Staff, and Hospital Administrators
- API Gateway (Kong/Envoy)
- Web Frontend (React/TypeScript on Nginx/CloudFront)
- Core Services Container (Java/Spring Boot)
- EMR Service (Node.js/TypeScript)
- Database Layer (PostgreSQL)
- Integration Worker (Apache Camel/Python) with internal components: Route Orchestrator, FHIR Transformer, Connector Client, Security Enforcer, DLQ Handler, and Worker Health Monitor
- Event Broker (Apache Kafka)
- Audit Log Store (PostgreSQL Append-Only tables / AWS S3 Glacier)
- Key Management Service (HashiCorp Vault / AWS KMS)
- Background Job Scheduler (Temporal.io)
- Global Load Balancer (AWS Route 53 / Envoy Global)
- Observability Collector (OpenTelemetry / Prometheus / Grafana Loki)
- External Systems: Identity Provider, Insurance Gateway, External Lab & Imaging Systems, Notification Gateway, AWS S3 Glacier Backup

## Relationships
- Web Frontend -> API Gateway: Routes client requests [HTTPS/REST]
- API Gateway -> Core Services Container & EMR Service: Dispatches authenticated requests [gRPC/HTTPS]
- Core Services Container & EMR Service -> Database Layer: Reads and writes transactional data [JDBC/PostgreSQL Protocol]
- Integration Worker -> Event Broker: Streams messages asynchronously [Kafka over TLS]
- Integration Worker -> Key Management Service: Accesses encryption keys [HTTPS/REST with mTLS]
- Integration Worker -> External Lab & Imaging Systems: Exchanges clinical data [HL7 FHIR REST over HTTPS with mTLS]
- Integration Worker -> Observability Collector: Exports telemetry data [gRPC/OTLP over TLS]

## Technology Stack
- Java/Spring Boot: Powers core transactional services for enterprise reliability
- Node.js/TypeScript: Drives the EMR Service for high-performance UI data loads (< 1s P95)
- PostgreSQL: Provides robust relational data storage and append-only audit logging
- Apache Kafka: Enables asynchronous, decoupled event streaming across containers
- Apache Camel & Python: Powers the Integration Worker for robust routing and FHIR transformations
- HashiCorp Vault / AWS KMS: Secures data at rest via AES-256 encryption and key management
- Kubernetes / AWS: Orchestrates hybrid cloud, active-active deployments for 99.99% uptime

## Rationale
The hybrid cloud architecture combines on-premises Kubernetes and AWS to meet strict regional data residency and 99.99% active-active availability constraints. Polyglot microservices and decoupled event-driven messaging ensure sub-second performance, airtight HIPAA/GDPR security, and seamless interoperability via HL7 FHIR APIs.