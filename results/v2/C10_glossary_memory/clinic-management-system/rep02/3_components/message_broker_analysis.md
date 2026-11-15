## Overview
The Clinic Management System is an asynchronous, high-availability healthcare platform designed to manage patient admissions, electronic medical records, scheduling, and billing. It ensures secure clinical workflows and meets stringent 10-year data retention mandates across a hybrid cloud topology.

## Key Elements
- **Users**: Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App
- **Containers**: Unified API Gateway, Patient Registration Microservice, EMR Microservice, Scheduling Microservice, Billing Microservice, Async Claims Processing Worker, Message Broker (Apache Kafka), Distributed Cache (Redis Enterprise), Cloud-Native Distributed SQL Database (CockroachDB)
- **Message Broker Components**: Topic Manager, Access Control & Encryption Manager, Schema Registry, Broker Health & Metrics Exporter, Data Retention & Tiered Storage Manager, In-Transit Data Masking & Tokenization, Broker Audit & Compliance Logger

## Relationships
- Patient Portal / Mobile App -> Unified API Gateway (HTTPS / REST and WebSocket via OIDC/OAuth 2.0)
- Front-Desk Receptionists / Clinicians / Billing Specialists / IT/Compliance Administrators -> Unified API Gateway (HTTPS / REST)
- Unified API Gateway -> Microservices (HTTP / REST and gRPC)
- Microservices -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Billing Microservice & EMR Microservice -> Message Broker (Apache Kafka Protocol / mTLS)
- Clinic Management System -> Lab & Imaging Systems (HL7 FHIR over HTTPS)
- Clinic Management System -> Insurance Clearinghouses (Secure EDI / HTTPS APIs)
- Clinic Management System -> Identity Provider (IdP) (OIDC/SAML 2.0 over HTTPS)
- on-prem-k8s -> eu-central-1 (Encrypted IPsec site-to-site VPN and mutual TLS)

## Technology Stack
- **API Gateway**: Unified API Gateway with TLS 1.3 for secure ingress and rate-limiting
- **Microservices**: Spring Boot (Patient Registration, Scheduling), Go / gRPC (EMR), Node.js / Express (Billing)
- **Message Broker**: Apache Kafka with Confluent Schema Registry and Kafka ACLs for asynchronous event-driven processing
- **Database**: CockroachDB (Cloud-Native Distributed SQL) utilizing Raft consensus for zero-downtime availability and 10-year retention
- **Caching & State**: Redis Enterprise for distributed session state and WebSocket messaging
- **Security & Compliance**: AES-256 encryption at rest, mTLS, SASL/SCRAM-512, and in-transit data masking for HIPAA/GDPR compliance

## Rationale
This architecture uses an event-driven Kafka broker combined with a distributed SQL database to decouple heavy integrations and isolate external latency, guaranteeing sub-second EMR load times and 99.99% uptime. The hybrid deployment with strict encryption and audit logging fulfills rigorous healthcare compliance and data retention regulations.