## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient EMRs, scheduling, and billing for healthcare facilities. It ensures 99.99% availability and strict HIPAA/GDPR compliance through a microservices-based, zero-trust architecture.

## Key Elements
*   **Users:** Clinical Staff, Patients, Auditors.
*   **Gateways:** Clinical API Gateway (Go), Patient-Facing API Gateway (Node.js/TypeScript).
*   **Services:** EMR/Scheduling Services (Java/Spring Boot), Reporting & Compliance Service, Audit Logging Sidecar.
*   **Infrastructure:** Kubernetes (Hybrid: On-prem/AWS), NATS/Kafka Message Broker, PostgreSQL Cluster (w/ Patroni), Redis Cache.
*   **Security:** Istio Service Mesh, HSM/KMS, WORM Storage.

## Relationships
*   **Service Communication:** mTLS-encrypted via Istio; asynchronous event-driven messaging via NATS/Kafka.
*   **Data Persistence:** PostgreSQL with synchronous replication; Redis for sub-second EMR retrieval.
*   **Compliance:** Audit Sidecars stream to WORM storage; Reporting Service accesses read-only replicas with dynamic data masking.
*   **Deployment:** GitOps via ArgoCD; automated HPA based on latency/queue depth metrics.

## Technology Stack
*   **Languages:** Java/Spring Boot (Domain logic), Go (Clinical Gateway), Node.js (Patient Gateway).
*   **Orchestration:** Kubernetes (Hybrid) with Istio Service Mesh.
*   **Data:** PostgreSQL (ACID compliance), Redis (Caching), NATS/Kafka (Event-driven decoupling).
*   **Security:** AES-256 at-rest, FIPS 140-2 HSM, OIDC tokens, mTLS.

## Rationale
The microservices architecture ensures horizontal scalability and fault isolation, critical for maintaining 99.99% availability in a hybrid environment. Decoupling transactional clinical paths from analytical reporting via message brokers and read-only replicas guarantees P95 latency targets for patient care.