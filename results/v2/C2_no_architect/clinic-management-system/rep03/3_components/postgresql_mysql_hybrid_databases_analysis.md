## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical operations while maintaining strict HIPAA and GDPR compliance across hybrid environments.

## Key Elements
* **Front Desk Staff, Clinicians, Billing Officers, Patients:** End-users interacting via web and mobile interfaces.
* **External Systems:** Lab Systems and Imaging Systems.
* **Containers:** Ingress Controller (Kubernetes Ingress / Istio), Patient Registration Container, Appointment Scheduling Container, EMR Container, Billing & Insurance Claim Container, HL7 FHIR Interoperability Engine.
* **Databases & Storage:** PostgreSQL/MySQL Hybrid Databases, WORM-Compliant Log Storage.

## Relationships
* **Ingress Controller -> Microservices:** Routes external HTTPS/gRPC traffic to internal containers.
* **EMR Container -> PostgreSQL/MySQL Hybrid Databases:** Persists and retrieves encrypted medical records [TCP/AES-256, TLS 1.3 mTLS].
* **Patient Registration Container -> PostgreSQL/MySQL Hybrid Databases:** Persists demographic data [TCP/AES-256, TLS 1.3 mTLS].
* **Appointment Scheduling & Billing Containers -> PostgreSQL/MySQL Hybrid Databases:** Persists schedules and financial transactions [TCP/AES-256, TLS 1.3 mTLS].
* **HL7 FHIR Interoperability Engine -> Lab & Imaging Systems:** Exchanges medical data [HL7 FHIR REST APIs].
* **Databases -> WORM-Compliant Log Storage:** Streams audit logs (`pgaudit`) [Syslog/TLS].

## Technology Stack
* **Orchestration:** Kubernetes (on-prem-k8s and AWS `eu-central-1`) for container management.
* **Databases:** PostgreSQL / MySQL configured with semi-synchronous replication via Patroni/Orchestrator.
* **Security & Secrets:** HashiCorp Vault for dynamic credentials; SPIFFE/SPIRE for workload identity; mTLS (TLS 1.3) for transit encryption.
* **Resiliency & Performance:** PgBouncer for connection pooling; Chaos Mesh for automated failover testing.
* **Interoperability:** HL7 FHIR REST APIs.

## Rationale
This hybrid architecture uses containerized microservices and optimized database replication to meet the 99.99% availability and <1s EMR load requirements. Rigorous security controls—including AES-256, column-level encryption, and WORM storage—ensure strict adherence to HIPAA and GDPR mandates.