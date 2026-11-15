## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, highly available clinical workflows while ensuring strict compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Clinicians/Doctors, Receptionists/Admin, Billing Specialists, Compliance/IT Auditors
- Patient Portal App, Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- API Gateway (NGINX / Kong), EMR Service, Appointment Service, Billing Container, Audit & Compliance Container
- HL7 FHIR Interoperability Service (Python / FastAPI)
- PostgreSQL with Redis caching, Apache Kafka

## Relationships
- Patient Portal App / API Gateway -> EMR Service / Appointment Service / Billing Container [HTTPS / REST / gRPC]
- API Gateway -> HL7 FHIR Interoperability Service [HTTPS / REST / mTLS]
- HL7 FHIR Interoperability Service -> External Lab & Imaging Systems [HL7 FHIR APIs over mTLS]
- All Containers -> PostgreSQL [SQL over TLS 1.3]
- All Containers -> Audit & Compliance Container [Apache Kafka]

## Technology Stack
- Node.js / Go: Used for core microservices to ensure high-performance concurrent processing
- Python / FastAPI: Selected for the HL7 FHIR service due to native Pydantic schema validation and rapid development
- PostgreSQL: Provides reliable relational persistence with AES-256 envelope encryption at rest
- Apache Kafka: Powers asynchronous event streaming and dead-letter queue resilience
- Kubernetes: Manages hybrid cloud container orchestration across on-prem and AWS eu-central-1

## Rationale
The hybrid architecture utilizes active-active Kubernetes clusters to achieve 99.99% availability and high-performance EMR delivery. Strict multi-factor authentication, mTLS, and AES-256 encryption satisfy stringent HIPAA and GDPR security constraints.