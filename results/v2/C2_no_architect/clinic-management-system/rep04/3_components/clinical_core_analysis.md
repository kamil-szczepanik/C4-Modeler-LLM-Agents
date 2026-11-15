## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, scheduling, electronic medical records, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability with external clinical systems.

## Key Elements
- Personas: Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators.
- External Systems: Insurance Payers/Clearinghouses, External Labs, and Imaging Systems.
- Containers & Components: Patient Portal, API Gateway (Istio, WAF), Clinical Core (EMR, Scheduling, Billing Reconciliation), and Notification & Reminder Container.
- Infrastructure: On-premises Kubernetes and AWS `eu-central-1` regions.

## Relationships
- Patient Portal -> API Gateway: HTTPS with OAuth2 authentication.
- API Gateway -> Clinical Core: Traffic routing via Istio mTLS.
- Clinical Core -> External Labs and Imaging Systems: HL7 FHIR APIs over mTLS.
- Clinical Core -> Insurance Payers/Clearinghouses: Secure HTTPS with dead-letter queues.

## Technology Stack
- Orchestration & Mesh: Kubernetes (active-active) and Istio for service mesh and traffic shaping.
- Security & Compliance: HashiCorp Vault for secret management, OAuth2/OIDC for auth, TLS 1.3, and AES-256 storage encryption.
- Interoperability & Logging: HL7 FHIR protocols, OpenTelemetry for distributed tracing, and local ring buffers for asynchronous audit logs.

## Rationale
This architecture decouples high-priority EMR workflows from heavy billing processes to guarantee sub-second performance and 99.99% uptime. Asynchronous auditing and hybrid replication meet strict healthcare compliance mandates without sacrificing operational efficiency.