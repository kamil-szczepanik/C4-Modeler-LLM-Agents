## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers in a hybrid cloud environment.]
[It ensures HIPAA and GDPR compliance while maintaining 99.99% availability and a 10-year data retention policy.]

## Key Elements
- Patients, Receptionists, Clinicians, and Billing Specialists
- Clinic Management System (Core Software System)
- Lab & Imaging Systems, Insurance Payment Gateway, Identity Provider
- Patient Portal, Notification Gateway (Twilio/SendGrid)
- Hybrid API Gateway with WAF

## Relationships
- Patient Portal to Core System via HTTPS/REST
- Lab & Imaging Systems to Core System via HL7 FHIR over HTTPS
- Insurance Payment Gateway to Core System via REST/SOAP with TLS 1.3
- Identity Provider to Core System via OIDC/SAML 2.0
- Inter-environment communication via mTLS

## Technology Stack
- On-premise Kubernetes and AWS (eu-central-1) for hybrid cloud deployment
- ArgoCD for GitOps deployments
- OpenTelemetry for centralized, tamper-proof hybrid observability
- Write-Once-Read-Many (WORM) storage for 10-year audit retention
- AES-256 for data encryption at rest

## Rationale
[The hybrid architecture leverages on-premises infrastructure and AWS eu-central-1 to strictly satisfy GDPR residency and HIPAA security mandates.]
[Active-active design patterns, mTLS, and WORM storage collectively guarantee high availability, strict audit trails, and resilient 10-year data retention.]