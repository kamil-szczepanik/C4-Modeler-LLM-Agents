## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records, appointment scheduling, and billing. It ensures high availability and strict regulatory compliance for medium-sized hospitals and clinics.

## Key Elements
- Front Desk Staff, Clinicians, Billing Specialists, Patients, Clinic Administrators, Practice Managers
- Laboratory Information Systems (LIS), PACS Imaging Archives, Insurance Payment Gateways
- Web Frontend (React)
- API Gateway (Node.js/Envoy)
- EMR Processing Service (Java Spring Boot)
- Billing Engine (Java Spring Boot)
- Interoperability Service (Python)
- Database (PostgreSQL)

## Relationships
- Front Desk Staff -> API Gateway: HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
- Clinicians -> API Gateway: HTTPS (TLS 1.3) with OAuth 2.0 / OIDC and MFA
- Web Frontend -> API Gateway: HTTPS (TLS 1.3)
- API Gateway -> EMR Processing Service: Internal gRPC
- API Gateway -> Billing Engine: Internal gRPC
- API Gateway -> Interoperability Service: Internal gRPC
- Interoperability Service -> Laboratory Information Systems (LIS): HL7 FHIR APIs over secure mutual TLS (mTLS)
- Interoperability Service -> PACS Imaging Archives: HL7 FHIR APIs over secure mutual TLS (mTLS)
- Interoperability Service -> Insurance Payment Gateways: HL7 FHIR APIs over secure mutual TLS (mTLS)

## Technology Stack
- React: Single Page Application container providing responsive user interfaces
- Node.js & Envoy: Routing, OAuth/MFA enforcement, and perimeter defense in the API Gateway
- Java Spring Boot: Core clinical records and financial workflow execution
- Python: Handling HL7 FHIR payloads in the Interoperability Service
- PostgreSQL: ACID-compliant database with AES-256 encryption at rest

## Rationale
This hybrid architecture uses containerized microservices communicating via gRPC to meet the sub-second P95 latency requirement for clinical screens. Active-active multi-region deployment and robust security protocols ensure 99.99% availability while maintaining HIPAA and GDPR compliance.