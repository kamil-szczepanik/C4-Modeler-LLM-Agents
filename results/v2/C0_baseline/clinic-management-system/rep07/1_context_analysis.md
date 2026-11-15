## Overview
The Clinic Management System is a hybrid-cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
* **Human Actors**: Patient, Clinician/Doctor, Receptionist/Admin, Billing Specialist, Compliance/IT Auditor
* **Software Systems**: Clinic Management System (Core), Patient Portal App, Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
* **Infrastructure**: On-Premises Kubernetes (on-prem-k8s), AWS (eu-central-1), Global API Gateway with WAF
* **Data & Messaging**: Synchronous replication storage, mTLS-secured Kafka/RabbitMQ message broker

## Relationships
* **Human Actors -> Clinic Management System**: HTTPS / TLS 1.3 via Web/Mobile UI
* **Patient Portal App -> Clinic Management System**: HTTPS REST/GraphQL for self-service scheduling and billing
* **Clinic Management System -> Identity Provider**: OIDC / SAML 2.0 with OAuth2 token binding for MFA/SSO
* **Clinic Management System <-> External Lab & Imaging Systems**: HL7 FHIR over mutual TLS (mTLS)
* **Clinic Management System -> Payment Gateway**: Asynchronous REST APIs via Kafka/RabbitMQ for claims

## Technology Stack
* **Kubernetes (Hybrid)**: Deployed across on-prem-k8s and AWS eu-central-1 for active-active high availability (99.99%).
* **HL7 FHIR & REST/GraphQL**: Standardized protocols for clinical interoperability and client communication.
* **AES-256 with CMK**: Customer-managed encryption keys for data at rest ensuring GDPR/HIPAA compliance.
* **SPIFFE/SPIRE & mTLS**: Automated certificate rotation for secure inter-service zero-trust communication.
* **Kafka/RabbitMQ**: Asynchronous messaging to decouple external third-party latency from core EMR performance.

## Rationale
This hybrid architecture combines on-premises control with cloud scalability to meet stringent data residency and 99.99% uptime demands. Asynchronous messaging and strict cryptographic boundaries protect core clinical workflows while supporting seamless external interoperability.