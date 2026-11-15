## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. Its core purpose is to deliver secure, regionally compliant telemedicine services meeting strict GDPR and HIPAA mandates.]

## Key Elements
* Patients (EU & US)
* Licensed Clinicians
* Patient Frontend Container (Distroless / Web)
* Clinician Frontend Container (Distroless / Web)
* API Gateway (Istio Service Mesh / Envoy)
* WebRTC SFU (Mediasoup / coturn)
* AI Symptom Checker Container (Python / TensorFlow / Distroless)
* Cloud WAF (Google Cloud WAF)
* WORM Cloud Storage (Google Cloud Storage)
* Regional GKE Clusters (europe-west3, us-central1)

## Relationships
* Patients and Clinicians access Frontend Containers via HTTPS over TLS 1.3 using Google Cloud CDN and Google Cloud WAF.
* Frontend Containers communicate with API Gateway using mTLS via Istio Service Mesh.
* API Gateway routes regional requests to Patient and Clinician Frontend Containers and backend services within Google Kubernetes Engine (GKE).
* WebRTC SFU handles video and audio consultations using WebRTC protocol.

## Technology Stack
* Google Cloud Platform (GCP) for cloud infrastructure across europe-west3 and us-central1.
* Google Kubernetes Engine (GKE) for container orchestration and regional data isolation.
* Istio Service Mesh and Envoy for mTLS and traffic routing.
* Distroless container images for minimized security attack surface.
* Python and TensorFlow for the AI Symptom Checker Container.
* Mediasoup and coturn for WebRTC SFU video streaming and audio fallback (R-06).

## Rationale
[This architecture enforces strict regional data residency by pinning traffic and data storage to europe-west3 and us-central1 via Google Cloud WAF and GKE clusters. It ensures high availability and security for cross-border telemedicine through Distroless containers, Istio mTLS, and Backend-for-Frontend session management.]