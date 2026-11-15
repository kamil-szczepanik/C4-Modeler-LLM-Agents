## Overview
• The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
• The system ensures high availability, strict HIPAA and GDPR compliance, and 10-year data retention across a hybrid cloud and on-premise topology.

## Key Elements
• Front-Desk Receptionists, Clinicians, Billing Specialists, IT/Compliance Administrators, Patients
• Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Patient Portal / Mobile App
• Unified API Gateway (API Gateway, TLS 1.3)
• Patient Registration Microservice (Spring Boot)
• EMR Microservice (Go / gRPC)
• Scheduling Microservice (Spring Boot)
• Billing Microservice (Node.js / Express)
• Async Claims Processing Worker
• Message Broker (Apache Kafka)
• Distributed Cache (Redis Enterprise)
• Cloud-Native Distributed SQL Database (CockroachDB)

## Relationships
• Patient Portal / Mobile App -> Unified API Gateway (HTTPS / REST and WebSocket via OIDC/OAuth 2.0)
• Clinic Management System -> Lab & Imaging Systems (HL7 FHIR over HTTPS REST/JSON with W3C trace contexts)
• Clinic Management System -> Insurance Clearinghouses (Secure EDI / HTTPS APIs with circuit breakers)
• Clinic Management System -> Identity Provider (IdP) (OIDC/SAML 2.0 over HTTPS)
• on-prem-k8s -> eu-central-1 (Encrypted IPsec site-to-site VPN and mutual TLS mTLS)

## Technology Stack
• Go / gRPC: Used for EMR Microservice to achieve <1s P95 load performance and internal low-latency transport
• CockroachDB: Selected for distributed SQL storage with Raft consensus to guarantee zero-downtime availability and 10-year data retention
• Apache Kafka: Implements asynchronous messaging for claims processing to prevent blocking HTTP threads
• Redis Enterprise: Provides distributed session state and WebSocket message broker capabilities
• Vault / cert-manager: Manages automated short-lived internal PKI certificate rotation with 24-hour TTL

## Rationale
• This architecture combines a hybrid multi-region cloud deployment with distributed consensus to satisfy 99.99% availability and zero-data-loss requirements.
• Microservice decomposition with strict encryption, WORM audit logging, and data minimization ensures complete HIPAA and GDPR compliance.