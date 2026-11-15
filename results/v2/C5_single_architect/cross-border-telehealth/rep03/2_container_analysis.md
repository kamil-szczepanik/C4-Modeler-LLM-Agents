## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict regional data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
* Patients and Clinicians (Users)
* Web/Mobile Frontend App (Flutter/React)
* API Gateway (Envoy/GCP API Gateway)
* Core Telehealth Service (Go/Spring Boot)
* WebRTC SFU Video Service (Mediasoup)
* AI Inference Service (Python/FastAPI)
* E-Prescription Integrator (Node.js)
* FHIR Event Bus (GCP Pub/Sub)
* Regional Data Stores (GCP Cloud SQL/Spanner)
* External National E-Prescription Networks and US Pharmacy Systems

## Relationships
* Patients/Clinicians to API Gateway via HTTPS and WSS
* API Gateway to Core Telehealth and AI Inference via gRPC
* Core Telehealth to WebRTC SFU via WebRTC/UDP
* Core Telehealth to E-Prescription Integrator via GCP Pub/Sub (HL7 FHIR)
* Integrator to External Networks via REST/SOAP

## Technology Stack
* GCP Cloud Platform: Dual deployment in `europe-west3` and `us-central1` for GDPR/HIPAA data residency.
* Flutter/React Frontend: Enables local caching for degraded connections under 300 kbit/s.
* Mediasoup WebRTC SFU: Adapts video streaming for unstable rural internet.
* Python/FastAPI AI Service: Implements traceable symptom checking with immutable audit logs.
* GCP Pub/Sub: Decouples asynchronous e-prescription messaging.

## Rationale
This architecture physically partitions data across isolated GCP regions to strictly satisfy GDPR and HIPAA mandates. Decoupled regional microservices, event-driven messaging, and adaptive WebRTC streaming ensure resilience and low latency over unstable connections.