## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and AI symptom checking for EU and US patients. The architecture enforces strict regional data residency and interoperability using GCP and microservices.

## Key Elements
* Patients (EU / US) & Licensed Clinicians
* Local Pharmacies (EU / US) & Notification Gateway
* Prescription API Controller (Java/Spring Boot)
* FHIR & National Mapping Engine (Java with HAPI FHIR)
* Pharmacy Integration Client (Java Spring WebClient)
* Prescription Outbox & Retry Processor (Java/Spring Boot, Resilience4j, Spring Cloud Stream)
* Google Cloud Pub/Sub & Regional Cloud Spanner

## Relationships
* Regional API Gateways -> Prescription API Controller: Forwards prescription requests and validates tokens [gRPC over mTLS]
* Prescription API Controller -> FHIR & National Mapping Engine: Validates payload and passes data [In-memory]
* FHIR & National Mapping Engine -> Pharmacy Integration Client: Passes serialized payloads [In-memory]
* Pharmacy Integration Client -> Local Pharmacies: Transmits e-prescriptions [HTTPS / HL7 FHIR over mTLS]
* Pharmacy Integration Client -> Prescription Outbox & Retry Processor: Forwards failed delivery events [In-memory / Event]
* Prescription Outbox & Retry Processor -> Notification Gateway: Triggers clinician alerts [gRPC over mTLS]

## Technology Stack
* Java / Spring Boot: Core runtime for reliable microservices and business logic implementation
* HAPI FHIR Library: Standardizes US and international healthcare interoperability data structures
* Google Cloud Spanner: Provides globally consistent, regionally partitioned transactional data storage
* Google Cloud Pub/Sub: Manages dead-letter queues and asynchronous event messaging with CMEK encryption
* Resilience4j: Implements circuit breakers and retry logic for unstable external connections

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional health data while providing robust fault tolerance for unstable connections. The modular design guarantees reliable cross-border prescription delivery via automated retries, circuit breaking, and secure cryptographic logging.