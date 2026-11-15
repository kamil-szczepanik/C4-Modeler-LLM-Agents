## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing while ensuring high availability, strict regulatory compliance, and high-performance clinical workflows. It provides a secure, scalable architecture leveraging modern containerized microservices and web interfaces.

## Key Elements
- Patients, Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management
- External Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouse
- Patient Portal, Internal Staff Application, API Gateway
- Patient Admission Service, Scheduling Service, EMR Service, Billing Service, Integration Engine
- Data Store (PostgreSQL, WORM Object Storage)

## Relationships
- Patients -> Patient Portal [HTTPS (Web/Mobile)]
- Patient Portal -> API Gateway [HTTPS (mTLS/OIDC)]
- Internal Staff Application -> API Gateway [HTTPS (mTLS/OIDC)]
- API Gateway -> Patient Admission Service, Scheduling Service, EMR Service, Billing Service [gRPC / REST over internal mesh]
- Integration Engine -> External Lab & Imaging Systems [HL7 FHIR over HTTPS (REST/JSON) with mTLS]
- Integration Engine -> Insurance Clearinghouse [EDI over SFTP / HTTPS]
- Services -> Data Store [PostgreSQL protocol with AES-256]

## Technology Stack
- React / TypeScript, Nginx: Front-end SPA implementation for Patient Portal and Internal Staff Application
- Kong / Envoy: API Gateway handling mTLS, rate limiting, and token validation
- Go / Node.js: High-performance backend microservices for admissions, scheduling, EMR, and integration
- Java Spring Boot: Robust enterprise backend for billing and insurance claims
- PostgreSQL, WORM Object Storage: Persistent storage ensuring AES-256 encryption and 10-year audit retention
- Kubernetes (on-prem-k8s, eu-central-1): Hybrid-cloud container orchestration meeting active-active 99.99% uptime requirements

## Rationale
This hybrid-cloud microservices architecture guarantees high availability (99.99%) through multi-region deployment and active-active scaling. Strict adherence to HIPAA and GDPR is enforced via AES-256 encryption, TLS/mTLS transport security, and WORM storage for immutable 10-year audit retention.