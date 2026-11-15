## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals to handle patient admissions, electronic medical records, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second EMR performance.

## Key Elements
- **Users**: Patients, Clinical Staff, Administrative Staff, Compliance Officers
- **External Systems**: Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Regulatory & Auditing System
- **API Gateway / BFF**: Kong / Envoy
- **Patient Portal**: Node.js/TypeScript backend
- **EMR & Scheduling Container**: Java Spring Boot application
- **Billing & Claims Container**: Python/FastAPI service
- **Analytics & Reporting Container**: Apache Pinot / ClickHouse
- **Data & Messaging Layer**: PostgreSQL, Redis, Apache Kafka, Debezium

## Relationships
- Patients & Staff access system via HTTPS/REST through Kong/Envoy API Gateway (OAuth2/OIDC, mTLS).
- Patient Portal communicates with backend via HTTPS/REST.
- EMR & Scheduling Container connects to PostgreSQL (AES-256) and Redis via gRPC/HTTPS.
- EMR, Billing, and Analytics containers communicate asynchronously via Apache Kafka events (Saga Pattern).
- Analytics container ingests data from PostgreSQL via Debezium CDC.
- System integrates with external Lab & Imaging systems via HL7 FHIR APIs.

## Technology Stack
- **Kong / Envoy**: Ingress routing, TLS termination, and MFA/JWT enforcement.
- **Node.js/TypeScript**: Powers the self-service Patient Portal.
- **Java Spring Boot**: Handles core EMR business logic, resource clash checks, and audit trails.
- **Python/FastAPI**: Decouples billing and insurance claim submissions.
- **Apache Kafka & Debezium**: Enables event-driven Saga pattern and CDC data piping.
- **PostgreSQL & Redis**: Relational storage (AES-256) and distributed scheduling locks.
- **Apache Pinot / ClickHouse**: Optimizes 10-year retention and heavy reporting queries.
- **Kubernetes (Hybrid)**: Orchestrates containers across on-prem-k8s and AWS eu-central-1.

## Rationale
The microservices-based, event-driven architecture using Kafka ensures strict fault isolation between clinical and financial workflows, protecting EMR performance. Hybrid Kubernetes deployment and managed active-active data layers guarantee 99.99% availability and strict data residency compliance.