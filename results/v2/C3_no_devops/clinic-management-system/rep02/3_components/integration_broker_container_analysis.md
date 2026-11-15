## Overview
The Clinic Management System is a hybrid cloud platform built for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% uptime, and secure interoperability with external clinical systems.

## Key Elements
- **Users**: Patient, Clinical Staff, Administrative Staff, Compliance Officer / Auditor
- **External Systems**: Payment Gateway, Insurance Clearinghouse, External Lab / Imaging Systems, Pharmacy Management System
- **Containers**: API Gateway (Kong / Nginx), Patient Self-Service Container (React / Next.js SPA), EMR Backend Container (Node.js / Java Spring Boot), Scheduling & Resource Engine Container (Java Spring Boot), Integration Broker Container (Apache Camel / Node-RED), Audit & Compliance Daemon Container (Go), EMR Database (PostgreSQL with RLS), Redis Cluster, Cold Storage, Apache Kafka
- **Integration Broker Internal Components**: Route Orchestrator (Apache Camel Context), Data Transformer Engine, DLQ & Retry Manager, Broker Management API

## Relationships
- API Gateway -> Integration Broker Container: Routes integration requests [Internal mTLS over gRPC/REST]
- Integration Broker Container -> External Lab / Imaging Systems: Exchanges diagnostic results [HL7 FHIR APIs over gRPC/REST]
- Integration Broker Container -> Pharmacy Management System: Exchanges electronic prescriptions [HL7 FHIR APIs over gRPC/REST]
- Integration Broker Container -> Payment Gateway: Processes billing transactions [HTTPS / REST]
- Integration Broker Container -> Insurance Clearinghouse: Verifies insurance and submits claims [HTTPS / REST]
- Route Orchestrator -> Data Transformer Engine: Transforms payloads [In-memory Java method call]
- Route Orchestrator -> DLQ & Retry Manager: Forwards failed transactions [Kafka Producer / Internal Topic]

## Technology Stack
- **Kubernetes / Hybrid Cloud (on-prem-k8s, eu-central-1)**: Ensures active-active high availability (99.99%) and flexible deployment.
- **Apache Camel / Kafka**: Powers enterprise integration patterns, message routing, and reliable dead-letter queue (DLQ) processing.
- **PostgreSQL with RLS / AES-256**: Secures relational data at rest with strict row-level security and compliance standards.
- **HL7 FHIR / gRPC / REST**: Provides interoperability and low-latency internal/external communication.

## Rationale
This hybrid architecture combines containerized microservices with robust message brokers to meet stringent HIPAA/GDPR compliance and high-availability requirements. Decoupled integration and storage layers ensure sub-second EMR performance while supporting 10-year data retention and seamless external interoperability.