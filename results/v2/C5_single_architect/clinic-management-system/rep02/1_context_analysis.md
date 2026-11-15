## Overview
The Clinic Management System is a distributed enterprise platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and seamless interoperability across hybrid cloud environments.

## Key Elements
* **Patient**: Actor using the Patient Portal via Web/Mobile.
* **Clinician / Receptionist**: Actors using the Clinic Management System Web interface.
* **Clinic Management System (CMS)**: Core distributed software system spanning hybrid infrastructure.
* **External Lab & Imaging Systems**: External systems for clinical diagnostics.
* **Payment Gateway / Insurance Clearinghouse**: External financial systems for billing and claims.
* **Notification Service**: External SMS and email gateway (Twilio/SendGrid).

## Relationships
* **Patient to CMS**: Interacts via HTTPS (Web/Mobile) using OAuth 2.0 / OpenID Connect for authentication and scheduling.
* **Clinician / Receptionist to CMS**: Interacts via HTTPS with multi-factor authentication for admissions, EMR, and scheduling.
* **CMS to External Lab & Imaging Systems**: Integrates via HL7 FHIR over REST/TLS.
* **CMS to Payment Gateway / Insurance Clearinghouse**: Integrates via HTTPS/REST for claims submission.
* **CMS to Notification Service**: Integrates via HTTPS/REST for 2FA challenges and appointment reminders.
* **On-Premise K8s to AWS (eu-central-1)**: Synchronizes data via encrypted VPN/Direct Connect.

## Technology Stack
* **Hybrid Cloud (on-prem-k8s & AWS eu-central-1)**: Selected to meet strict GDPR data residency and HIPAA compliance constraints.
* **HL7 FHIR over REST/TLS**: Chosen to ensure standardized interoperability with external lab and imaging systems.
* **OAuth 2.0 / OpenID Connect**: Implemented at the system boundary for secure authentication and audit trails.
* **AES-256 & TLS 1.3/mTLS**: Enforced for data at rest and in transit to satisfy security mandates.

## Rationale
This hybrid architecture directly fulfills the requirement for 99.99% high availability and stringent 10-year data retention while adhering to HIPAA and GDPR compliance. Utilizing standard protocols like HL7 FHIR and OAuth 2.0 guarantees secure interoperability and robust audit logging.