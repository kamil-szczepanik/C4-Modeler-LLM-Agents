## Overview
• The Clinic Management System manages patient registration, scheduling, electronic medical records (EMR), and billing for medium-sized hospitals and clinics.
• It provides secure, high-availability healthcare operations compliant with HIPAA and GDPR regulations across a hybrid cloud architecture.

## Key Elements
• Patients / Consumers
• Receptionists / Front Desk
• Clinicians / Doctors
• Billing Specialists
• Clinic Administrators
• Compliance Auditors / Data Protection Officers (DPOs)
• Clinic Management System (Core Software)
• External Systems: Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP)
• Infrastructure: `on-prem-k8s` and `eu-central-1` (AWS)

## Relationships
• Patients, staff, and auditors interact with the Clinic Management System via HTTPS/Secure Web Portals.
• Clinic Management System connects to IdP via OIDC/SAML 2.0 for multi-factor authentication.
• Integrates with Lab & Imaging Systems using HL7 FHIR REST APIs over TLS 1.3.
• Submits insurance claims to Payment Gateways via HTTPS/REST using OAuth 2.0.
• Replicates data and archives compliance logs to AWS `eu-central-1` via mTLS and S3 APIs.

## Technology Stack
• Kubernetes (`on-prem-k8s` and cloud): Chosen for hybrid workload orchestration and local data residency.
• AES-256 with Customer-Managed Keys (CMK): Selected to satisfy strict data-at-rest encryption security mandates.
• HL7 FHIR REST APIs: Adopted for standardized healthcare interoperability with external diagnostics.
• Kafka / FluentBit: Utilized for non-blocking asynchronous audit queuing to protect sub-second EMR load times.
• WORM Cloud Archival Storage: Deployed in AWS to meet the 10-year data retention mandate.

## Rationale
• The hybrid architecture keeps critical clinical read/write operations on-premise to maintain zero-latency during WAN outages and satisfy local data residency laws.
• Asynchronous queues and isolated audit paths ensure strict compliance and 99.99% availability without degrading sub-second clinician performance SLAs.