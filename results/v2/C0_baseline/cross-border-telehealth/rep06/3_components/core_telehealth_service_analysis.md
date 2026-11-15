## Overview
- Cross-border telehealth platform providing video consultations, e-prescriptions, and AI symptom checking for EU and US patients.
- Enforces strict regional data residency and regulatory compliance (GDPR, HIPAA, EU MDR) on Google Cloud Platform.

## Key Elements
- **Users**: Patients (EU and US), Licensed Clinicians, Platform Administrators / Compliance Officers.
- **Containers**: Patient Mobile/Web App (Flutter / React), Clinician Portal (React), API Gateway (Envoy / Kong), Core Telehealth Service (Go on GKE), Interoperability & E-Prescription Adapter, Consent & Privacy Management Container, AI Orchestrator & Audit Service, LiveKit/WebRTC Media Relays (TURN / STEF), Regional Data Storage (Cloud SQL, Cloud Spanner, Cloud KMS, Redis).
- **Core Telehealth Service Components**: Session Orchestrator, Consent Interceptor, Audit Logger, ABAC Policy Engine, Graceful State Manager.

## Relationships
- **Patient/Clinician Apps -> API Gateway**: Sends user requests [HTTPS / WSS].
- **API Gateway -> Core Telehealth Service**: Routes core telehealth API calls [gRPC / mTLS (Istio Mesh)].
- **Session Orchestrator -> LiveKit/WebRTC Media Relays**: Manages video consultation streams [SRTP / DTLS].
- **Consent Interceptor -> Consent & Privacy Management Container**: Validates real-time patient consent tokens [gRPC / mTLS].
- **Session Orchestrator -> ABAC Policy Engine**: Queries access rights and consent scopes [In-memory Go function call / Open Policy Agent].
- **Session Orchestrator & Graceful State Manager -> Regional Data Storage**: Reads and writes regionally-scoped patient data and session states [SQL / Redis / Cloud KMS].

## Technology Stack
- **Cloud Provider**: GCP (`europe-west3` for EU, `us-central1` for US) for infrastructure-level geo-isolation.
- **Orchestration & Mesh**: Google Kubernetes Engine (GKE) with Istio service mesh for SPIFFE/SPIRE mTLS and traffic management.
- **Languages & Frameworks**: Go for core backend services; Flutter and React for client apps.
- **Security & Authorization**: Open Policy Agent (OPA) for embedded ABAC; GCP Secret Manager and Cloud KMS for CMEK encryption.
- **Observability & State**: Prometheus and OpenTelemetry for telemetry and SLO monitoring; Redis for transient session state management during degraded connectivity.

## Rationale
- Infrastructure isolation and regional Cloud KMS key management guarantee strict adherence to GDPR and HIPAA data residency constraints.
- Embedded OPA policies and dedicated session orchestration ensure sub-50ms authorization checks and resilient, low-bandwidth video consultation capabilities.