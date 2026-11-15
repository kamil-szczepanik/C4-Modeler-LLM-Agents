## Overview
The Clinic Management System is a hybrid cloud, high-availability platform designed to handle patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It ensures strict HIPAA and GDPR compliance while maintaining 99.99% uptime and sub-second EMR response times.

## Key Elements
* **Users:** Patients, Clinicians, Administrative Staff, Billing Officers, Regulatory Auditors
* **External Systems:** Enterprise Identity Provider, External Lab and Imaging Systems, Payment Gateway and Insurance Clearinghouse, Audit Archive
* **API Gateway:** Kong / Nginx
* **Frontend Container:** Next.js / Node.js (Patient Portal BFF)
* **Clinical Core Container:** Node.js / Java Spring Boot
* **Scheduling & Resource Engine:** Python / Go with Redis
* **Interoperability Service:** Apache Camel / HAPI FHIR
* **Billing & Claims Worker:** .NET Core with RabbitMQ
* **Analytics & Reporting Container:** Apache Superset / Metabase backed by ClickHouse and Read-Only PostgreSQL Replica via Debezium CDC

## Relationships
* **Patients/Staff -> API Gateway:** HTTPS / REST, OAuth2/OIDC with MFA
* **Patient Portal BFF -> API Gateway:** HTTPS / REST
* **API Gateway -> Clinical Core / Scheduling / Interoperability:** mTLS / gRPC / REST
* **Clinical Core -> PostgreSQL:** TCP with AES-256
* **Clinical Core -> Debezium CDC -> Analytics Store:** Kafka / TCP with mTLS
* **Billing Worker -> Payment Gateway & Insurance Clearinghouse:** HTTPS / REST with strict egress filtering
* **Clinical Core -> Audit Archive:** Cryptographically signed audit logs via secure TCP

## Technology Stack
* **API Gateway:** Kong / Nginx for centralized routing and mTLS/OAuth2 enforcement
* **Core Backend:** Java Spring Boot / Node.js for robust transactional handling
* **Scheduling:** Redis for real-time resource locking and clash checks
* **Interoperability:** Apache Camel / HAPI FHIR for HL7 FHIR standard compliance
* **Messaging & CDC:** RabbitMQ for asynchronous billing; Debezium and Kafka for real-time data replication
* **Databases:** PostgreSQL with AES-256 at rest, ClickHouse for analytics

## Rationale
Decoupling the Billing Worker and Analytics containers protects core clinical EMR performance (<1s P95) and ensures uptime during external clearinghouse outages. Zero-trust network boundaries, mTLS, and AES-256 encryption satisfy strict HIPAA, GDPR, and 10-year audit retention mandates.