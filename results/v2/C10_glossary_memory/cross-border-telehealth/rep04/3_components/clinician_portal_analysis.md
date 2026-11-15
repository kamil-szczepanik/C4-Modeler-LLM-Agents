## Overview
The Cross-Border Telehealth Platform is a healthcare system delivering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Clinician Portal component enables licensed medical professionals to manage consultations, review traceable AI recommendations, and issue cross-border e-prescriptions securely.

## Key Elements
- **Clinician Portal**: React SPA providing the clinician user interface (Hosted on GCP Cloud Storage / Cloud CDN).
- **Consultation Workspace Component**: Manages live video feeds and low-bandwidth fallback tools.
- **AI Audit Reviewer Component**: Displays traceable AI symptom-checker recommendations and model versions.
- **E-Prescription Dashboard Component**: Interfaces with regional standards and features a Cross-Border Pharmacy Routing Indicator.
- **Portal Navigation Shell Component**: Manages layout routing, role-based view rendering, and error boundaries.
- **Portal State Management Component**: Redux Toolkit/React Query managing session state, RBAC, and inactivity timeouts without caching PHI/PII.
- **API Client Component**: Axios/WebSockets client handling secure egress with OpenTelemetry distributed tracing.

## Relationships
- Clinician Portal -> GCP Cloud Storage / Cloud CDN: Serves static SPA assets globally per region [HTTPS]
- Clinician Portal -> Regional Identity & Consent Providers: Authenticates clinicians via OIDC with short-lived JWTs [HTTPS]
- Clinician Portal -> API Gateway & Routing Service: Routes all outbound traffic via API Client Component [HTTPS]
- Portal Navigation Shell Component -> Consultation Workspace Component: Renders active consultation view [React Props / State]
- Portal Navigation Shell Component -> AI Audit Reviewer Component: Renders audit logs view [React Props / State]
- Portal Navigation Shell Component -> E-Prescription Dashboard Component: Renders prescription and routing view [React Props / State]
- Consultation Workspace Component -> API Client Component: Fetches video stream metadata [HTTPS / WebSockets]
- AI Audit Reviewer Component -> API Client Component: Queries traceable AI logs [HTTPS]
- E-Prescription Dashboard Component -> API Client Component: Submits prescriptions [HTTPS]

## Technology Stack
- **React SPA**: Powers the Clinician Portal UI for rapid component rendering and modular architecture.
- **Redux Toolkit / React Query**: Manages local session caching, RBAC, and secure state handling.
- **Axios / WebSockets**: Handles asynchronous communication and real-time data streaming.
- **GCP Cloud Storage & Cloud CDN**: Provides low-latency static asset delivery in `europe-west3` and `us-central1`.
- **OpenTelemetry**: Enables Real User Monitoring (RUM) and distributed tracing for client-side observability.

## Rationale
This architecture ensures secure, low-latency access for clinicians while strictly enforcing regional data privacy and compliance mandates. Centralizing communication through an API client and leveraging GCP Cloud CDN supports high availability and regulatory accountability across EU and US jurisdictions.