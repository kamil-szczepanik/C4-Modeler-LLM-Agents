## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- Users: Patients, Receptionists, Clinical Staff, Billing Specialists
- External Systems: External Labs/Imaging (HL7 FHIR), Insurance Clearinghouses, Payment Gateways, Identity Provider
- Containers: API Gateway (Envoy/Kong), Patient Portal Service, Scheduling Service, EMR Service, Billing Service, HL7 FHIR Integration Service, Analytics Service
- Data & Messaging: PostgreSQL Database, Apache Kafka Message Broker, External Vault/HSM

## Relationships
- Patients and Staff to API Gateway via HTTPS (OAuth2/OIDC, Multi-Factor Auth)
- API Gateway to Internal Services (Patient Portal, Scheduling, EMR, Billing) via gRPC over mTLS
- Internal Services to PostgreSQL via TLS with AES-256 at rest
- Services to Apache Kafka via internal TLS for asynchronous event publishing
- HL7 FHIR Integration Service to Labs/Imaging systems via HL7 FHIR REST APIs
- Billing Service to Insurance Clearinghouses and Payment Gateways via secure REST/HTTPS
- On-premise services to `eu-central-1` Analytics via secure TLS tunnels (PHI stripped)

## Technology Stack
- On-Premise Kubernetes & AWS (`eu-central-1`): Hybrid cloud deployment for data locality and scalability.
- Envoy / Kong: API Gateway for ingress routing, JWT validation, and rate limiting.
- PostgreSQL: Core transactional database for EMR and scheduling with streaming replication and AES-256 encryption.
- Apache Kafka: Event broker for decoupled, asynchronous workflow triggers.
- gRPC / mTLS: High-performance, secure inter-container communication protocol.
- HL7 FHIR: Standardized interoperability protocol for lab and imaging system integration.

## Rationale
This architecture uses hybrid container isolation to keep sensitive PHI localized on-premise while leveraging cloud resources for analytics, fulfilling stringent HIPAA and GDPR mandates. Active-active PostgreSQL replication, gRPC communication, and Kafka decoupling guarantee 99.99% availability and sub-second P95 EMR performance.