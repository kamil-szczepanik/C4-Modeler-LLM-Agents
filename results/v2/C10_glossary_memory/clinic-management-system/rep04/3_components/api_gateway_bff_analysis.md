## Overview
[The Clinic Management System is a hybrid cloud healthcare platform that manages patient admissions, EMRs, scheduling, and billing for medical facilities. It ensures HIPAA/GDPR compliance, high availability (99.99%), and long-term data retention.]

## Key Elements
- Patient, Clinician, Billing/Admin Staff, Compliance Officer
- Clinic Management System
- Patient Portal SPA/Mobile (React/TypeScript)
- Clinician/Admin Workspace SPA (React/TypeScript)
- API Gateway / BFF (Envoy/Kong)
- Core Services Container (Java/Spring Boot)
- Billing Service Container (Node.js/TypeScript)
- Integration Service Container (Apache Camel / Spring Integration)
- Audit & Compliance Logging Container (WORM-compliant storage / Spring Integration)
- PostgreSQL & HL7 FHIR Compliant Data Stores (PostgreSQL with AES-256 at rest)
- Message Broker (RabbitMQ/Kafka)
- Lab & Imaging Systems, Insurance Clearinghouse / External Billing Provider

## Relationships
- Patient -> API Gateway / BFF [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Clinician -> API Gateway / BFF [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Billing/Admin Staff -> API Gateway / BFF [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- Compliance Officer -> API Gateway / BFF [HTTPS (TLS 1.3, OAuth2/OIDC, MFA)]
- API Gateway / BFF -> Patient Portal SPA/Mobile [HTTPS]
- API Gateway / BFF -> Clinician/Admin Workspace SPA [HTTPS]
- API Gateway / BFF -> Core Services Container [gRPC over mTLS]
- API Gateway / BFF -> Billing Service Container [gRPC over mTLS]
- Core Services Container -> PostgreSQL & HL7 FHIR Compliant Data Stores [JDBC (AES-256 at rest)]
- Billing Service Container -> Message Broker [AMQP]
- Integration Service Container -> Lab & Imaging Systems [HL7 FHIR over REST/JSON (TLS 1.3)]
- Billing Service Container -> Insurance Clearinghouse / External Billing Provider [HTTPS / EDI X12]

## Technology Stack
- Envoy/Kong: API gateway for routing, reverse proxy, token exchange, and edge security
- React/TypeScript: High-performance frontend user interfaces for portals and workspaces
- Java/Spring Boot: Robust domain logic for core clinical services and EMRs
- Node.js/TypeScript: Isolated financial and billing processing
- PostgreSQL: Relational persistence with AES-256 encryption at rest
- RabbitMQ/Kafka: Asynchronous messaging for resilient insurance claim submissions
- Apache Camel / Spring Integration: HL7 FHIR translation adapters and audit logging
- Hybrid Cloud: Deployed across on-prem-k8s and AWS eu-central-1 for high availability

## Rationale
[This architecture satisfies high availability (99.99%) and HIPAA/GDPR requirements through active-active hybrid cloud deployment, mTLS service mesh communication, and strict token exchange. It meets sub-second P95 performance targets using an optimized API Gateway / BFF with payload aggregation and dedicated microservices.]