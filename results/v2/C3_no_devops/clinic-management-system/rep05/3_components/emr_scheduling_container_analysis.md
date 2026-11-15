## Overview
[Clinic Management System managing patient admissions, EMR, scheduling, and billing for healthcare facilities. Built for 99.99% availability, HIPAA/GDPR compliance, and sub-second P95 performance.]

## Key Elements
* API Gateway / BFF (Kong / Envoy)
* Patient Portal (Node.js / TypeScript)
* EMR & Scheduling Container (Java Spring Boot)
* Patient & EMR Management Component (Spring Data JPA / Hibernate)
* Scheduling & Clash Detection Engine (Java / Redis)
* FHIR Interoperability Adapter (HAPI FHIR / Spring WebClient)
* Clinical Workflow & Telemetry Component (Micrometer / OpenTelemetry)
* Data & Messaging Layer (PostgreSQL, Redis, Apache Kafka, Debezium)
* Lab & Imaging Systems

## Relationships
* API Gateway / BFF -> EMR & Scheduling Container: Routes requests [HTTPS/REST, mTLS]
* Scheduling & Clash Detection Engine -> Redis: Acquires distributed locks [Redis Protocol / TLS]
* Patient & EMR Management Component -> PostgreSQL: Persists EMR records with audit logs [JDBC / gRPC, AES-256]
* EMR & Scheduling Container -> Lab & Imaging Systems: Integrates for labs/imaging [HL7 FHIR APIs]
* Clinical Workflow & Telemetry Component -> Apache Kafka: Publishes sanitized telemetry [Apache Kafka / TLS]

## Technology Stack
* Java Spring Boot: Core runtime for EMR & Scheduling container ensuring high performance and robust business logic.
* Redis: Distributed locking mechanism for fast (<50ms) resource clash detection.
* PostgreSQL: Primary persistent store utilizing JDBC/gRPC with AES-256 encryption at rest.
* Apache Kafka: Asynchronous event backbone for sagas and telemetry streaming.
* HAPI FHIR: Translates domain models to HL7 FHIR resources for interoperability.
* Micrometer / OpenTelemetry: Captures performance traces and UX telemetry.

## Rationale
[The hybrid architecture utilizes Spring Boot and Redis for low-latency EMR access and rapid scheduling clash checks. Strict security protocols, mTLS, and zero-trust authorization guarantee full HIPAA and GDPR compliance.]