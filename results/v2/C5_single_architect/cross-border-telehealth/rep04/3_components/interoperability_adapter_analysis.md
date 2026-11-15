## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, regulatory compliance, and localized interoperability.

## Key Elements
- **Patient & Clinician**: End users accessing the platform via Web/Mobile SPA/PWA.
- **Google Cloud API Gateway**: Manages ingress traffic.
- **Data Residency & Consent Router**: Go-based service routing data per region.
- **Core Services Backend**: Go/Spring Boot application managing core business logic.
- **AI Symptom Checker Service**: Python/FastAPI medical device supporting trace logging.
- **Video Streaming Server**: LiveKit WebRTC SFU on Google Kubernetes Engine (GKE).
- **Interoperability Adapter**: Node.js/TypeScript container decomposed into:
  - **Regional Routing Enforcer** (TypeScript)
  - **FHIR Translation Engine** (TypeScript/HAPI FHIR JS)
  - **EU National Standard Transformer** (TypeScript)
  - **Outbound Integration Dispatcher** (TypeScript/Axios)
- **Cloud SQL PostgreSQL**: Regional database instances.
- **External Systems**: External Pharmacy Systems, National Health Registries, National Identity Providers, AI Model Provider API.

## Relationships
- Core Services Backend -> Regional Routing Enforcer: Sends canonical health records with region tags [gRPC]
- Regional Routing Enforcer -> FHIR Translation Engine / EU National Standard Transformer: Routes payloads based on jurisdiction [In-memory]
- FHIR Translation Engine -> Outbound Integration Dispatcher: Passes validated US FHIR resources [In-memory]
- EU National Standard Transformer -> Outbound Integration Dispatcher: Passes localized EU payloads [In-memory]
- Outbound Integration Dispatcher -> External Pharmacy Systems / National Health Registries: Dispatches payloads [HTTPS/Mutual TLS, REST/FHIR]
- Web/Mobile Client -> Google Cloud API Gateway -> Data Residency & Consent Router -> Core Services Backend [HTTPS/gRPC]

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (GCP regions `europe-west3` and `us-central1`) for regional data isolation.
- **Backend & Adapters**: Go, Spring Boot, Python (FastAPI), Node.js, and TypeScript.
- **Frontend**: Flutter and React for Web/Mobile SPA/PWA.
- **Streaming**: LiveKit WebRTC SFU on GKE for resilient low-bandwidth video.
- **Database & Protocols**: Cloud SQL PostgreSQL, gRPC for internal service communication, HTTPS with mTLS for external integrations, and HL7 FHIR for US interoperability.

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating EU and US data processing within dedicated GCP regions using a Regional Routing Enforcer. Decoupling regional schema transformations from egress handling ensures reliable, compliant data exchanges with external pharmacies and health registries.