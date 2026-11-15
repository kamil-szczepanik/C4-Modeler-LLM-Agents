## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It ensures high availability, 10-year data retention, and strict HIPAA and GDPR compliance.]

## Key Elements
* Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
* React Single-Page Application (SPA) / React Native Mobile Client
* Envoy API Gateway / Edge Proxy
* EMR & Scheduling Service, Billing & Claims Service, FHIR Interoperability Service
* PostgreSQL Databases, Apache Kafka / RabbitMQ Message Brokers
* AWS S3 / WORM Object Storage, HashiCorp Vault

## Relationships
* Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors -> React SPA / Mobile Client via HTTPS
* React SPA / Mobile Client -> Envoy API Gateway / Edge Proxy via HTTPS / TLS 1.3 with OAuth2/OIDC
* Services -> PostgreSQL Databases via encrypted TCP
* Services -> Apache Kafka / RabbitMQ via AMQP/TCP
* Services -> AWS S3 / WORM Storage via HTTPS

## Technology Stack
* React & React Native: Cross-platform web and mobile UI rendering
* Node.js / Java & Spring Boot: Backend services for low-latency EMR and billing operations
* HAPI FHIR: Healthcare interoperability for lab and imaging systems
* PostgreSQL & SQLCipher/SQLite: Relational data storage with AES-256 encryption at rest
* Apache Kafka / RabbitMQ: Asynchronous messaging for system decoupling
* AWS S3 WORM Storage: Immutable long-term data retention

## Rationale
[A hybrid cloud infrastructure with regional PostgreSQL databases and active-active routing meets the 99.99% availability requirement. Containerized Java and Node.js microservices integrated with HAPI FHIR ensure rapid performance and seamless regulatory interoperability.]