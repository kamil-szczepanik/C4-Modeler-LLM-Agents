## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The Integration Service container handles protocol translations and enforces regional data residency for external communications.

## Key Elements
- Prescription Router Component (Spring Integration)
- EU Gateway Adapter Component (Spring WebClient)
- US Pharmacy Adapter Component (Spring WebClient)
- Data Residency Enforcer Component
- Audit Logging Component

## Relationships
- Message Broker -> Integration Service: Consumes asynchronous messages [Google Cloud Pub/Sub]
- Integration Service -> EU National e-Prescription Gateways: Exchanges e-prescriptions [REST/SOAP over mTLS]
- Integration Service -> US Pharmacy Networks: Exchanges e-prescriptions [REST/SOAP over mTLS]

## Technology Stack
- Java / Spring Boot: Core framework for business logic and enterprise integration
- Spring Integration & Spring WebClient: Handles protocol routing and regional API calls
- Resilience4j: Implements circuit breakers and exponential backoff to prevent retry storms
- GCP Secret Manager & KMS: Manages dynamic mTLS certificates and cryptographic signing of audit trails
- Google Cloud Pub/Sub: Asynchronous messaging and dead-letter queues for failed dispatches

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional deployments and enforcing data residency via dedicated components. Asynchronous processing and resilience patterns maintain high availability despite unstable external gateway connections.