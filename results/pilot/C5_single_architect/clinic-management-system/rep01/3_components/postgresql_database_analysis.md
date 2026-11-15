## Overview
The Clinic Management System is a hybrid cloud clinical IT platform managing patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- Clinic Staff and Patients (Users)
- Single Page Application (React)
- API Gateway (OAuth2/OIDC)
- Microservices: Patient Management, EMR, Scheduling, Billing (Kubernetes)
- HL7 FHIR Integration Container (Apache Camel)
- PostgreSQL Database with Patroni Cluster & `pgAudit`
- Redis Cache, Elasticsearch Audit Trail, Apache Kafka
- External Systems: Insurance Gateways, Lab/Imaging Systems, Identity Provider

## Relationships
- Single Page Application -> API Gateway: HTTPS/REST
- API Gateway -> Microservices: gRPC / HTTPS
- Microservices -> PostgreSQL Database: PostgreSQL Wire Protocol over TLS 1.3
- HL7 FHIR Integration Container -> External Lab/Imaging Systems: HL7 FHIR over HTTPS
- Microservices -> Apache Kafka: AMQP / TCP

## Technology Stack
- React: Powers the responsive frontend user interface.
- Kubernetes: Orchestrates containerized microservices across hybrid environments (`on-prem-k8s` and `eu-central-1`).
- PostgreSQL with Patroni: Ensures active-active high availability (99.99%) and data persistence.
- Apache Camel: Facilitates HL7 FHIR interoperability with external medical systems.
- Elasticsearch: Stores immutable audit trails for compliance.
- AES-256 and TLS 1.3: Enforces encryption at rest and in transit for HIPAA/GDPR compliance.

## Rationale
This hybrid architecture combines containerized microservices with a Patroni-managed PostgreSQL cluster to guarantee 99.99% uptime and strict regulatory compliance. Dedicated domain schemas, TLS 1.3, and AES-256 encryption secure sensitive clinical data across distributed cloud and on-premise environments.