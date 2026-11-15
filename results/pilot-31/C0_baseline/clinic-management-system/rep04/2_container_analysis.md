## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, scheduling, and billing for clinical environments. It ensures high availability and regulatory compliance through a microservices architecture.

## Key Elements
*   **Frontends:** Patient Portal (React/Next.js), Administrative Dashboard (Angular)
*   **Services:** Core EMR Service (Spring Boot), Billing Service (Go), Audit Visualization Service, Read-Only Analytics Service
*   **Infrastructure:** Kubernetes (On-prem/AWS), Istio Service Mesh, HashiCorp Vault
*   **Data Layer:** PostgreSQL (CloudNativePG), Immutable Ledger Database, ClickHouse (Analytics)
*   **Integration:** Debezium (CDC), Spring Cloud Gateway, GSLB

## Relationships
*   **Frontend-to-Backend:** REST/gRPC via Spring Cloud Gateway with OIDC/OAuth2 MFA.
*   **Service-to-Service:** mTLS-encrypted communication managed by Istio service mesh.
*   **Data Synchronization:** Debezium CDC connectors stream transactional data from PostgreSQL to Analytics/Audit stores.
*   **External Interoperability:** HL7 FHIR APIs for lab and imaging system integration.
*   **Traffic Management:** GSLB handles failover between on-prem Kubernetes and AWS regions.

## Technology Stack
*   **Spring Boot/Go:** Chosen for high-concurrency performance and modularity.
*   **PostgreSQL/ClickHouse:** PostgreSQL for transactional integrity; ClickHouse for high-performance analytical reporting.
*   **Istio:** Implements Zero Trust security and mTLS across hybrid-cloud boundaries.
*   **HashiCorp Vault:** Centralized management of dynamic, short-lived secrets.
*   **Debezium:** Enables decoupled, real-time data streaming for audit and analytics.

## Rationale
This architecture uses microservices and CDC to decouple heavy analytical/audit workloads from the transactional EMR, ensuring sub-second P95 performance for clinical staff. The hybrid-cloud deployment with GSLB and Istio provides the 99.99% availability and Zero Trust security required for HIPAA/GDPR compliance.