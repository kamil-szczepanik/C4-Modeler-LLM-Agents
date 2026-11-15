## Overview
The Audit & Compliance Service is a Spring Boot component of the Clinic Management System that ensures strict HIPAA and GDPR compliance through real-time event ingestion and immutable logging. It provides automated anomaly detection, compliance reporting, and secure 10-year data retention for healthcare institutions.

## Key Elements
- **Audit Event Ingestion Engine**: Spring Integration Kafka consumer handling real-time audit streams with a Dead-Letter Queue.
- **Compliance Rules Engine**: Drools/Java policy evaluator for detecting EMR access anomalies and tenant-specific threshold alerts.
- **Audit Query & Reporting API**: Spring MVC REST interface serving compliance dashboards to the React SPA Frontend.
- **Retention & Archival Manager**: Batch scheduler enforcing the $\ge$ 10-year data retention and WORM offloading policy.
- **Report Generation Service**: Apache PDFBox/Thymeleaf service for asynchronous generation of PDF/CSV compliance exports.
- **Object Storage Gateway**: Interface managing AWS S3 storage with Object Lock configuration.
- **PostgreSQL Database**: Patroni-managed relational database with AES-256 encryption at rest.

## Relationships
- EMR Core Service & Billing Service -> Audit Event Ingestion Engine: Sends audit events [gRPC over mTLS with eBPF routing]
- Audit Event Ingestion Engine -> Apache Kafka: Consumes streaming audit events [TCP]
- Audit Event Ingestion Engine & Compliance Rules Engine -> PostgreSQL: Writes immutable logs and queries access patterns [JDBC over TLS with AES-256]
- Audit Query & Reporting API -> SPA Frontend: Serves dashboard data [HTTPS]
- Retention & Archival Manager -> Object Storage Gateway: Offloads aged logs to WORM storage [HTTPS / S3 API with SigV4]
- Report Generation Service -> SPA Frontend: Delivers generated reports via download links [HTTPS]

## Technology Stack
- **Java / Spring Boot**: Core runtime framework for enterprise reliability and service modularity.
- **Apache Kafka**: Event streaming backbone ensuring decoupled, high-throughput audit event ingestion.
- **PostgreSQL with Patroni**: Primary-replica relational storage guaranteeing secure, encrypted active-active data persistence.
- **AWS S3 Object Lock**: WORM-compliant cloud object storage ensuring tamper-proof retention for regulatory compliance.
- **Apache PDFBox**: Asynchronous generation engine for scheduled and ad-hoc compliance report exports.

## Rationale
This architecture uses asynchronous ingestion, decoupling, and automated storage tiering to maintain 99.99% system availability without impacting primary clinical workflows. It guarantees regulatory compliance by combining encryption, WORM storage, and strict 10-year data retention policies.