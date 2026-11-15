## Overview
This architecture defines the internal components and operational strategies for the Patient & EMR Service within the Clinic Management System. It ensures HIPAA/GDPR compliance, sub-second performance, and 99.99% availability in a hybrid cloud deployment.

## Key Elements
*   **Demographics Controller**: Manages patient registration and attribute-based access control.
*   **EMR Document Manager**: Handles clinical data persistence, structured records, and blob storage.
*   **Audit Interceptor**: Generates cryptographic, tamper-evident audit trails via AspectJ and HSM.
*   **FHIR Resource Mapper**: Transforms domain models using HAPI FHIR libraries for interoperability.
*   **Patroni PostgreSQL Cluster**: Provides high-availability relational data storage.
*   **S3-compatible Tiered Storage**: Enforces 10-year WORM compliance for unstructured records.

## Relationships
*   **API Gateway -> Demographics Controller / EMR Document Manager**: Routes client requests via HTTPS / mTLS (Istio).
*   **Demographics Controller -> Keycloak**: Validates OAuth2/OIDC tokens and attribute-based access control.
*   **EMR Document Manager -> PostgreSQL**: Executes transactional persistence via JDBC / HikariCP.
*   **EMR Document Manager -> S3 Storage**: Streams unstructured clinical objects using AWS SDK v2 over HTTPS.
*   **Service -> Apache Kafka**: Publishes asynchronous clinical events using transactional outbox patterns with SASL/SCRAM and JWE.

## Technology Stack
*   **Java / Spring Boot**: Core container framework ensuring modular component isolation.
*   **Spring Data JPA & Hibernate**: Object-relational mapping for transactional database operations.
*   **HAPI FHIR**: Java library for HL7 FHIR payload transformation and validation.
*   **Apache Kafka & Spring Kafka**: Asynchronous event backbone with transactional outbox support.
*   **PostgreSQL with Patroni**: High-availability relational database with connection pooling.
*   **HashiCorp Vault & AWS KMS**: Secret management and envelope encryption (AES-256).
*   **Istio & Flagger**: Service mesh and automated canary deployments for high availability.

## Rationale
The component-level decomposition separates concerns to meet the strict sub-second P95 performance SLA while maintaining robust security. Dual-storage and transactional outbox patterns guarantee the 10-year WORM retention and zero data loss mandates under high-availability constraints.