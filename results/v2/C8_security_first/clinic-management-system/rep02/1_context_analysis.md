## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, appointment scheduling, and insurance billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and seamless interoperability with external clinical systems.

## Key Elements
- Patients
- Receptionists / Front Desk Staff
- Clinicians / Doctors
- Billing Specialists
- Clinic Management System (Core Software System)
- Identity Provider (IdP)
- Lab & Imaging Systems
- Insurance Clearinghouse

## Relationships
- Patients & Staff -> Clinic Management System: HTTPS (TLS 1.3), Web/Mobile UI
- Clinic Management System -> Identity Provider (IdP): OIDC / SAML over HTTPS
- Clinic Management System <-> Lab & Imaging Systems: HL7 FHIR over mTLS
- Clinic Management System -> Insurance Clearinghouse: REST over HTTPS with OAuth 2.0

## Technology Stack
- Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1): Enables active-active deployment and local survivability during WAN partitions
- OpenTelemetry: Provides unified observability and synthetic transaction monitoring for performance SLAs
- AES-256 and WORM Storage: Secures data at rest with customer-managed keys and ensures 10-year immutable data retention
- OAuth 2.0 / OIDC with MFA: Enforces strict Role-Based and Attribute-Based Access Control

## Rationale
The hybrid active-active architecture guarantees 99.99% availability and local survivability for critical patient intake during network disruptions. Robust encryption, mTLS, and immutable audit logs satisfy strict HIPAA and GDPR compliance requirements without sacrificing clinical performance.