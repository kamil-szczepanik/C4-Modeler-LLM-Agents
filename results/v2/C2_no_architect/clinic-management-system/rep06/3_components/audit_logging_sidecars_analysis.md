## Overview
The Clinic Management System is a hybrid cloud platform providing patient admissions, scheduling, Electronic Medical Records, and billing for medium-sized healthcare facilities. It ensures high availability (99.99%), strict regulatory compliance (HIPAA, GDPR, 10-year data retention), and secure interoperability.

## Key Elements
* Audit Logging sidecars (Logging / WORM): Enforce immutable compliance, audit tracking, and zero-loss queuing.
* Compliance Officers: Internal users reviewing security dashboards and investigating audit trails.
* AWS S3 Object Lock: Immutable external storage tier enforcing 10-year retention policies.
* Fluentbit / Logstash Daemonsets: Asynchronous log ingestion and parsing pipelines.
* Application Containers: Co-located EMR and billing microservices communicating via local Unix domain sockets.
* SPIFFE/SPIRE: Identity management framework issuing short-lived SVIDs.

## Relationships
* Application Containers to Audit Logging sidecars: Ingests log streams locally via Unix domain sockets.
* Audit Logging sidecars to Fluentbit / Logstash Daemonsets: Streams logs asynchronously using TLS.
* Fluentbit / Logstash to AWS S3 Object Lock: Forwards logs for permanent storage using mTLS authenticated via SPIFFE/SPIRE SVIDs.
* Compliance Officers to Audit Logging / S3: Accesses searchable compliance dashboards over HTTPS.

## Technology Stack
* AWS S3 Object Lock: Chosen for immutable, WORM-compliant storage meeting the 10-year data retention mandate.
* Unix Domain Sockets: Selected for secure, high-performance inter-container communication between applications and audit sidecars.
* SPIFFE/SPIRE: Implemented for zero-trust, automated workload identity and mTLS authentication.
* Fluentbit / Logstash Daemonsets: Utilized to offload heavy payload processing and avoid application-side latency.
* Cryptographic Hash-Chaining: Implemented locally to ensure tampering or truncation of logs is mathematically detectable.

## Rationale
This architecture ensures uncompromising regulatory compliance and zero-loss audit logging without violating strict P95 performance constraints. By combining stateless sidecars, local buffering with application throttling, and immutable cloud storage, the system achieves both HIPAA/GDPR mandates and 99.99% availability.