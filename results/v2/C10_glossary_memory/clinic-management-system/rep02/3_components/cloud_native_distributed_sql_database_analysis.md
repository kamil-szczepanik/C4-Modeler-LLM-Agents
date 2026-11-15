## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability and HIPAA/GDPR compliance across a hybrid cloud infrastructure.

## Key Elements
- **Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients** [People]
- **Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App** [External Systems]
- **Unified API Gateway** (API Gateway, TLS 1.3) [Container]
- **Patient Registration Microservice** (Spring Boot), **EMR Microservice** (Go / gRPC), **Scheduling Microservice** (Spring Boot), **Billing Microservice** (Node.js / Express) [Containers]
- **Async Claims Processing Worker** (Background Worker), **Message Broker** (Apache Kafka), **Distributed Cache** (Redis Enterprise), **Cloud-Native Distributed SQL Database** (CockroachDB) [Containers]
- **SQL Layer**, **Distributed Transaction Engine**, **Storage Layer (Raft Consensus & RocksDB)** [Components of CockroachDB]

## Relationships
- **Patient Portal / Mobile App -> Unified API Gateway** (HTTPS / REST and WebSocket via OIDC/OAuth 2.0)
- **Front-Desk / Clinicians / Billing / IT -> Unified API Gateway** (HTTPS / REST)
- **Unified API Gateway -> Patient Registration & Scheduling & Billing Microservices** (HTTP / REST)
- **Unified API Gateway -> EMR Microservice** (gRPC)
- **Microservices -> Cloud-Native Distributed SQL Database** (PostgreSQL Wire Protocol / TLS 1.3)
- **Billing Microservice -> Message Broker** (Apache Kafka Protocol)
- **Async Claims Processing Worker -> Message Broker** (Apache Kafka Protocol)
- **Clinic Management System -> Lab & Imaging Systems** (HL7 FHIR over HTTPS / REST / JSON with W3C trace contexts)
- **Clinic Management System -> Insurance Clearinghouses** (Secure EDI / HTTPS APIs with circuit breakers)
- **Clinic Management System -> Identity Provider (IdP)** (OIDC/SAML 2.0 over HTTPS)
- **on-prem-k8s -> eu-central-1** (Encrypted IPsec site-to-site VPN and mutual TLS)

## Technology Stack
- **API Layer:** TLS 1.3, JWT validation via Unified API Gateway
- **Backend Services:** Spring Boot, Go (gRPC), Node.js / Express
- **Messaging & Caching:** Apache Kafka for asynchronous processing; Redis Enterprise for distributed sessions
- **Database:** CockroachDB (SQL Layer, Distributed Transaction Engine, RocksDB + Raft Consensus) for distributed ACID compliance
- **Infrastructure & Security:** Kubernetes (`on-prem-k8s`), AWS (`eu-central-1`), AES-256 at rest, mutual TLS (mTLS), PgBouncer for connection pooling

## Rationale
This hybrid cloud architecture ensures zero-downtime 99.99% availability and strict HIPAA/GDPR compliance for critical healthcare operations. Distributed SQL with Raft consensus guarantees data consistency and durability across regions while meeting sub-second EMR performance demands.