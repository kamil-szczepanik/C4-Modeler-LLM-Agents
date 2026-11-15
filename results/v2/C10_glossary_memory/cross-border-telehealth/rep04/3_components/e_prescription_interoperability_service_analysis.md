## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients using GCP. It enforces strict regional data residency and compliance using GCP Cloud Spanner, Cloud KMS, and isolated services.

## Key Elements
- **E-Prescription Interoperability Service** (Spring Boot / Apache Camel)
- **Prescription Router Component** (Apache Camel EIP)
- **HL7 FHIR Translator Component** (Java / HAPI FHIR)
- **EU National Gateway Adapter Component** (Apache Camel / Spring Integration)
- **Prescription Audit & Status Service Component** (Spring Boot / Data JPA)
- **Security & Token Validation Component** (Spring Security / OAuth2)
- **Dead-Letter Queue (DLQ) & Retry Handler Component** (Google Cloud Pub/Sub)
- **External Pharmacies** (EU national gateways and US pharmacy networks)

## Relationships
- API Gateway & Routing Service -> Security & Token Validation Component [gRPC / mTLS]
- Security & Token Validation Component -> Prescription Router Component [Direct / In-memory]
- Prescription Router Component -> EU National Gateway Adapter Component [Direct / In-memory]
- Prescription Router Component -> HL7 FHIR Translator Component [Direct / In-memory]
- Prescription Router Component -> Dead-Letter Queue (DLQ) & Retry Handler Component [AMQP / Pub/Sub]
- EU National Gateway Adapter Component -> External Pharmacies [TLS / Mutual TLS with digital signatures]

## Technology Stack
- **Spring Boot & Apache Camel**: Powers message routing, enterprise integration patterns, and microservices logic.
- **Java & HAPI FHIR**: Implements HL7 FHIR standard translations for US prescription compliance.
- **Google Cloud Pub/Sub**: Manages resilient asynchronous dead-letter queues with CMEK encryption.
- **Google Cloud KMS / Cloud HSM**: Provides hardware-backed keys for digital signatures and data-at-rest encryption.

## Rationale
This architecture ensures secure, compliant cross-border e-prescription delivery by isolating translation and routing logic behind robust security validation and cryptographic non-repudiation. Utilizing GCP managed services and regional data controls guarantees adherence to GDPR and HIPAA mandates without sacrificing system reliability.