## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checking for patients in the EU and the US. It ensures strict data residency, regulatory compliance, and high availability across unstable rural networks.

## Key Elements
- Patients & Clinicians (Users)
- Identity Providers (IdP), Payment Gateway, External Pharmacy Systems (External Systems)
- Single-Page Application / Mobile App (Flutter/TypeScript)
- API Gateway (Cloud API Gateway)
- Core Telehealth Service (Go/gRPC)
- AI Inference Wrapper (Python/FastAPI)
- SFU Media Server / LiveKit (GKE)
- US FHIR Adapter (Node.js/TypeScript)
- EU E-Prescription Gateway (Java/Spring Boot)
- Cloud SQL PostgreSQL & Cloud Storage (Data Storage)

## Relationships
- Patients/Clinicians interact with SPA/Mobile App via HTTPS and WebSockets.
- SPA/Mobile App communicates with API Gateway via HTTPS/mTLS.
- API Gateway routes traffic to Core Telehealth Service, AI Inference Wrapper, US FHIR Adapter, and EU E-Prescription Gateway via gRPC and HTTPS.
- SFU Media Server handles peer-to-peer and relayed video streams for consultations via WebRTC/UDP.
- US FHIR Adapter integrates with US pharmacy systems via HTTPS/REST.
- EU E-Prescription Gateway integrates with national e-prescription standards via mTLS, SOAP, and REST.

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` for strict regional data residency.
- Google Kubernetes Engine (GKE): Orchestrates region-isolated container clusters.
- Flutter / TypeScript: Powers cross-platform client applications.
- Go / gRPC: Implements high-performance Core Telehealth Service.
- Python / FastAPI: Manages AI Symptom Checker inference and traceability logging.
- LiveKit: Provides SFU media streaming with adaptive bitrate for rural connections.
- Node.js / TypeScript & Java / Spring Boot: Handles regional interoperability adapters.
- Cloud SQL (PostgreSQL) & Cloud Storage: Secures partitioned regional data storage.

## Rationale
Region-isolated GKE clusters and partitioned PostgreSQL databases guarantee compliance with GDPR and HIPAA by ensuring patient data never leaves its source region. Dedicated SFU media servers and localized integration adapters ensure low-bandwidth resilience and seamless interoperability with regional healthcare standards.