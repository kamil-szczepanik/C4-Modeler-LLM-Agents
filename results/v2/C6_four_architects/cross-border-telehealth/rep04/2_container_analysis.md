## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability and regulatory compliance.

## Key Elements
* **Clients:** Web Application (React) and Mobile App (Flutter)
* **Ingress:** Google Cloud Global HTTPS Load Balancer with Google Cloud Armor and Google Cloud DNS (Geo-routing)
* **API Gateway:** Google Cloud API Gateway
* **Core Services (GKE Autopilot):** Core Telehealth Service (Node.js/Go), Video Consultation Service (LiveKit), AI Symptom Checker Service (Python/FastAPI), Consent Management Service (Go), E-Prescription & Interoperability Gateway (Node.js/TypeScript with Java/Spring Boot FHIR Adapter), and Audit & Compliance Logging Service (Go)
* **Messaging & Storage:** Google Cloud Pub/Sub and Google Cloud SQL for PostgreSQL

## Relationships
* **Clients ➔ Ingress:** HTTPS/WSS via Google Cloud DNS geo-routing
* **API Gateway ➔ GKE Containers:** gRPC over mTLS for secure intra-cluster routing
* **GKE Containers ➔ Cloud SQL:** PostgreSQL Wire Protocol with TLS encryption
* **Services ➔ Pub/Sub:** Cloud Pub/Sub API over TLS for asynchronous event processing

## Technology Stack
* **Cloud Infrastructure:** GCP (`europe-west3` and `us-central1`) for regional data isolation
* **Orchestration:** Google Kubernetes Engine (GKE Autopilot) with OCI-compliant Docker containers to minimize operational overhead
* **Real-Time Media:** LiveKit containerized on GKE to maintain regional data boundaries
* **Interoperability:** HL7 FHIR adapters and national EU e-prescription protocols (e.g., eHDSI/OpenNCP)

## Rationale
This architecture guarantees strict regional data residency by deploying isolated GCP regions and GKE clusters. It satisfies GDPR, HIPAA, and EU MDR requirements through robust audit logging, consent management, and secure gRPC/mTLS communication.