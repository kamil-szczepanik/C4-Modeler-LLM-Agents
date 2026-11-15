## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to provide highly available, secure, and interoperable clinical IT operations complying with HIPAA and GDPR regulations.

## Key Elements
* Patients, Clinicians, Receptionists, Billing Specialists, Hospital Administrators
* External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
* API Gateway (Nginx / Envoy)
* Patient Web/Mobile App (React / Flutter)
* Clinical Workstation App (Angular / Electron)
* Core Services Container (Java / Spring Boot)
* Integration Service (Node.js / Apache Camel)
* Notification Container (Python / Celery)
* Reporting & Analytics Container (Analytics Platform)
* PostgreSQL (OLTP with AES-256)
* ClickHouse (OLAP)
* Redis
* Apache Kafka Container (Strimzi Operator managed)
  * Kafka Broker Cluster (Java/Scala)
  * Schema Registry (Java/Confluent)
  * Kafka Connect (Java)

## Relationships
* Core Services Container -> Schema Registry: Validates event schemas prior to publishing [HTTP/REST over TLS 1.3]
* Core Services Container -> Kafka Broker Cluster: Publishes encrypted EMR and patient events (`acks=all`) [Kafka Protocol / mTLS]
* Kafka Broker Cluster -> Kafka Connect: Streams raw events to persistent sinks [Kafka Protocol]
* Kafka Connect -> PostgreSQL / ClickHouse: Offloads sanitized historical data for 10-year retention [JDBC / Native Drivers over TLS 1.3]
* Patient Web/Mobile App -> API Gateway: Accesses patient registration and scheduling [HTTPS / REST]
* Clinical Workstation App -> API Gateway: Manages EMR and patient workflows [HTTPS / REST / WebSocket]
* Integration Service -> External Lab & Imaging Systems: Exchanges health data [HL7 FHIR REST APIs]

## Technology Stack
* Kubernetes (Strimzi Operator): Orchestrates container workloads across on-prem-k8s and eu-central-1 for high availability.
* Apache Kafka: Manages asynchronous event-driven microservices decoupling with `acks=all` and MirrorMaker 2.
* Java / Spring Boot: Powers core clinical and business logic services.
* PostgreSQL & ClickHouse: Provides persistent OLTP and OLAP storage with AES-256 encryption at rest.
* Redis: Handles fast caching and session state management.
* TLS 1.3 & SASL/OAUTHBEARER: Secures inter-broker, client communications, and IdP-integrated authentication.

## Rationale
This architecture uses an active-active hybrid cloud deployment combined with robust event-driven decoupling via Apache Kafka to guarantee 99.99% uptime and low-latency EMR performance. Strict data isolation, mTLS, AES-256 encryption, and Kafka Connect offloading ensure comprehensive HIPAA and GDPR compliance with a 10-year data retention capability.