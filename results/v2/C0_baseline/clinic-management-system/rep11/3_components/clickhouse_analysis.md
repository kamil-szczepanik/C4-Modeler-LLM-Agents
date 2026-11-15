## Overview
[A secure, high-performance Clinic Management System built to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA and GDPR compliance with 99.99% high availability across hybrid cloud and on-premises environments.]

## Key Elements
* Patients, Clinicians, Receptionists, Billing Specialists, Hospital Administrators
* External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
* API Gateway (Nginx / Envoy)
* Patient Web/Mobile App (React / Flutter), Clinical Workstation App (Angular / Electron)
* Core Services Container (Java / Spring Boot), Integration Service (Node.js / Apache Camel), Notification Container (Python / Celery), Reporting & Analytics Container (Analytics Platform)
* PostgreSQL (OLTP with AES-256), ClickHouse (OLAP with AggregatingMergeTree and ClickHouse Keeper), Redis, Apache Kafka

## Relationships
* Reporting & Analytics Container -> ClickHouse: Ingests sanitized event streams and queries data using ClickHouse Native Protocol over mTLS [TCP / 9440]
* Core Services Container -> PostgreSQL: Persists transactional data [TCP / SQL via TLS]
* Integration Service -> External Lab & Imaging Systems: Interoperates via HL7 FHIR APIs [HTTPS]
* API Gateway -> Core Services Container: Routes client requests [gRPC / HTTPS]

## Technology Stack
* Java / Spring Boot: Core business logic and domain services for robust enterprise reliability
* PostgreSQL: OLTP database ensuring ACID compliance and AES-256 encryption at rest
* ClickHouse: OLAP columnar database using `AggregatingMergeTree` for sub-second analytical queries
* ClickHouse Keeper: Replicated consensus module managing cluster coordination without WAN bottlenecks
* Apache Kafka: Event streaming backbone for asynchronous service communication

## Rationale
[This hybrid architecture guarantees 99.99% availability and meets a 10-year data retention mandate by separating OLTP and OLAP workloads. It strictly enforces HIPAA and GDPR compliance through mTLS, AES-256 encryption, and pre-aggregated datamarts.]