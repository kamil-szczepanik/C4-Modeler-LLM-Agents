## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict data residency, regulatory compliance (GDPR and HIPAA), and low-bandwidth resilience.

## Key Elements
- Patients and Licensed Clinicians (People)
- Google Cloud Global Load Balancer with Cloud Armor (System Edge)
- Regional API Gateway / BFF instances deployed in `europe-west3` (EU) and `us-central1` (US) (Containers)
- Core Telehealth Service, Video Consultation Service, AI Orchestrator, and E-Prescription Integrator (Containers)
- Region Router & Enforcement Filter, Authentication & Consent Interceptor, and Regional Service Router (Components)
- External Systems: National Pharmacy Networks, US Pharmacy Systems, AI Model Provider, Identity Providers

## Relationships
- Global Load Balancer -> Regional API Gateway / BFF: Routes geo-targeted traffic [HTTPS]
- Authentication & Consent Interceptor -> Regional Service Router: Forwards validated requests [In-process function call]
- Regional API Gateway / BFF -> Core Telehealth Service: Manages profiles and appointments [gRPC over mTLS via Istio]
- Regional API Gateway / BFF -> Video Consultation Service: Connects real-time video [gRPC over mTLS via Istio]
- Regional API Gateway / BFF -> AI Orchestrator: Sends AI symptom analysis requests [gRPC over mTLS via Istio]
- Regional API Gateway / BFF -> E-Prescription Integrator: Requests e-prescription processing [gRPC over mTLS via Istio]

## Technology Stack
- Google Cloud Platform (`europe-west3`, `us-central1`): Enforces regional data residency constraints (R-05).
- Go (Golang): Used for regional API Gateway / BFF development to ensure high performance and low latency.
- gRPC over mTLS via Istio: Provides secure, encrypted service-to-service internal communication.
- WebRTC SFU (LiveKit): Powers video consultations with degraded mode support for low-bandwidth connections (R-06).
- Python (FastAPI): Powers the AI Orchestrator for symptom checking (R-03, R-07).
- Java (Spring Boot): Powers the E-Prescription Integrator for interoperability (R-02, R-08).
- Cloud SQL (PostgreSQL), Cloud Storage, Cloud Bigtable: Secure regional data persistence.

## Rationale
Deploying regional API Gateway / BFF instances with geo-routing ensures health data never leaves its required jurisdiction, satisfying GDPR and HIPAA constraints. Internal gRPC/mTLS communication via Istio guarantees secure, high-performance microservice interactions across regional GCP clusters.