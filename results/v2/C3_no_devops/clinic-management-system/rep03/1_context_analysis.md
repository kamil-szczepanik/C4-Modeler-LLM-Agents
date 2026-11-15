## Overview
The Clinic Management System is a hybrid cloud platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. Its core purpose is to streamline clinical workflows while strictly maintaining HIPAA and GDPR compliance and 99.99% availability.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers, and Regulatory Auditors
- Clinic Management System (Core Software System hosted on-premise Kubernetes and AWS eu-central-1)
- Enterprise Identity Provider (IdP)
- External Lab and Imaging Systems
- Payment Gateway and Insurance Clearinghouse
- Audit Archive (AWS S3 Glacier with WORM controls)

## Relationships
- Patients, Clinicians, Admin, and Billing interact with the Clinic Management System via Web/Mobile clients over HTTPS
- Clinic Management System authenticates users with the Enterprise Identity Provider via OIDC/SAML over HTTPS
- Clinic Management System integrates with External Lab & Imaging Systems using HL7 FHIR APIs over mTLS/HTTPS
- Clinic Management System submits claims to the Clearinghouse via REST APIs over TLS 1.3
- Clinic Management System streams logs to the Audit Archive using encrypted TLS 1.3 connections

## Technology Stack
- On-premise Kubernetes and AWS (eu-central-1): Hybrid cloud infrastructure to meet residency and availability constraints
- HL7 FHIR over HTTPS: Standardized healthcare interoperability protocol for lab and imaging systems
- OIDC/SAML over HTTPS: Enterprise identity federation protocols supporting multi-factor authentication
- AES-256 and HSM/KMS: Encryption standard for data at rest across databases and object storage
- AWS S3 Glacier: Cold storage solution for immutable 10-year data retention compliance

## Rationale
This hybrid architecture combines on-premise Kubernetes with AWS eu-central-1 to satisfy strict EU GDPR data sovereignty and 99.99% high availability requirements. Utilizing standard protocols like HL7 FHIR, OIDC, and robust encryption ensures seamless interoperability while strictly fulfilling HIPAA security mandates.