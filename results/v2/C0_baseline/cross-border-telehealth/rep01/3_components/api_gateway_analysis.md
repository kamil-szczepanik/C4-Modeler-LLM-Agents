## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, regulatory compliance (GDPR/HIPAA), and adaptive connectivity for rural users.

## Key Elements
- Patients (Urban and Rural) & Licensed Clinicians
- Pharmacists & Compliance Officers
- Regional API Gateways (Envoy Proxy / Apigee)
- Regional Application Services (Google Kubernetes Engine - GKE)
- WebRTC Media Servers & Policy/Consent Engine (Open Policy Agent - OPA)
- AI Symptom Checker (Vertex AI endpoints)

## Relationships
- Patients & Clinicians -> Regional API Gateways: HTTPS and WSS via TLS 1.3
- Regional API Gateways -> Regional Application Services: gRPC over Istio mTLS
- Regional API Gateways -> WebRTC Media Servers: WSS signaling and session setup
- Regional API Gateways -> AI Symptom Checker: gRPC with `X-Audit-Context` headers

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency compliance (GDPR/HIPAA).
- Envoy Proxy / Apigee: Handles geo-routing, TLS termination, consent validation, and schema checking.
- Google Kubernetes Engine (GKE): Hosts scalable regional application microservices.
- Open Policy Agent (OPA): Evaluates patient consent policies dynamically.
- Istio: Enforces mTLS service mesh security and circuit breaking.

## Rationale
Regional API gateways behind Anycast DNS guarantee that EU and US health data remain physically isolated within their respective jurisdictions. Offloading WebRTC video streams and utilizing Envoy-based edge routing protect availability and performance for rural users on unstable connections.