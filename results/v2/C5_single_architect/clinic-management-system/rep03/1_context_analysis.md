## Overview
The Clinic Management System is a hybrid cloud platform that securely manages patient admissions, electronic medical records, scheduling, and billing for clinical environments. It ensures strict regulatory compliance, high availability, and seamless interoperability with external healthcare infrastructure.

## Key Elements
- **Actors:** Patient (Web/Mobile), Clinician/Staff (Web), Hospital Administrator (Web)
- **Software System:** Clinic Management System
- **External Systems:** Identity Provider (OIDC/SAML), Payment Gateway, External Labs & Imaging Systems (HL7 FHIR), Regulatory Archiving / Audit Storage

## Relationships
- **Patient, Clinician, Administrator -> Clinic Management System:** Accesses features via HTTPS/Web/Mobile
- **Clinic Management System -> Identity Provider:** Authenticates users via OIDC/SAML with multi-factor auth
- **Clinic Management System -> Payment Gateway:** Submits billing and insurance claims via REST/TLS
- **Clinic Management System <-> External Labs & Imaging Systems:** Exchanges medical data via HL7 FHIR over TLS
- **Clinic Management System -> Regulatory Archiving / Audit Storage:** Replicates audit logs and records via HTTPS/TLS 1.3 for 10-year retention

## Technology Stack
- **Infrastructure:** Hybrid deployment utilizing on-premises Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for active-active high availability (R-06)
- **Protocols:** HTTPS, TLS 1.3, REST, and HL7 FHIR for secure, interoperable data exchange
- **Security:** OIDC/SAML for identity federation and multi-factor authentication (R-05)

## Rationale
This hybrid architecture isolates sensitive clinical data across compliant local and cloud environments to meet HIPAA, GDPR, and high availability mandates. Dedicated external integrations ensure seamless interoperability and immutable long-term storage without compromising core system performance.