## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict compliance, and seamless interoperability with external healthcare networks.

## Key Elements
- **Medical Staff & Administrators (Person):** Primary clinical users accessing daily workflows via HTTPS and MFA.
- **Patients (Person):** End-users accessing self-service scheduling and viewing records via the Patient Portal.
- **Billing Specialists (Person):** Financial users managing revenue cycles and claims.
- **Clinic Management System (Software System):** Central boundary encompassing admissions, EMR, scheduling, and billing containers.
- **External Labs & Imaging Systems (Software System):** External diagnostic partners integrating via HL7 FHIR.
- **Insurance Clearinghouse (Software System):** External entity for automated claims processing.
- **WORM Audit Store (Infrastructure System):** Dedicated compliance boundary for immutable logs.

## Relationships
- **Medical Staff, Patients, & Billing Specialists -> Clinic Management System:** Interacts via HTTPS using TLS 1.3 with enforced MFA (R-05).
- **Clinic Management System <-> External Labs & Imaging Systems:** Integrates using HL7 FHIR (REST/JSON over TLS 1.3) (R-08).
- **Clinic Management System -> Insurance Clearinghouse:** Submits claims via secure EDI/HTTPS (R-04).
- **Clinic Management System -> WORM Audit Store:** Streams immutable access and admin logs via secure syslog/TLS (R-03).
- **on-prem-k8s <-> eu-central-1:** Communicates across the hybrid boundary via strict mutual TLS (mTLS).

## Technology Stack
- **Hybrid Kubernetes (`on-prem-k8s` & `eu-central-1`):** Chosen to meet active-active high availability (99.99%) and local survivability constraints (R-06).
- **HL7 FHIR (REST/JSON):** Standardized protocol for external lab and imaging interoperability (R-08).
- **AES-256 & Decentralized KMS:** Implemented across the hybrid boundary for secure data at rest and tenant-isolated encryption (R-05).
- **TLS 1.3 & mTLS:** Mandated for all external and inter-cluster traffic to enforce Zero-Trust security.

## Rationale
This hybrid architecture combines on-premises Kubernetes survivability with cloud elasticity in AWS (`eu-central-1`) to achieve the required 99.99% uptime and local data control. Strict adherence to HL7 FHIR, mTLS, and WORM storage satisfies rigorous HIPAA and GDPR compliance mandates while supporting sub-second EMR performance.