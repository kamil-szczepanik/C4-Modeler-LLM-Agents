## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers.]
[It uses a hybrid architecture designed for HIPAA/GDPR compliance, 99.99% availability, and a 10-year data retention mandate.]

## Key Elements
* Patients, Receptionists, Physicians, Billing Specialists
* API Gateway (Go)
* Patient Portal Frontend (Node.js)
* Physician EMR Frontend (React)
* EMR Backend (Java Spring Boot)
* Billing Service (Python)
* Event Broker (Apache Kafka with KRaft mode)
* Schema Registry (Quarkus)
* Kafka Connect & Strimzi Operator
* Database (PostgreSQL & WORM Storage)
* External Systems: Payment Gateways, Lab/Imaging Systems, Enterprise IDP

## Relationships
* API Gateway -> EMR Backend: Routes REST/GraphQL requests [HTTPS, TLS 1.3]
* EMR Backend -> Event Broker: Publishes and consumes clinical events [TCP, TLS 1.3, SCRAM-SHA-512]
* Billing Service -> Event Broker: Publishes and consumes billing events [TCP, TLS 1.3, SCRAM-SHA-512]
* Event Broker -> WORM Storage: Persists immutable audit logs [TLS 1.3, AES-256]
* Event Broker (on-prem-k8s) <-> Event Broker (AWS eu-central-1): Cross-cluster replication [MirrorMaker 2, mTLS]

## Technology Stack
* Apache Kafka (KRaft mode): Asynchronous messaging and backpressure handling for high throughput
* Strimzi Operator: Declarative Kubernetes cluster lifecycle management
* Quarkus Schema Registry: Enforces Avro-based payload validation against HL7 FHIR standards
* PostgreSQL & WORM Storage: Structured data persistence and 10-year regulatory audit compliance
* TLS 1.3 & mTLS: Encrypts data in transit across hybrid components
* SCRAM-SHA-512 & ACLs: Enforces strict broker-client authentication and least-privilege access
* AES-256: Encrypts persistent volumes at rest for HIPAA compliance

## Rationale
[The hybrid architecture utilizes active-active Kafka replication across on-premise Kubernetes and AWS to meet the 99.99% availability requirement.]
[Robust encryption, immutable storage, and schema validation ensure strict HIPAA and GDPR compliance while maintaining high-performance clinical data exchange.]