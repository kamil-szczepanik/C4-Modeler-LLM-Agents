## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized healthcare facilities. It ensures HIPAA/GDPR compliance and 99.99% availability via a hybrid cloud architecture.

## Key Elements
- Users: Patient, Receptionist, Clinician, Billing Specialist
- External Systems: Identity Provider, External Lab & Imaging Systems, Insurance Clearinghouses, Payment Gateway, SIEM / Observability System, Centralized Vault
- Containers: API Gateway (NGINX/Kong), Web Application (React SPA), Core Services (Spring Boot), Billing Service (Node.js), Integration Service (Apache Camel), Data & Infrastructure Tier (PostgreSQL/Citus, Redis, Kafka, Istio, ArgoCD)
- Integration Service Components: Route Orchestrator (Apache Camel), FHIR Transformer (HAPI FHIR), Data Anonymization Interceptor, Vault Client (Spring Cloud Vault), Dead Letter Channel, Payload Cryptography Processor

## Relationships
- Core Services -> Integration Service: Asynchronous event streaming [Kafka with payload-level JWE/AES-256]
- Integration Service -> External Lab & Imaging Systems: Lab orders and results [HTTPS/FHIR with mTLS and OAuth2]
- Integration Service -> Centralized Vault: Dynamic secrets and X.509 certs [AppRole tokens]
- Integration Service -> SIEM / Observability System: Tracing telemetry with anonymized IDs [OpenTelemetry]

## Technology Stack
- Apache Camel: Enterprise integration patterns and workflow orchestration for the Integration Service
- HAPI FHIR Library: Standardized HL7 FHIR resource transformation (R-08)
- Kafka: Event streaming and encrypted Dead Letter Queue for reliability
- Spring Cloud Vault: Secure secret management and mTLS certificate handling
- Kubernetes (KEDA): Hybrid container deployment with auto-scaling

## Rationale
This architecture ensures 99.99% uptime and low-latency EMR access through asynchronous event-driven decoupling. It guarantees HIPAA/GDPR compliance via strict cryptographic controls, payload anonymization, and isolated network policies.