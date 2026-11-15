## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for healthcare providers. Its core purpose is to deliver secure, highly available clinical operations while enforcing strict healthcare compliance.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- **Frontend Containers**: WAF Container, API Gateway (Kubernetes Ingress/Gateway), Patient Portal Container
- **Backend Containers**: EMR Container, Scheduling Container, Billing Container, Notification Container, Analytics & Reporting Container
- **Data & Infrastructure**: PostgreSQL Databases (Patroni/etcd), Apache Kafka / RabbitMQ Event Broker, Immutable Audit Storage Sink, HashiCorp Vault

## Relationships
- **Patient Portal Container -> API Gateway**: HTTPS/REST requests [TLS 1.3]
- **EMR Container -> PostgreSQL Databases**: Read/Write patient data [TCP/PostgreSQL Protocol, AES-256]
- **EMR & Billing Containers -> HashiCorp Vault**: Key management and secret retrieval via Vault Agent sidecars [gRPC/mTLS]
- **HashiCorp Vault -> Immutable Audit Storage Sink**: Streams audit logs [Syslog/TCP]
- **External Systems**: Insurance Clearinghouses, External Labs/Imaging Vendors [HL7 FHIR REST APIs]

## Technology Stack
- **Compute**: Kubernetes (on-prem-k8s and AWS `eu-central-1`) for container orchestration and active-active scaling.
- **Security**: HashiCorp Vault with Transit and Database Secrets Engines for AES-256 encryption and dynamic credential generation.
- **Databases**: PostgreSQL managed with Patroni/etcd for high availability.
- **Integration**: HL7 FHIR APIs for interoperability with external medical systems.

## Rationale
This hybrid architecture uses Kubernetes and active-active regional deployment to guarantee 99.99% availability. Integrating HashiCorp Vault with sidecar caching ensures AES-256 encryption and dynamic secrets without degrading EMR screen load performance below the 1-second P95 threshold.