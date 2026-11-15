## Overview
The Clinic Management System is a hybrid-cloud platform that manages patient admissions, EMRs, scheduling, and billing. It provides secure, highly available clinical operations while ensuring strict HIPAA and GDPR compliance.

## Key Elements
* **Users:** Patients, Front Desk Staff, Clinicians, Billing Specialists
* **Systems:** Clinic Management System (Core), Payment Gateway, Insurance Verification/RTE APIs, Lab & Imaging Systems
* **Containers:** API Gateway, Patient Portal, EMR Service, Billing Service, Scheduling Service
* **Technologies:** Kubernetes (on-prem-k8s), AWS (`eu-central-1`), OAuth2/OIDC, HL7 FHIR APIs, AES-256 / AWS KMS

## Relationships
* Patients / Staff -> API Gateway: HTTPS over TLS 1.3 with OAuth2/MFA authentication
* Core System -> Lab & Imaging Systems: RESTful HL7 FHIR APIs over mTLS
* Core System -> Insurance Clearinghouses: Real-Time Eligibility (RTE) APIs over TLS 1.3 with payload signatures
* Core System -> Payment Gateways: Secure HTTPS for claims and billing processing

## Technology Stack
* **Cloud Infrastructure:** Hybrid deployment across on-premise Kubernetes and AWS `eu-central-1` for high availability (99.99%)
* **Security & Compliance:** OAuth2/OIDC for IAM, AES-256 encryption via AWS KMS and local HSMs for data at rest, mTLS for inter-service communication
* **Interoperability:** HL7 FHIR over REST for standardized external medical data exchange

## Rationale
The hybrid architecture balances low-latency on-premise clinical operations with cloud scalability to meet 99.99% availability requirements. Strict encryption, OAuth2 access controls, and HL7 FHIR standards ensure seamless interoperability while satisfying mandatory HIPAA and GDPR data protection frameworks.