## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, high availability (99.99%), and a 10-year data retention policy.

## Key Elements
- Users: Front-Desk Receptionist, Clinician, Billing Specialist, Patient, Hospital Administrator, Compliance Officer
- External Systems: Lab & Imaging Systems, Payment & Insurance Gateway, Identity Provider (IdP)
- Containers: API Gateway (Kong/NGINX), Patient Portal Frontend (React), Staff Web Application (React), Core Clinical & EMR Service (Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service (Go/Spring Boot)
- Frontend Components: Authentication & Session Manager, Appointment & Scheduling Module, Demographics & Profile Form, Accessibility & Localization Module, API Client Layer
- Storage: PostgreSQL databases, AWS S3 Object Lock, HashiCorp Vault

## Relationships
- Patient -> Patient Portal Frontend: Accesses patient portal [HTTPS/REST]
- Patient Portal Frontend -> API Gateway: Makes API requests [HTTPS/REST]
- API Gateway -> Core Clinical & EMR Service: Routes EMR queries [gRPC/HTTPS]
- Core Clinical & EMR Service -> PostgreSQL: Persists patient medical records [JDBC/TLS]
- FHIR Interoperability Adapter -> External Lab & Imaging Systems: Exchanges health data [HL7 FHIR REST API]
- Billing & Claims Service -> Third-Party Payment & Insurance Gateway: Submits insurance claims [HTTPS/REST]

## Technology Stack
- Frontend: React 18, TypeScript, React Query, Tailwind CSS, deployed immutably to CDN
- Backend Services: Java Spring Boot, Node.js, Python, Go
- Integration & Security: HAPI FHIR, HashiCorp Vault for secrets management, Kong/NGINX API Gateway
- Database & Storage: PostgreSQL, AWS S3 Object Lock for 10-year data retention
- Infrastructure: Hybrid deployment on On-Premises Kubernetes and AWS (`eu-central-1`)

## Rationale
The hybrid architecture distributes workloads securely while leveraging AWS cloud scalability and on-premise Kubernetes control for clinical systems. Microservices isolation combined with PostgreSQL and AWS S3 Object Lock guarantees high availability (99.99%) and strict HIPAA/GDPR compliance.