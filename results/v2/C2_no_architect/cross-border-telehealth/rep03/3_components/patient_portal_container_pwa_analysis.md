## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and resilience for rural users with unstable internet connections.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Patient Portal Container (PWA) with offline IndexedDB storage and Web Crypto API encryption
- Clinical Workspace Container with LiveKit WebRTC SFU
- Consent & Compliance Container with Istio service mesh and WORM BigQuery
- External Systems: Local Pharmacies and Vertex AI

## Relationships
- Patients (EU/US) -> Patient Portal Container (PWA): Accesses telehealth and symptom checker via HTTPS, WebRTC, and OAuth2/OIDC via Identity-Aware Proxy (IAP)
- Patient Portal Container (PWA) -> Consent & Compliance Container: Validates consent and logs emergency break-glass overrides via mTLS and OAuth2 inside GKE
- Patient Portal Container (PWA) -> Vertex AI: Processes symptom checker inputs with logged model versions

## Technology Stack
- Google Cloud Platform (GCP): Deployed in `europe-west3` and `us-central1` to enforce strict regional data residency
- Google Cloud CDN: Distributes the PWA with regional backends to guarantee edge compliance and low latency
- Web Crypto API: Secures cached local health data and consent states in IndexedDB using PIN or biometric-derived keys
- Istio Service Mesh: Manages secure, authenticated mTLS service-to-service communication within GKE

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating regional data while offering an offline-first PWA to support rural users. It balances strict security, auditability, and adaptive low-bandwidth availability for critical healthcare workflows.