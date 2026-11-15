## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces regional data residency and strict regulatory compliance on Google Cloud Platform.]

## Key Elements
* Patients (EU/US) and Licensed Clinicians
* API Gateway (Envoy and Google Cloud Load Balancing)
* Core Telehealth Service (Node.js/Go container)
* E-Prescription Integration Service (Java/Spring Boot container)
* AI Symptom Checker Service (Python/FastAPI container)
* Media Streaming Container (Janus WebRTC SFU)
* EU National E-Prescription Gateways and US Healthcare Networks/Pharmacies
* Google Cloud Pub/Sub (Regional DLQs and Event Topics)
* Regional Redis Clusters and PostgreSQL Instances

## Relationships
* API Gateway -> Core Telehealth Service: Routes external HTTP/HTTPS traffic [gRPC over mTLS]
* Core Telehealth Service -> E-Prescription Integration Service: Coordinates prescription workflows [gRPC over mTLS]
* E-Prescription Integration Service -> EU National Gateways: Submits translated prescriptions [REST/SOAP APIs via mTLS]
* E-Prescription Integration Service -> US Healthcare Networks: Exchanges prescription data [HL7 FHIR APIs over HTTPS]
* E-Prescription Integration Service -> Google Cloud Pub/Sub: Manages failed dispatches and failure events [gRPC/HTTPS]

## Technology Stack
* Google Cloud Platform (`europe-west3`, `us-central1`): Ensures regional data residency compliance (R-05)
* Java / Spring Boot & Apache Camel: Powers the E-Prescription Integration Service and adapter routing
* HAPI FHIR & Resilience4j: Handles US interoperability and external network circuit-breaking
* Google Cloud Pub/Sub & CMEK: Provides regional messaging and at-risk data encryption
* Redis Cluster: Enables high-availability idempotency enforcement

## Rationale
[Regional GKE deployments and regionalized databases guarantee strict HIPAA and GDPR data residency compliance. Asynchronous event queues and circuit breakers isolate external gateway failures to maintain care continuity.]