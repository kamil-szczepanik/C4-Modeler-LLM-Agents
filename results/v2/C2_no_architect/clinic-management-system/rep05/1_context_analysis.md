## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), appointments, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability for clinical operations.

## Key Elements
* **Users:** Patients, Clinical Staff (Doctors/Nurses), Administrative & Billing Staff, Clinic Administrators/Compliance Officers
* **Containers:** Patient Self-Service Portal, EMR & Scheduling Core, Billing & Insurance Engine, Edge WAF / API Gateway
* **Infrastructure:** On-Premises Kubernetes Cluster (`on-prem-k8s`), AWS Cloud (`eu-central-1`)
* **Data Stores:** EMR Database with HSM-backed envelope encryption, WORM (Write-Once-Read-Many) Audit Storage Bucket

## Relationships
* **Patients to Patient Portal:** HTTPS / TLS 1.3 for registration, demographic capture, and appointment scheduling
* **Clinical & Admin Staff to Core Services:** FIDO2/WebAuthn MFA and short-lived JWTs (OAuth2/OIDC) for secure EMR and billing access
* **Core Services to Lab/Imaging Systems:** HL7 FHIR APIs over mTLS for clinical data exchange
* **Hybrid Infrastructure:** Encrypted mTLS (TLS 1.3) interconnecting `on-prem-k8s` and `eu-central-1`

## Technology Stack
* **Orchestration:** Kubernetes (`on-prem-k8s` and cloud) for active-active high availability (99.99% uptime)
* **Security & Auth:** OAuth2/OIDC, FIDO2/WebAuthn MFA, AES-256 for data at rest, and cloud-native HSMs for envelope encryption
* **Interoperability:** HL7 FHIR APIs for standardized third-party clinical system integration
* **Observability:** OpenTelemetry for distributed tracing and real-time audit log streaming

## Rationale
The hybrid architecture balances data sovereignty and strict GDPR/HIPAA compliance by maintaining local clinical controls while leveraging cloud scalability. Robust security measures, including zero-trust networking, mTLS, and WORM storage, guarantee regulatory adherence and 10-year data retention without compromising sub-second EMR performance.