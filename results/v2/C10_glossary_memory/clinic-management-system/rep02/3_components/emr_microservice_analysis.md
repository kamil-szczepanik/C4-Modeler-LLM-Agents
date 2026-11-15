## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It delivers high availability, rigorous compliance, and interoperability across hybrid cloud environments.

## Key Elements
- Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients
- Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App
- Unified API Gateway, Patient Registration Microservice, EMR Microservice, Scheduling Microservice, Billing Microservice
- Async Claims Processing Worker, Message Broker (Apache Kafka), Distributed Cache (Redis Enterprise), Cloud-Native Distributed SQL Database (CockroachDB)

## Relationships
- Patient Portal / Mobile App -> Unifiedational API Gateway via HTTPS / REST and WebSocket (OIDC/OAuth 2.0)
- Unified API Gateway -> EMR Microservice via gRPC (TLS 1.3)
- EMR Microservice -> Cloud-Native Distributed SQL Database via SQL / TLS
- Billing Microservice -> Message Broker via Apache Kafka Protocol
- Clinic Management System -> Lab & Imaging Systems via HL7 FHIR over HTTPS

## Technology Stack
- Go / gRPC: Used for the EMR Microservice to achieve < 1 s P95 screen load performance.
- Spring Boot: Used for Patient Registration and Scheduling microservices for robust enterprise support.
- Node.js / Express: Used for the Billing Microservice for rapid integration development.
- Apache Kafka: Implements asynchronous messaging for claims processing.
- CockroachDB: Distributed SQL database ensuring Raft consensus, zero-downtime availability, and 10-year retention.
- Redis Enterprise: Provides distributed caching and session state.

## Rationale
This hybrid architecture combines secure, low-latency microservices with robust distributed data storage to satisfy strict HIPAA, GDPR, and 99.99% availability requirements. It balances clinical workflow speed with enterprise-grade security and interoperability.