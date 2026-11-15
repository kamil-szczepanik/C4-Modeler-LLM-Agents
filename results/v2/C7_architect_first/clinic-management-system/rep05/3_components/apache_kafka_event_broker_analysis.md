## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It relies on a hybrid, high-availability architecture to ensure HIPAA and GDPR compliance.

## Key Elements
- Patients, Clinicians, Hospital Administrators (Users)
- Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateways/Insurance Clearinghouses (External Systems)
- API Gateway (Kong, Nginx, Envoy sidecar)
- Patient Portal Service (Node.js / TypeScript)
- Patient & Scheduling Service (Node.js / TypeScript)
- EMR Service (Java / Spring Boot)
- Billing Service (Python / FastAPI)
- Integration Service (Apache Camel)
- PostgreSQL Databases (PostgreSQL with read replicas)
- Apache Kafka Event Broker (Apache Kafka with KRaft consensus, Schema Registry, and Kafka Connect)
- HashiCorp Vault (HashiCorp Vault)

## Relationships
- Microservices -> Kafka Broker Core: Publishes and consumes partitioned event logs via mTLS [TCP / TLS 1.3]
- Kafka Broker Core -> Schema Registry: Validates message structure against enforced contracts via HTTP/REST over TLS
- Kafka Connect -> Object Storage / Long-Term Archive: Offloads immutable audit and EMR logs via HTTPS / Storage APIs
- External Systems -> Integration Service: Connects via HL7 FHIR APIs

## Technology Stack
- Node.js / TypeScript: Powers lightweight, responsive patient portal and scheduling services
- Java / Spring Boot: Provides robust, enterprise-grade foundation for EMR processing
- Python / FastAPI: Delivers high-performance billing and insurance claim workflows
- Apache Kafka: Enables event-driven messaging with KRaft consensus and Strimzi Kubernetes operator
- PostgreSQL: Ensures reliable relational data storage with read replicas
- HashiCorp Vault: Secures secrets, mTLS certificates, and AES-256 encryption keys

## Rationale
The hybrid architecture utilizes active-active Kubernetes clusters and KRaft-based Kafka brokers to achieve the required 99.99% uptime and low-latency EMR performance. Strict mTLS, AES-256 encryption, and automated long-term archiving ensure full HIPAA and GDPR compliance.