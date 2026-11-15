## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability, stringent compliance, and clinical interoperability.

## Key Elements
- **Users**: Patient, Clinician / Receptionist, Compliance Officer
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Notification Service
- **Containers**: API Gateway (Kong / NGINX), Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service (FHIR Adapter), Audit Service, Apache Kafka, PostgreSQL, Redis, Elasticsearch / WORM storage
- **Components (Elasticsearch / WORM)**: Ingest Node / REST API Gateway, Index Lifecycle Management (ILM) Engine, WORM Storage Engine, Audit Data Node Cluster, Access Control & RBAC Component

## Relationships
- **Audit Service -> Ingest Node**: Streams audit events via REST over HTTPS, TLS 1.3, Mutual TLS
- **Ingest Node -> Audit Data Node Cluster**: Indexes validated records via Internal Transport Protocol over TCP, TLS 1.3
- **ILM Engine -> WORM Storage Engine**: Migrates and locks indexes via S3 API with Object Lock
- **Audit Data Node Cluster -> WORM Storage Engine**: Offloads older indices via S3 API, TLS 1.3
- **Compliance Officer -> Access Control Component**: Queries audit trails via HTTPS, RBAC, OAuth2/OIDC
- **Containers -> External Systems**: Connects via HL7 FHIR APIs, HTTPS, and secure payment protocols

## Technology Stack
- **Backend Services**: Spring Boot (Java) and Node.js for microservices logic
- **Messaging**: Apache Kafka for asynchronous event streaming
- **Databases**: PostgreSQL with AES-256 encryption for relational EMR and operational data
- **Caching**: Redis for rapid resource clash checks and session state
- **Audit & Compliance Storage**: Elasticsearch (Lucene engine) with ILM policies, frozen tier searchable snapshots, and AWS S3 Object Lock (Compliance Mode)
- **Security & Infrastructure**: Kong / NGINX API Gateway, TLS 1.3, OpenID Connect, On-Premise Kubernetes and AWS (eu-central-1)

## Rationale
This hybrid architecture isolates critical clinical workflows while leveraging scalable cloud and on-premise components. It enforces HIPAA and GDPR compliance, multi-factor authentication, AES-256 encryption, and immutable 10-year data retention.