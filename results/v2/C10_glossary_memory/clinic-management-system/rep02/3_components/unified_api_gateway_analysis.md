## Overview
The Clinic Management System is a hybrid cloud healthcare platform designed to handle patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability (99.99%), strict regulatory compliance (HIPAA and GDPR), and interoperability with external clinical systems.

## Key Elements
- Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients
- Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App
- Unified API Gateway (API Gateway, TLS 1.3)
- Patient Registration Microservice (Spring Boot)
- EMR Microservice (Go / gRPC)
- Scheduling Microservice (Spring Boot)
- Billing Microservice (Node.js / Express)
- Async Claims Processing Worker (Background Worker)
- Message Broker (Apache Kafka)
- Distributed Cache (Redis Enterprise)
- Cloud-Native Distributed SQL Database (CockroachDB)

## Relationships
- Patient Portal / Mobile App -> Unified API Gateway (HTTPS / REST and WebSocket via OIDC/OAuth 2.0)
- Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators -> Unified API Gateway (HTTPS / REST)
- Unified API Gateway -> Patient Registration Microservice, Scheduling Microservice, Billing Microservice (HTTP / REST)
- Unified API Gateway -> EMR Microservice (gRPC)
- Microservices -> Cloud-Native Distributed SQL Database (SQL / TLS)
- Billing Microservice <-> Message Broker <-> Async Claims Processing Worker (Apache Kafka Protocol)
- Clinic Management System -> Lab & Imaging Systems (HL7 FHIR over HTTPS)
- Clinic Management System -> Insurance Clearinghouses (Secure EDI / HTTPS APIs)
- Clinic Management System -> Identity Provider (IdP) (OIDC/SAML 2.0)
- on-prem-k8s -> eu-central-1 (Encrypted IPsec VPN and mTLS)

## Technology Stack
- Unified API Gateway: Kong/Envoy with Lua/Wasm plugins for zero-trust token validation and routing
- Microservices Backend: Spring Boot (Java), Go (gRPC for high-performance EMR), Node.js / Express
- Messaging: Apache Kafka for asynchronous claims processing
- Storage: CockroachDB for distributed SQL storage with Raft consensus and Redis Enterprise for caching/sessions
- Security & Interoperability: TLS 1.3, mTLS via service mesh, OAuth 2.0 / OIDC, HL7 FHIR over HTTPS

## Rationale
The hybrid architecture utilizes active-active Kubernetes deployments across on-premises clusters and AWS eu-central-1 to guarantee 99.99% uptime and low-latency clinical access. CockroachDB and Kafka ensure fault-tolerant 10-year data retention and zero-loss asynchronous processing required by healthcare regulations.