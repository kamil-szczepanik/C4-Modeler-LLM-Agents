## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It guarantees strict regulatory compliance and high availability for low-bandwidth connections.

## Key Elements
* **Clients:** Web Application & Mobile App (Flutter / React)
* **Edge & Routing:** API Gateway (Google Cloud API Gateway / Envoy)
* **Backend Services:** Core Telehealth Service (Go / Spring Boot), AI Symptom Checker Orchestrator (Python / FastAPI), E-Prescription Integration Service (Node.js / Java), Media Relay & Signaling Service (WebRTC / LiveKit)
* **Data Storage:** Cloud SQL PostgreSQL and Memorystore Redis

## Relationships
* **Client to Gateway:** HTTPS and WSS protocols for application traffic and real-time signaling
* **Gateway to Microservices:** gRPC protocol over internal GCP VPC networks
* **Services to Database:** TLS 1.3 connections to regional Cloud SQL PostgreSQL instances
* **External Integrations:** HL7 FHIR for US systems and national e-prescription standards for EU countries

## Technology Stack
* **GCP (`europe-west3`, `us-central1`):** Enforces data residency for GDPR and HIPAA compliance
* **Go / Spring Boot & Python:** Power core business logic and traceable AI orchestration
* **WebRTC / LiveKit:** Enables resilient video consultations down to 300 kbit/s via adaptive bitrate control

## Rationale
Regional container duplication in GCP ensures strict data isolation between the EU and US. Dedicated media relay and integration microservices satisfy low-bandwidth and regional interoperability constraints.