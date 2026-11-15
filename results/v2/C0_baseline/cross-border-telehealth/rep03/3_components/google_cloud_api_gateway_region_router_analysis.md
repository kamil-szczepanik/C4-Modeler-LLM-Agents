## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency and compliance with GDPR and HIPAA mandates.

## Key Elements
* React / Flutter Web and Mobile Apps
* Google Cloud API Gateway / Region Router (Envoy/Istio Ingress Mesh)
* Go / Spring Boot Core Telehealth Backends
* LiveKit / WebRTC SFU Video Media Servers
* Python / FastAPI + TensorFlow AI Symptom Checker Container
* Open Policy Agent (OPA) Consent Management Container
* Google Cloud SQL, Google Cloud Storage, and Cloud KMS

## Relationships
* React / Flutter Apps -> Google Cloud API Gateway / Region Router: Sends API requests and traffic [HTTPS]
* Google Cloud API Gateway / Region Router -> Go / Spring Boot Core Telehealth Backends: Routes validated payloads [gRPC over Istio mTLS mesh]
* Go / Spring Boot Core Telehealth Backends -> Google Cloud SQL: Persists regional health data [PostgreSQL protocol over mTLS]
* React / Flutter Apps -> LiveKit / WebRTC SFU Video Media Servers: Streams video consultations [WebRTC / TURN/STUN]

## Technology Stack
* GCP (europe-west3, us-central1): Chosen for regional control and strict data residency compliance.
* Envoy / Istio Ingress Mesh: Selected for advanced traffic routing, mTLS, and resiliency features.
* Go / Spring Boot: Utilized for high-performance, scalable core backend services.
* TensorFlow / FastAPI: Deployed for traceable AI symptom checking and urgency recommendations.

## Rationale
This architecture ensures strict geographic data separation between the EU and the US to satisfy GDPR and HIPAA requirements. The Envoy-based edge mesh provides essential resilience and circuit breaking to support rural patients with unstable connections.