## Overview
The Clinic Management System is a hybrid cloud platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. Its core purpose is to provide a highly available, secure, and interoperable clinical IT infrastructure complying with HIPAA and GDPR regulations.

## Key Elements
* **Users:** Patients, Clinical Staff, Administrative & Billing Staff, Hospital IT / Compliance Officers
* **External Systems:** Identity Provider, Third-Party Payment Gateway, External Lab & Imaging Systems
* **Containers:** API Gateway (Kong / Envoy / Istio), EMR & Scheduling Service (Java Spring Boot / Node.js NestJS), Billing & Claims Service (Java Spring Boot), Integration Engine (HAPI FHIR), Data Tier (PostgreSQL), Event Broker (Apache Kafka)
* **Integration Engine Components:** FHIR Endpoint API (Java / HAPI FHIR JPA Server), Transformation & Mapping (Apache Camel), Outbound Dispatcher (Spring Integration), Provenance & Audit Interceptor, Metrics Exporter (Micrometer / Prometheus)

## Relationships
* **EMR & Scheduling Service -> FHIR Endpoint API:** Synchronous clinical data sync [gRPC / mTLS]
* **Transformation & Mapping -> FHIR Endpoint API:** Persists normalized resources [JDBC / TLS]
* **FHIR Endpoint API -> Data Tier (PostgreSQL):** Persists FHIR resources and metadata [JDBC / TLS 1.3]
* **Outbound Dispatcher -> External Lab & Imaging Systems:** Dispatches outbound payloads [HTTPS / mTLS with HashiCorp Vault certificates]
* **Integration Engine -> External Lab & Imaging Systems:** Exchanges lab results and medical imaging [HL7 FHIR APIs]

## Technology Stack
* **Kubernetes (on-prem-k8s & eu-central-1):** Hybrid cloud infrastructure ensuring 99.99% active-active uptime.
* **Istio Service Mesh:** Enforces mTLS across container boundaries and manages OAuth2/JWT scope validation.
* **Java Spring Boot & HAPI FHIR:** Powers the EMR, Billing, and FHIR Endpoint API components for robust healthcare standards support.
* **Apache Camel & Spring Integration:** Handles legacy protocol translation and reliable outbound message dispatching.
* **Apache Kafka:** Manages asynchronous queuing and Dead-Letter Queue (DLQ) handling for clinical continuity.
* **PostgreSQL:** Provides encrypted (AES-256) relational data storage for persistent medical and administrative records.
* **HashiCorp Vault:** Securely manages dynamic API keys and mTLS client certificates.

## Rationale
This hybrid microservices architecture leverages cloud-native technologies like Kubernetes, Kafka, and Istio to guarantee high availability and sub-second P95 performance required for critical clinical workflows. Strict adherence to security standards—including mTLS, AES-256 storage, and HL7 FHIR interoperability—ensures total HIPAA and GDPR compliance without sacrificing scalability.