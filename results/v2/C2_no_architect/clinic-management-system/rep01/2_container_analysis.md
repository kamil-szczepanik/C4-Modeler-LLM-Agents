## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely handle patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
* **Users:** Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
* **External Systems:** Insurance Clearinghouses, External Labs/Imaging Vendors
* **Containers:** API Gateway, Patient Portal Container, EMR Container, Scheduling Container, Billing Container, Notification Container, Analytics & Reporting Container, WAF Container
* **Infrastructure/Data:** On-Premises Kubernetes Cluster, AWS (eu-central-1), PostgreSQL Databases (Patroni/etcd), Kafka/RabbitMQ Event Broker, Immutable Audit Storage Sink, HashiCorp Vault

## Relationships
* **Patients/Users to API Gateway / WAF:** HTTPS (TLS 1.3), OAuth2/OIDC, Multi-Factor Authentication
* **Containers to Containers:** mTLS via SPIFFE/SPIRE, gRPC / REST APIs
* **Core Containers to Event Broker:** Asynchronous message publishing/consuming via Apache Kafka / RabbitMQ
* **Containers to External Systems:** Secure HTTPS REST APIs and HL7 FHIR protocols for lab, imaging, and insurance clearinghouses
* **Databases to Storage:** Active-Passive replication with field-level encryption for PHI

## Technology Stack
* **Orchestration:** Kubernetes (hybrid on-prem and AWS eu-central-1) for container management
* **Deployment:** ArgoCD (GitOps) for repeatable, audit-compliant deployments
* **Security & Auth:** OAuth2/OIDC, SPIFFE/SPIRE for mTLS, HashiCorp Vault for hardware-backed AES-256 key management
* **Messaging:** Apache Kafka or RabbitMQ for asynchronous, decoupled event-driven integration
* **Database:** PostgreSQL with Patroni/etcd for high-availability active-passive clustering
* **Interoperability:** HL7 FHIR APIs for standardized healthcare data exchange

## Rationale
The hybrid architecture balances strict HIPAA/GDPR data residency mandates with high availability (99.99%) through an active-passive regional database topology. Field-level PHI encryption and strict container segmentation protect sensitive health data without sacrificing the sub-second EMR performance required by clinicians.