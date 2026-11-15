## Overview
The Clinic Management System is a hybrid cloud-based clinical IT platform that manages patient admissions, electronic medical records (EMRs), scheduling, and billing. Its core purpose is to provide highly available, secure, and interoperable healthcare operations for medium-sized hospitals and clinics.

## Key Elements
- Patients and Clinicians/Receptionists (People)
- API Gateway (Kong / NGINX)
- Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service (FHIR Adapter)
- Audit Service components: Audit API Controller, Event Normalizer & Processor, WORM Storage Writer, Retention Enforcement Manager (Spring Boot / Java)
- External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- Apache Kafka, PostgreSQL, Redis, Elasticsearch / WORM storage

## Relationships
- Patients & Clinicians -> API Gateway via HTTPS / TLS 1.3
- Audit API Controller -> Apache Kafka via Kafka Consumer Protocol (TCP)
- WORM Storage Writer -> Elasticsearch / WORM storage via HTTPS / S3 Object Lock API with AES-256
- Integration Service -> External Lab & Imaging Systems via HL7 FHIR REST APIs

## Technology Stack
- Spring Boot (Java) & Node.js for backend microservices due to enterprise support and high concurrency
- Apache Kafka for asynchronous, decoupled event-driven communication
- PostgreSQL with AES-256 encryption at rest for relational data
- Elasticsearch / WORM storage with AWS S3 Object Lock for immutable 10-year audit logging
- Kubernetes (on-prem-k8s and AWS eu-central-1) for high-availability container orchestration

## Rationale
This hybrid architecture satisfies HIPAA, GDPR, and 10-year data retention mandates through strict component isolation, immutable WORM storage, and end-to-end encryption. An active-active deployment model across on-premise and AWS regions ensures 99.99% high availability and low-latency performance.