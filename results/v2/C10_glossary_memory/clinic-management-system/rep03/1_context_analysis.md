## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. Its core purpose is to deliver highly available, secure healthcare operations while maintaining strict regulatory compliance.

## Key Elements
- **Users**: Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, and Hospital Administrator
- **Software Systems**: Clinic Management System, Payment Gateway, External Lab & Imaging Systems, and Identity Provider (IdP)
- **Deployment Environments**: On-Premise Infrastructure (on-prem-k8s) and AWS Cloud (eu-central-1)

## Relationships
- **Users to System**: HTTPS (TLS 1.3) via WAF with risk-based adaptive MFA
- **System to IdP**: OpenID Connect (OIDC) / OAuth2 over HTTPS
- **System to External Systems**: HL7 FHIR APIs and Payment REST APIs over encrypted HTTPS
- **Internal Cross-Environment**: Encrypted site-to-site VPN with mutual TLS (mTLS) and micro-segmentation

## Technology Stack
- **Kubernetes (on-prem-k8s & AWS)**: Orchestration platform ensuring high availability and hybrid workload separation
- **OpenID Connect (OIDC) IdP**: Centralized authentication with local on-prem caching for emergency break-glass
- **HL7 FHIR APIs**: Standardized healthcare interoperability interface for external lab and imaging integration
- **AES-256 and WORM Storage**: Cryptographic storage controls ensuring HIPAA/GDPR compliance and 10-year data retention

## Rationale
The hybrid architecture balances local-first autonomy for life-critical clinical writes during WAN outages with cloud scalability for patient portals. This guarantees 99.99% availability and sub-second EMR performance while strictly enforcing zero-trust security and data residency mandates.