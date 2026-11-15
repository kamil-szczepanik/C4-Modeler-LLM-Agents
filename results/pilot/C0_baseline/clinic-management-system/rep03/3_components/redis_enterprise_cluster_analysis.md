## Overview
[The Clinic Management System provides patient registration, EMR, scheduling, and billing for healthcare providers while maintaining HIPAA and GDPR compliance. It utilizes a hybrid cloud architecture to guarantee 99.99% high availability and sub-second performance.]

## Key Elements
- Patients, Front Desk Staff, Clinicians, Billing Specialists
- Patient Portal SPA & Clinician Workspace SPA (React)
- API Gateway (Kong/Envoy)
- Core Clinical Services & Finance & Billing (Spring Boot)
- PostgreSQL cluster (PostgreSQL with PgBouncer)
- Elasticsearch (Elasticsearch)
- Redis Enterprise cluster (Redis Enterprise)
- Kafka event bus (Apache Kafka)
- External Systems: Payment Gateway, Insurance Verification/RTE APIs, Lab & Imaging Systems

## Relationships
- Patients & Staff -> Patient/Clinician SPAs: Accesses UI via HTTPS/TLS 1.3
- SPAs -> API Gateway (Kong/Envoy): Routes client traffic via REST/GraphQL [HTTPS/TLS 1.3]
- API Gateway -> Core Clinical Services & Finance & Billing: Dispatches requests via gRPC/REST [mTLS]
- Core Clinical Services & Finance & Billing -> PostgreSQL cluster: Reads/writes relational data [PostgreSQL Wire Protocol over TLS]
- Core Clinical Services & Finance & Billing -> Redis Enterprise cluster: Caches data and handles locking [RESP3 over TLS]
- Core Clinical Services & Finance & Billing -> Kafka event bus: Publishes and consumes domain events [TCP/TLS]
- Core Clinical Services -> External Lab & Imaging Systems: Exchanges health records [HL7 FHIR REST APIs over TLS]

## Technology Stack
- React: Powers responsive single-page applications for patients and clinicians
- Spring Boot: Implements robust microservices for core clinical and billing logic
- PostgreSQL: Provides ACID-compliant relational storage for primary medical records
- Redis Enterprise: Delivers low-latency distributed caching, session management, and appointment locking via CRDTs
- Apache Kafka: Enables reliable, decoupled event-driven messaging across services
- Kubernetes (on-prem-k8s & eu-central-1): Orchestrates hybrid cloud containers with high availability
- AES-256 & TLS 1.3: Secures data at rest and in transit for HIPAA/GDPR compliance

## Rationale
[This hybrid architecture separates scalable stateless frontend and service layers from persistent databases to meet strict 99.99% availability SLAs. Furthermore, utilizing Redis Enterprise with CRDTs and PostgreSQL ensures robust data consistency, local low-latency caching, and regulatory compliance across hybrid environments.]