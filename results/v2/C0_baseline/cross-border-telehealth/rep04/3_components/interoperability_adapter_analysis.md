## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- **Interoperability Adapter Container**: Manages cross-border prescription routing and external gateway communication.
- **EU Gateway Plugin**: Translates core payloads to national EU standards using Go.
- **US FHIR Translator**: Maps payloads to US HL7 FHIR resources using Go and HAPI FHIR Java.
- **Regional Routing Engine**: Enforces data residency by directing traffic to regional endpoints.
- **Delivery Status Notifier**: Asynchronously pushes delivery acknowledgements via GCP Pub/Sub.
- **Audit Ledger & Receipt Signer**: Signs payloads and receipts using Google Cloud KMS.
- **External Gateways**: EU E-Prescription Gateways and US Pharmacy Networks.

## Relationships
- API Gateway / Core Backend -> Interoperability Adapter: Triggers e-prescription routing via mTLS and Internal API.
- Regional Routing Engine -> EU Gateway Plugin / US FHIR Translator: Delegates payload transformation via in-memory communication or gRPC.
- EU Gateway Plugin / US FHIR Translator -> Audit Ledger & Receipt Signer: Requests cryptographic signatures via in-memory communication or gRPC.
- Delivery Status Notifier -> API Gateway / Core Backend: Publishes signed delivery receipts via GCP Pub/Sub.
- Interoperability Adapter -> EU E-Prescription Gateways: Transmits EU prescriptions using REST, SOAP, and HL7 FHIR over mTLS.
- Interoperability Adapter -> US Pharmacy Networks: Transmits US prescriptions using REST, SOAP, and HL7 FHIR over mTLS.

## Technology Stack
- **Go**: Core implementation language for high performance and low resource consumption.
- **GCP Pub/Sub**: Asynchronous messaging for reliable delivery status notifications under unstable network conditions.
- **Google Cloud KMS**: Region-specific key management for generating tamper-proof cryptographic audit receipts.
- **GCP Secret Manager**: Secure storage for external gateway mTLS private keys and certificates.
- **GCP Cloud Logging**: Centralized logging with PHI/PII masking enforced for GDPR and HIPAA compliance.

## Rationale
This architecture enforces data residency by deploying isolated regional instances in europe-west3 and us-central1. Asynchronous queuing and cryptographic auditing ensure compliance, reliability, and non-repudiation for cross-border healthcare transactions.