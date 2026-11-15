## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and interoperability across diverse national healthcare standards.

## Key Elements
* **Routing & Consent Validator**: Spring Cloud Gateway validating patient consent and routing payloads by region (EU vs. US).
* **US FHIR Translator**: HAPI FHIR JPA mapping domain models to HL7 FHIR for US pharmacies.
* **EU National Adapter Engine**: Apache Camel housing pluggable adapters for national EU e-prescription standards.
* **Audit & Compliance Logger**: Records transaction hashes to ensure accountability.
* **Regional Outbox Dispatcher**: Spring Batch / Debezium ensuring transactional outbox execution for regional data locality.

## Relationships
* **API Gateway/BFF** -> **Routing & Consent Validator**: Inbound dispatch via gRPC.
* **EU National Adapter Engine** -> **National Pharmacy Networks (EU)**: Transmits prescriptions via REST/SOAP over mTLS.
* **US FHIR Translator** -> **US Pharmacy Systems**: Transmits prescriptions via HL7 FHIR over HTTPS.
* **US FHIR Translator & EU National Adapter Engine** -> **Data Storage (Cloud SQL)**: Persists audit states and outbox events via JDBC/HikariCP using regional endpoints (`europe-west3`, `us-central1`).

## Technology Stack
* **Java / Spring Boot**: Core framework for the E-Prescription Integrator container ensuring robust enterprise integration.
* **Apache Camel / Spring Integration**: Powers pluggable adapters to handle diverse national EU e-prescription formats.
* **HAPI FHIR**: Implements US healthcare interoperability standards.
* **Spring Batch / Debezium**: Manages transactional outbox patterns for reliable data staging and residency enforcement.
* **Cloud SQL (PostgreSQL)**: Regional databases deployed in `europe-west3` and `us-central1` ensuring strict data segregation.

## Rationale
This component architecture isolates complex and divergent national e-prescription standards while rigorously enforcing regional data residency constraints (GDPR and HIPAA). Using proven integration and batch patterns guarantees reliable, compliant cross-border prescription delivery even under unstable network conditions.