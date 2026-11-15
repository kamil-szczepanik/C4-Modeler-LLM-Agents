## Overview
• Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
• Operates as a hybrid cloud clinical IT solution delivering high availability and regulatory compliance.

## Key Elements
• Users: Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers
• External Systems: Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways
• Containers: Web Frontend (React), API Gateway (Node.js), EMR Processing Service (Java Spring Boot), Billing Engine (Java Spring Boot), Interoperability Service (Python), Database (PostgreSQL)
• Interoperability Service Components: API Router Component, FHIR Transformation Engine, Outbound mTLS Dispatcher Component

## Relationships
• Front Desk Staff -> API Gateway via HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
• Clinicians -> API Gateway via HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
• Web Frontend -> API Gateway via HTTPS (TLS 1.3)
• API Gateway -> EMR Processing Service via Internal gRPC
• API Gateway -> Interoperability Service via Internal gRPC
• Interoperability Service -> Laboratory Information Systems (LIS) via HL7 FHIR APIs over secure mutual TLS (mTLS)
• Interoperability Service -> PACS Imaging Archives via HL7 FHIR APIs over secure mutual TLS (mTLS)
• Interoperability Service -> Insurance Payment Gateways via HL7 FHIR APIs over secure mutual TLS (mTLS)

## Technology Stack
• React: Single Page Application container for responsive user interfaces
• Node.js: API Gateway container for routing and OAuth/MFA enforcement
• Java Spring Boot: Core EMR Processing Service and Billing Engine containers for robust business logic
• Python: Interoperability Service container for handling HL7 FHIR payloads using FastAPI, Pydantic, and HTTPX
• PostgreSQL: Encrypted database container with ACID compliance and AES-256 encryption at rest
• Kubernetes: Hybrid deployment orchestration platform ensuring 99.99% uptime via active-active configurations

## Rationale
• Combines containerized microservices with hybrid cloud infrastructure to satisfy strict HIPAA and GDPR compliance requirements.
• Implements active-active high availability and HL7 FHIR interoperability standards to ensure seamless clinical workflows and secure data exchanges.