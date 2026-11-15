## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance for critical clinical workflows.

## Key Elements
*   **Users**: Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance / IT Auditor, Hospital Executive.
*   **External Systems**: External Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Business Analytics / Reporting Service.
*   **Containers**: Frontend Container (React, TypeScript), Edge Container (Kong / Envoy), Clinical Service (Go), Scheduling Service (Node.js), Billing Service (Spring Boot), Audit & Compliance Log Service (Go), Integration Service / FHIR Facade (Go).
*   **Clinical Service Components**: EMR Management Component, Patient Admission & Demographics Component, Clinical Data Access Repository, Audit & Event Publisher Component.
*   **Data & Infrastructure**: Apache Kafka / RabbitMQ, PostgreSQL, Redis, Encrypted S3-compatible Object Storage, Kubernetes (on-prem-k8s, AWS eu-central-1).

## Relationships
*   Edge Container -> Clinical Service: Routes incoming requests via internal mTLS [gRPC, REST over mTLS]
*   Clinical Service -> Clinical Data Access Repository: Reads and writes clinical records and cache [TLS-encrypted PostgreSQL, Redis]
*   Clinical Data Access Repository -> Object Storage: Archives long-term medical records [Encrypted S3-compatible APIs]
*   Clinical Service -> Event Bus: Publishes asynchronous domain events [Apache Kafka / RabbitMQ]
*   Integration Service -> External Systems: Exchanges health data [HL7 FHIR APIs]

## Technology Stack
*   **Go**: Powers the Clinical Service, Audit Service, and FHIR Facade for high performance and low latency.
*   **React & TypeScript**: Used for the responsive frontend container.
*   **PostgreSQL & Redis**: Provides ACID-compliant relational storage and high-speed in-memory caching for sub-second EMR retrieval.
*   **Apache Kafka / RabbitMQ**: Handles asynchronous event-driven messaging to decouple microservices.
*   **Kubernetes**: Orchestrates hybrid multi-region deployments with Horizontal Pod Autoscalers (HPA).
*   **OpenTelemetry**: Captures distributed traces and structured logs for system observability.

## Rationale
The microservices architecture combined with active-active Kubernetes deployments guarantees 99.99% availability and high resilience. Utilizing Go for core clinical components ensures sub-second P95 performance while maintaining robust AES-256 encryption and comprehensive audit trails for HIPAA and GDPR compliance.