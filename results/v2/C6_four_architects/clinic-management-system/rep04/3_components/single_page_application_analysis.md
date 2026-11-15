## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures HIPAA/GDPR compliance, high availability (99.99%), and sub-second EMR performance using a hybrid cloud deployment.

## Key Elements
- **Users**: Doctors, Nurses, Receptionists, Billing Staff
- **Frontend Container**: Single-Page Application (React / TypeScript) with Router, Auth, API Client, UI Modules, Security Interceptor, Telemetry, and Encryption Manager components
- **Edge Container**: API Gateway (Kong / Envoy) with TLS Termination, Auth Plugin, and Rate Limiter
- **Backend Containers**: Core Clinical Microservice (Spring Boot), Scheduling Microservice (Go), Billing & Claims Microservice (.NET), Integration / FHIR Service (Node.js), FHIR Integration Broker (Apache Camel)
- **Data & Infrastructure**: Distributed Relational Database (CockroachDB / PostgreSQL), Message Broker (Apache Kafka), Caching Layer (Redis Enterprise), Key Management Service (Vault), Audit Log Store (Elasticsearch), Service Mesh (Istio)
- **External Systems**: Identity Provider (IdP), Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems

## Relationships
- **Users -> Single-Page Application**: Interacts with UI [HTTPS / WSS]
- **Single-Page Application -> API Gateway**: Sends requests via API Client [HTTPS / WSS]
- **API Gateway -> Core Clinical, Scheduling, & Billing Microservices**: Forwards requests via Service Mesh [gRPC / HTTPS with mTLS]
- **Integration / FHIR Service -> External Lab & Imaging Systems**: Exchanges health data [HL7 FHIR REST APIs]
- **Core Services -> Distributed Relational Database & Message Broker**: Persists data and publishes domain events [TCP / TLS]

## Technology Stack
- **Frontend**: React, TypeScript, Redux Toolkit / Zustand, TanStack Query, Web Crypto API for client-side encryption, OpenTelemetry for metrics
- **Gateway & Mesh**: Kong / Envoy, Istio Service Mesh for mTLS and routing
- **Backend**: Spring Boot (Clinical), Go (Scheduling), .NET (Billing), Node.js & Apache Camel (FHIR Integration)
- **Data & Caching**: CockroachDB / PostgreSQL, Redis Enterprise for caching and rate limiting
- **Security & Compliance**: Vault for key management, Elasticsearch for immutable audit logging, OAuth2/OIDC for authentication

## Rationale
The hybrid cloud architecture leverages on-premises Kubernetes and AWS (eu-central-1) to guarantee strict data residency and 99.99% high availability. Microservices combined with event-driven messaging via Kafka ensure strict segregation of sensitive clinical workloads while meeting sub-second EMR performance and comprehensive HIPAA/GDPR audit requirements.