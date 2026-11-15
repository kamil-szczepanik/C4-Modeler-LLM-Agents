## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Built on GCP to ensure strict regional data residency, regulatory compliance, and resilience for rural connectivity.

## Key Elements
* Patients and Clinicians (Users)
* Web & Mobile Clients (React / React Native)
* API Gateway & Routing (Kong / GCP API Gateway)
* Core Telehealth Service (Java / Spring Boot)
* WebRTC Media Broker (Node.js / Mediasoup)
* AI Symptom Checker Service (Python / FastAPI)
* FHIR & E-Prescription Integration Service (Python / Java)
* Consent & Audit Logging Service (Go)
* Messaging (Cloud Pub/Sub)
* Databases (Cloud SQL PostgreSQL, Cloud Storage)
* National E-Prescription Gateways (EU) and US Pharmacy Networks

## Relationships
* Web & Mobile Clients -> API Gateway & Routing: HTTPS / WSS
* API Gateway & Routing -> Core Telehealth Service: gRPC / REST
* Core Telehealth Service -> WebRTC Media Broker: WebRTC / gRPC
* Core Telehealth Service -> AI Symptom Checker Service: gRPC / REST
* Core Telehealth Service -> FHIR & E-Prescription Integration Service: gRPC / REST
* FHIR & E-Prescription Integration Service -> National E-Prescription Gateways & US Pharmacy Networks: HTTPS with mTLS
* All Services -> Consent & Audit Logging Service: gRPC over TLS

## Technology Stack
* Cloud Provider: GCP (`europe-west3` for EU, `us-central1` for US) to enforce data residency
* Backend Services: Java (Spring Boot) and Python (FastAPI) for core logic and AI
* Integration: Java (HAPI FHIR) for US Core profiles and national eHDSI/OpenNCP standards
* Messaging & Resilience: Cloud Pub/Sub for asynchronous retry queues during network partitions
* Communication: gRPC for internal service-to-service communication; HTTPS with mTLS for external integrations

## Rationale
The architecture strictly enforces regional isolation between EU and US data processing to comply with GDPR and HIPAA mandates. Asynchronous queuing via Cloud Pub/Sub guarantees prescription delivery and telehealth availability for patients with unstable rural internet connections.