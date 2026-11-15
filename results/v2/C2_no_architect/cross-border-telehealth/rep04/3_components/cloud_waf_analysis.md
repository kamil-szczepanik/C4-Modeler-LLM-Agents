## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and high availability over unstable connections.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Google Cloud Armor (Cloud WAF)
- API Gateway (Istio Service Mesh / Envoy)
- Regional GKE Clusters (`europe-west3` and `us-central1`)
- WebRTC SFU (Mediasoup / coturn)
- AI Symptom Checker Container (Python / TensorFlow)
- Google Cloud Logging and BigQuery

## Relationships
- Patients and Clinicians connect to Google Cloud Armor via HTTPS/WebSockets.
- Google Cloud Armor enforces mTLS to the API Gateway (Istio / Envoy).
- API Gateway routes authenticated requests to regional GKE Clusters (`europe-west3`, `us-central1`).
- Cloud WAF streams sanitized security telemetry to regional Google Cloud Logging and BigQuery datasets.

## Technology Stack
- Google Cloud Armor: Provides edge WAF protection, geo-routing, and DDoS mitigation with isolated regional policies.
- Istio Service Mesh / Envoy: Manages ingress traffic, mTLS, and API routing.
- Terraform: Enforces Infrastructure-as-Code and drift detection across regions.
- Google Cloud Logging / BigQuery: Stores regionally segregated, PHI-minimized audit and security logs.

## Rationale
This architecture enforces strict regional data residency and compliance via isolated GCP regions and WAF policies. It protects vulnerable rural connections through session-token rate-limiting and low-overhead inspection profiles.