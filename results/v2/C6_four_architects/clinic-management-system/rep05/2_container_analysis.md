## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It delivers high availability, sub-second performance, and strict HIPAA/GDPR compliance via a hybrid-cloud architecture.

## Key Elements
* **API Gateway:** Nginx/Kong container handling SSL termination, rate limiting, and JWT validation via OIDC.
* **Patient & Scheduling Service:** Java/Spring Boot container managing registrations and appointments.
* **EMR Service:** Java/Spring Boot container handling clinical notes, audit trails, and gRPC communication.
* **Billing Service:** Node.js/TypeScript container handling insurance claims and billing.
* **FHIR Interoperability Service:** Python/FastAPI container translating data to HL7 FHIR standards.
* **Background Worker:** Python/Celery container handling asynchronous tasks, PDF generation, and log offloading.
* **Keycloak Container:** Local IAM container managing RBAC tokens and local token introspection.
* **Observability Agent:** Prometheus/Grafana Promtail sidecar container for metrics and structured logging.
* **Distributed Cache:** Redis Enterprise cluster providing fast data reads.
* **Message Broker:** Apache Kafka cluster for asynchronous event-driven decoupling.
* **Primary Database:** PostgreSQL multi-master active-active cluster with AES-256 encryption.
* **Database Access Proxy:** PgBouncer with IAM authentication for connection pooling.
* **Audit & Archival Store:** AWS S3 / On-Prem Object Storage for 10+ year immutable data retention.
* **Internal Service Mesh:** Istio/Envoy enforcing mutual TLS (mTLS) across all containers.

## Relationships
* **Clients & External Systems** interact with the **API Gateway** via **HTTPS / TLS 1.3**.
* **API Gateway** routes traffic to microservices via **Istio Service Mesh (mTLS / HTTP/2)**.
* **Backend Services** communicate internally using **gRPC** and publish events to **Apache Kafka** via **SASL/SCRAM over TLS**.
* **Backend Services** query data through **Redis Enterprise (TCP)** and **PgBouncer** connecting to **PostgreSQL (TLS 1.3)**.
* **Background Worker** consumes events from **Kafka** and writes cold audit data to **Audit & Archival Store** via **HTTPS**.

## Technology Stack
* **Orchestration:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active high availability.
* **Backend Services:** Java (Spring Boot), Node.js (TypeScript), and Python (FastAPI/Celery) for modular service separation.
* **Data & Caching:** PostgreSQL multi-master with AES-256 encryption and Redis Enterprise for sub-second read performance.
* **Messaging & Mesh:** Apache Kafka for asynchronous decoupling and Istio/Envoy for mTLS transit security.

## Rationale
This hybrid-cloud, microservices-based architecture combines active-active Kubernetes deployment with multi-master PostgreSQL and Redis caching to guarantee 99.99% availability and sub-second EMR performance. Strict encryption at rest (AES-256), mTLS service mesh, and PgBouncer ensure comprehensive HIPAA and GDPR compliance.