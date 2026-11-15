## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for clinical environments. It ensures 99.99% availability and HIPAA/GDPR compliance across hybrid cloud infrastructure.]

## Key Elements
- Patients, Clinicians, Billing Admins
- API Gateway (Kong / Nginx on Kubernetes)
- Web Application (React / Next.js)
- Patient & Scheduling, EMR, Billing, and Integration Microservices (Node.js / Spring Boot on Kubernetes)
- Event Broker (Apache Kafka via Strimzi operator)
- PostgreSQL Database (Multi-AZ)
- WORM Audit Log Store with HSM-backed KMS
- Identity Provider (IdP) & External Lab/Imaging Systems

## Relationships
- Web Application -> API Gateway: HTTPS/REST and WebSockets
- API Gateway -> Microservices: gRPC and REST over Istio Service Mesh (mTLS)
- Microservices -> Event Broker: Kafka Protocol (SASL/SCRAM over mTLS, TLS 1.3)
- Integration Service -> External Systems: HL7 FHIR APIs over HTTPS
- Microservices -> PostgreSQL: TCP/Postgres Protocol (TLS)

## Technology Stack
- Kubernetes / Strimzi: Orchestration and Kafka deployment for high availability (99.99%)
- Apache Kafka: Asynchronous event messaging with KRaft, `acks=all`, and `min.insync.replicas=2`
- PostgreSQL: Relational persistence with multi-AZ replication
- WORM Storage + HSM-backed KMS: Immutable audit logging meeting strict 10-year retention rules
- Istio Service Mesh (SPIFFE/SPIRE): Zero-trust security, mTLS, and automated 24-hour certificate rotation

## Rationale
[This hybrid architecture uses Kafka and multi-AZ Kubernetes for active-active high availability and rapid disaster recovery. Strict client-side encryption and WORM storage fulfill rigorous HIPAA and GDPR compliance mandates.]