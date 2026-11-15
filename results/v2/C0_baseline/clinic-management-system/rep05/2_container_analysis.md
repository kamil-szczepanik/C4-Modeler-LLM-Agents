## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It provides secure, highly available clinical IT capabilities while maintaining strict HIPAA and GDPR compliance across a hybrid cloud environment.

## Key Elements
* **Users:** Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist
* **External Systems:** Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouses, Payment Gateway, Centralized Vault, SIEM / Observability System
* **Containers:** API Gateway (NGINX / Kong), Web Application (React SPA), Core Services (Spring Boot / Java), Billing Service (Node.js / Express), Integration Service (Apache Camel)
* **Data & Infrastructure Tier:** PostgreSQL with Citus, Redis, Kafka/RabbitMQ message brokers, Istio service mesh, ArgoCD

## Relationships
* **Patient/Clinician to API Gateway:** HTTPS / WSS with TLS 1.3, OAuth2 token validation, and multi-factor authentication
* **API Gateway to Web Application:** Serves React SPA via NGINX
* **Web Application to Core Services:** gRPC over mTLS (Istio) for sub-second EMR interactions
* **Core Services to Billing & Integration Services:** Asynchronous event streaming via Kafka/RabbitMQ with payload-level message encryption
* **Integration Service to External Systems:** HL7 FHIR APIs for lab and imaging systems
* **Billing Service to External Systems:** Secure external calls to Payment Gateways and Insurance Clearinghouses
* **All Containers to Infrastructure:** Dynamic secrets fetching from Centralized Vault via AppRole tokens; OpenTelemetry tracing to SIEM

## Technology Stack
* **Frontend:** React SPA served via NGINX for high-performance UI rendering
* **Backend Core:** Spring Boot / Java for patient, scheduling, and EMR bounded contexts
* **Backend Services:** Node.js / Express for billing and insurance claim workflows
* **Integration:** Apache Camel for HL7 FHIR translation
* **Database & Caching:** PostgreSQL with Citus and Redis, featuring column-level AES-256 encryption at rest
* **Messaging:** Kafka / RabbitMQ with dead-letter queues for asynchronous decoupling
* **Orchestration & Security:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`), Istio service mesh, ArgoCD, and OpenTelemetry

## Rationale
This hybrid architecture uses regional primary databases, asynchronous messaging, and rigorous network segmentation to guarantee 99.99% availability and sub-second EMR performance. It embeds defense-in-depth security controls—including mTLS, message-level encryption, and dynamic vault secrets—to ensure strict HIPAA and GDPR compliance.